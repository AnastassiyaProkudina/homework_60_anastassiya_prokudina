from django.contrib import admin

from online_store.models import Product, Cart, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "image",
        "category",
        "balance",
        "price",
        "created_at",
        "updated_at",
        "is_deleted",
        "deleted_at",
    )
    list_filter = ("title", "category", "price", "balance")
    fields = ("title", "description", "image", "category", "balance", "price")


class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "qty")
    list_filter = ("id", "product", "qty")
    fields = ("id", "product", "qty")


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "phone",
        "address",
    )
    list_filter = ("name", "phone", "id")
    fields = (
        "id",
        "name",
        "phone",
        "address",
        "product",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
