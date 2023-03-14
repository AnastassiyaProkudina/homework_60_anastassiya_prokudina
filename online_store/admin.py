from django.contrib import admin

from online_store.models import Product, Cart


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


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
