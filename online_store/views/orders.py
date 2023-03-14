from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from online_store.forms import OrderForm
from online_store.models import Order, Cart


class OrderDetailView(DetailView):
    template_name = "orders/order.html"
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.filter(id=self.object.pk)
        context["order"] = order

        return context


class OrderCreateView(CreateView):
    template_name = "orders/order_create.html"
    model = Order
    form_class = OrderForm

    def post(self, request, **kwargs):
        products = request.POST.get(pk=kwargs['pk'])
        print(products)
        return redirect("order_detail", kwargs={"pk": self.object.pk})


    def get_success_url(self):
        return reverse("order_detail", kwargs={"pk": self.object.pk})
