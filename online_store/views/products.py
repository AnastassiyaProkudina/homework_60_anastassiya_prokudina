from django.shortcuts import render, redirect, get_object_or_404

from online_store.forms import ProductForm, SearchForm
from online_store.models import Product, CategoryChoice


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(
        request,
        "products/product.html",
        context={"product": product, "choices": CategoryChoice.choices},
    )


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect("product_detail", pk=product.pk)
    else:
        form = ProductForm()
    return render(
        request,
        "products/product_create.html",
        context={"form": form, "choices": CategoryChoice.choices},
    )


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST or None, instance=product)
        if form.is_valid():
            product.save()
            return redirect("product_detail", pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        "products/product_update.html",
        context={"form": form, "product": product},
    )


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(
        request, "products/product_confirm_delete.html", context={"product": product}
    )


def product_confirm_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect("index")


def products_delete(request):
    products = Product.objects.filter(is_deleted=False)
    if request.method == "POST":
        for product in products:
            x = request.POST.get(str(product.pk))
            print(x)
            if str(x) == "on":
                b = Product.objects.get(pk=product.pk)
                b.delete()
        return redirect("index")

    context = {"products": products, "choices": CategoryChoice.choices}
    return render(request, "products/products_delete.html", context=context)


#
# def product_search(request):
#     if request.method == "":
#         form = SearchForm(request.GET.)
#         if form.is_valid():
#             title = form.cleaned_data.get("title")
#             products = Product.objects.all().filter(is_deleted=False, balance__gte=0, title=title).order_by('title')
#             context = {"form": form, "products": products}
#             return render(request, "products/index.html", context=context)
