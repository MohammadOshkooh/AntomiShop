from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, FormView

from tag.models import Tag
from .forms import CommentForm
from blog.models import Article, BlogComment, ArticleCategory
from django.contrib import messages


class BlogListView(ListView):
    model = Article
    template_name = 'blog.html'
    context_object_name = 'articles'
    paginate_by = 1

    def get_queryset(self):
        queryset = Article.objects.all()

        # --- Search ---
        search = self.request.GET.get('search')
        if search is not None:
            queryset = queryset.filter(title__icontains=search)

        # -- Category --
        category = self.request.GET.get('category')
        if category is not None:
            queryset = queryset.filter(category__title=category)

        # --- Tag ---
        tag = self.request.GET.get('tag')
        if tag is not None:
            queryset = queryset.filter(tag__title=tag)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogListView, self).get_context_data()
        context['comments'] = BlogComment.objects.all()
        context['categories'] = ArticleCategory.objects.all()
        context['tags'] = Tag.objects.all()
        context['command'] = 'list'

        return context


class BlogDetailView(DetailView, FormView):
    form_class = CommentForm
    model = Article
    template_name = 'blog_details.html'
    context_object_name = 'article'

    def form_valid(self, form):
        # get parent_id from hidden input
        try:
            parent_id = int(self.request.POST.get('parent_id'))
        except:
            parent_id = None
        # if parent_id has been submitted get parent_obj id
        if parent_id:
            parent_object = BlogComment.objects.get(id=parent_id)
            # if parent_object is exist
            if parent_object:
                # create reply comment
                reply_comment = form.save(commit=False)
                reply_comment.parent = parent_object

        # normal comment
        new_comment = form.save(commit=False)
        new_comment.owner = self.request.user
        article = Article.objects.filter(pk=self.kwargs.get('pk')).first()
        new_comment.article = article
        new_comment.save()
        messages.success(self.request, 'کامنت با موفقست ثبت شد')
        return redirect(article.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        comments = BlogComment.objects.filter(article=kwargs['object'])
        context['comments'] = comments
        comment_main_parents = BlogComment.objects.filter(parent=None)
        context['comment_main_parents'] = comment_main_parents
        context['articles'] = Article.objects.all()
        context['categories'] = ArticleCategory.objects.all()
        context['tags'] = Tag.objects.all()
        context['command'] = 'detail'

        return context
