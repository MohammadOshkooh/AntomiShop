from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, FormView, DeleteView, CreateView

from shop.forms import ProductReviewForm, AddFavoriteItemForm
from shop.models import Product, Comment, ProductCategory, ProductTag, Favorite


class ProductList(ListView):
    model = Product
    template_name = 'shop/products_list.html'
    context_object_name = 'products'
    paginate_by = 16

    def get_queryset(self):
        queryset = Product.objects.filter(availability=True)

        # category filter
        category = self.request.GET.get('category')
        if category is not None:
            queryset = queryset.filter(category__title__contains=category)

        # tag filter
        tag = self.request.GET.get('tag')
        if tag is not None:
            queryset = queryset.filter(tag__title=tag)

        # filter price
        # price_min = self.request.GET.get('price_min')
        # price_max = self.request.GET.get('price_max')
        # if price_min is not None and price_max is not None:
        #     print('---------------------not none price filter ----------------')
        #     queryset = queryset.filter(current_price__range=range(0,1000))
        #     # queryset = queryset.filter(current_price__range=range(int(price_min), int(price_max)))
        #     print(range(int(price_min), int(price_max)))

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductList, self).get_context_data()
        main_parents = []
        for c in ProductCategory.objects.all():
            if c.parent is None:
                main_parents.append(c)

        context['categories'] = ProductCategory.objects.all()
        context['main_parents'] = main_parents
        context['tags'] = ProductTag.objects.all()
        return context


class ProductDetail(DetailView, FormView):
    model = Product
    template_name = 'shop/product_detail.html'
    queryset = Product.objects.filter(availability=True)
    context_object_name = 'product'

    form_class = ProductReviewForm

    def form_valid(self, form):
        user = self.request.user
        product = self.queryset.first()
        if user.is_authenticated:
            review_form = form.save(commit=False)
            review_form.owner = user
            review_form.product = product
            review_form.save()
            messages.success(self.request, 'نظر شما با موفقیت ثبت شد')
            return HttpResponseRedirect(product.get_absolute_url(), product.slug)
        else:
            messages.error(self.request, 'برای ثبت نظر لطفا لاگین کنید')
            return HttpResponseRedirect(reverse_lazy('account_login'))

    def form_invalid(self, form):
        return super(ProductDetail, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        product = kwargs['object']
        context['comments'] = Comment.objects.filter(is_active=True, product=product)
        return context


# ---- Favorite list ---- #

class FavoritesView(ListView):
    model = Favorite
    template_name = 'favorite_list/favorites_list.html'
    context_object_name = 'favorite_items'

    def get_queryset(self):
        queryset = Favorite.objects.filter(owner=self.request.user)
        return queryset


class ClearFavoritesList(DeleteView):
    model = Favorite
    success_url = reverse_lazy('shop:favorites_list')


# def delete_favorite_item(request, slug):
#     instance = Favorite.objects.filter(owner=request.user).first()
#     product = get_object_or_404(Product, slug=slug)
#     if instance is not None:
#         if request.method == 'POST':
#             instance.product.remove(product)
#             messages.success(request, 'ایتم با موفقیت از لیست علاقه مندی ها حذف شد')
#
#     return redirect('shop:favorites_list')
#

class DeleteFavoriteItem(FormView):
    model = Favorite
    form_class = AddFavoriteItemForm

    def form_valid(self, form):
        slug = self.kwargs.get('slug')
        instance = Favorite.objects.filter(owner=self.request.user).first()
        product = get_object_or_404(Product, slug=slug)
        if product in instance.product.all():
            instance.product.remove(product)
            messages.success(self.request, 'ایتم با موفقیت از لیست علاقه مندی ها حذف شد')

        return redirect('shop:favorites_list')


# def add_favorite_items(request, slug):
#     instance = Favorite.objects.filter(owner=request.user).first()
#     product = get_object_or_404(Product, slug=slug)
#     if instance is not None:
#         if request.method == 'POST':
#             if product in instance.product.all():
#                 messages.error(request, 'این ایتم از قبل در لیست علاقه مندی ها وجود دارد')
#             else:
#                 add_form = AddFavoriteItemForm(instance=instance, data=request.POST)
#                 add_form = add_form.save()
#                 add_form.product.add(product)
#                 messages.success(request, 'ایتم با موفقیت به لیست علاقه مندی ها اضافه شد')
#
#     else:  # instance in None -> favorite list not exist
#         if request.method == 'POST':
#             add_form = AddFavoriteItemForm()
#             # Favorite.objects.create(owner=request.user)
#             add_form = add_form.save(commit=False)
#             add_form.owner = request.user
#             add_form.save()
#             add_form.product.add(product)
#             messages.success(request, 'ایتم با موفقیت به لیست علاقه مندی ها اضافه شد')
#
#     return redirect('shop:product_detail', slug=slug)


class AddFavoriteItems(FormView):
    model = Favorite
    form_class = AddFavoriteItemForm()

    def get_success_url(self):
        return reverse('shop:product_detail', kwargs=[self.kwargs.get('slug')])

    def get_form(self, form_class=None):
        instance = Favorite.objects.filter(owner=self.request.user).first()
        if instance is not None:
            return AddFavoriteItemForm(instance=instance, data=self.request.POST)

    def form_valid(self, form):
        slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)
        instance = Favorite.objects.filter(owner=self.request.user).first()
        if instance is not None:
            if self.request.method == 'POST':
                if product in instance.product.all():
                    messages.error(self.request, 'این ایتم از قبل در لیست علاقه مندی ها وجود دارد')
                else:
                    form = form.save()
                    form.product.add(product)
                    messages.success(self.request, 'ایتم با موفقیت به لیست علاقه مندی ها اضافه شد')

        else:  # instance in None -> favorite list not exist
            if self.request.method == 'POST':
                # Favorite.objects.create(owner=request.user)
                form = form.save(commit=False)
                form.owner = self.request.user
                form.save()
                form.product.add(product)
                messages.success(self.request, 'ایتم با موفقیت به لیست علاقه مندی ها اضافه شد')

        return redirect('shop:product_detail', slug=slug)
