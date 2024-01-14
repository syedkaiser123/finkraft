from django.urls import path
from user_records import views as all_views

urlpatterns = [
    path('users/', all_views.UserListCreateView.as_view(), name='user-list-create'),
    path('products/', all_views.ProductListCreateView.as_view(), name='user-products'),
    path('products/<int:pk>/', all_views.ProductRetrieveView.as_view(), name='user-product-details'),
]