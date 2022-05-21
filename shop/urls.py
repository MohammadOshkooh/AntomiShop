from django.urls import path

from .views import ProductList, ProductDetail, FavoritesView, ClearFavoritesList, AddFavoriteItems, \
    DeleteFavoriteItem

app_name = 'shop'

urlpatterns = [
    path('favorites-list/<pk>/clear/', ClearFavoritesList.as_view(), name='clear_favorites_list'),
    path('favorite-list/<slug>/remove/', DeleteFavoriteItem.as_view(), name='delete_favorite_item'),
    path('favorites-list/<slug>/create/', AddFavoriteItems.as_view(), name='add_favorites_items'),
    # path('favorites-list/<slug>/create/', add_favorite_items, name='add_favorites_items'),

    path('favorites-list/', FavoritesView.as_view(), name='favorites_list'),
    path('', ProductList.as_view(), name='product_list'),
    path('<slug:slug>', ProductDetail.as_view(), name='product_detail'),
]
