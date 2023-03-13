from django.views.generic import ListView

from online_store.models import ProductInCart


class CartView(ListView):
    template_name = 'products/cart.html'
    model = ProductInCart
    context_object_name = 'cart'
    ordering = ('id',)

    def get_queryset(self):
        queryset = super().get_queryset().filter(qty__gt=0)
        return queryset
