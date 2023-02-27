from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from online_store.models import CategoryChoice, Product


def categories_list(request: WSGIRequest):
    context = {"choices": CategoryChoice.choices}
    return render(request, "categories/categories.html", context=context)


def category(request, pk):
    products = Product.objects.filter(is_deleted=False, category=pk)
    products.order_by("title").values()
    if not products:
        message = f"You have no products in category {pk}"
        context = {"message": message}
    else:
        message = f"You have {len(products)} product in category {pk}"
        context = {
            "products": products,
            "choices": CategoryChoice.choices,
            "message": message,
        }
    return render(request, "products/index.html", context=context)
