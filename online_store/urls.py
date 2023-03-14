from django.urls import path

from online_store.views.base import IndexView, IndexRedirectView
from online_store.views.cart import CartView, ProductCartCreateView
from online_store.views.categories import *
from online_store.views.products import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("product/", IndexRedirectView.as_view(), name="products_index_redirect"),
    path("product/create", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>", ProductDetail.as_view(), name="product_detail"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path(
        "product/<int:pk>/confirm_delete/",
        ProductDeleteView.as_view(),
        name="product_confirm_delete",
    ),
    path("product/products_delete", products_delete, name="products_delete"),
    path("category/", categories_list, name="categories_list"),
    path("products/<pk>", category, name="category"),
    path("cart/", CartView.as_view(), name="cart_list"),
    path(
        "product/<int:pk>/cart/add/",
        ProductCartCreateView.as_view(),
        name="product_cart_add",
    ),
]
