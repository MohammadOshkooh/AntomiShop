from django.urls import path, include

from .views import ProductList, product_detail, FavoritesView, ClearFavoritesList, AddFavoriteItems, \
    DeleteFavoriteItem

app_name = 'shop'

urlpatterns = [
    path('api/', include('shop.api.urls', namespace='shop_api')),

    path('favorites-list/<pk>/clear/', ClearFavoritesList.as_view(), name='clear_favorites_list'),
    path('favorite-list/<slug>/remove/', DeleteFavoriteItem.as_view(), name='delete_favorite_item'),
    path('favorites-list/<slug>/create/', AddFavoriteItems.as_view(), name='add_favorites_items'),

    path('favorites-list/', FavoritesView.as_view(), name='favorites_list'),
    path('', ProductList.as_view(), name='product_list'),
    path('<slug:slug>/', product_detail, name='product_detail'),

]
