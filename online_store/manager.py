from django.db.models import Manager, Sum, Q, F


class ProductManager(Manager):
    def get_balance(self, pk):
        return self.get_queryset().get(pk=pk).balance

    def get_total_result(self):
        result = (
            self.get_queryset()
            .filter(carts__qty__gt=0)
            .annotate(total=F("carts__qty") * F("price"))
            .aggregate(Sum("total"))
        )

        return float(result["total__sum"])


class CartManager(Manager):
    def get_qty(self, product_id):
        product_qty = (
            self.get_queryset().filter(product_id=product_id).aggregate(Sum("qty"))
        )
        return product_qty["qty__sum"]

        # products_in_cart = Cart.objects.all()
        # for product_in_cart in products_in_cart:
        #     if product_in_cart.pk == pk:
        #         product_in_cart.qty += 1
        # if product_in_cart.qty > balance:
        #     return None
        # i.save()
