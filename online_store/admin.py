from django.contrib import admin

from online_store.models import Product


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


admin.site.register(Product, ProductAdmin)
