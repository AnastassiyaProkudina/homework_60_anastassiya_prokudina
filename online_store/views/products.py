from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView

from online_store.forms import ProductForm
from online_store.models import Product, CategoryChoice


class ProductDetail(DetailView):
    template_name = "products/product.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(id=self.object.pk)
        context['products'] = products
        context["choices"] = CategoryChoice.choices
        return context


class ProductCreateView(CreateView):
    template_name = "products/product_create.html"
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    template_name = "products/product_update.html"
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = "products/product_confirm_delete.html"
    model = Product
    success_url = reverse_lazy('index')





class ProductConfirmDeleteView(TemplateView):
    template_name = "products/product_confirm_delete.html"

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = get_object_or_404(Product, pk=kwargs["pk"])
        context["product"].delete()
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