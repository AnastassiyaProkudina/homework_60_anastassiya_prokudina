from django.urls import path

from online_store.views.base import products_list
from online_store.views.categories import *
from online_store.views.products import *

urlpatterns = [
    path("", products_list, name="index"),
    path("product/", products_list, name="index"),
    path("product/create", product_create, name="product_create"),
    path("product/<int:pk>", product_detail, name="product_detail"),
    path("product/<int:pk>/update/", product_update, name="product_update"),
    path("product/<int:pk>/delete/", product_delete, name="product_delete"),
    path(
        "product/<int:pk>/confirm_delete/",
        product_confirm_delete,
        name="product_confirm_delete",
    ),
    path("product/products_delete", products_delete, name="products_delete"),
    path("category/", categories_list, name="categories_list"),
    path("products/<pk>", category, name="category"),
]
