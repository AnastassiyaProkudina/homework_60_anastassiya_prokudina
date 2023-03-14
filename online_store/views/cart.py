from django.db.models import Q, F, Sum
from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView

from online_store.models import Cart, Product


class CartView(ListView):
    template_name = "cart/cart.html"
    model = Product
    context_object_name = "products"
    ordering = ("id",)

    def get_queryset(self):
        queryset = (
            super()
            .get_queryset()
            .filter(Q(carts__qty__gt=0))
            .annotate(total=F("carts__qty") * F("price"))
        )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["result"] = Product.objects.get_total_result()
        return context


class ProductCartCreateView(TemplateView):
    model = Cart
    template_name = "products/index.html"

    def post(self, request, **kwargs):
        product_in_cart = Cart.objects.filter(product_id=kwargs["pk"])
        if product_in_cart:
            balance = Product.objects.get_balance(pk=kwargs["pk"])
            qty = Cart.objects.get_qty(product_id=kwargs["pk"])
            if balance >= qty:
                product_in_cart.update(qty=qty)
            else:
                message = f"Unable to add to cart. Only {balance}pcs in stock."
        else:
            Cart.objects.create(product_id=kwargs["pk"], qty=1)
        return redirect("index")
