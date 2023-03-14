from django import forms
from django.core.exceptions import ValidationError

from online_store.models import Product, Cart, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "category", "price", "image", "balance", "description"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 2:
            raise ValidationError("Title must be longer than two characters!")
        return title


class SimpleSearchForm(forms.Form):
    search = forms.CharField(
        max_length=30,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search Product...",
                "style": "border: solid #da7b93 2px; font-size: 16px; position: absolute;",
            }
        ),
    )


class ProductCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = [
            "qty",
        ]

    def clean_qty(self, pk):
        qty = self.cleaned_data.get("qty")
        balance = Product.objects.get_balance(pk=pk)
        if qty > balance:
            raise ValidationError(f"Max quantity is : {balance}!")
        return qty


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "name",
            "address",
            "phone",
        ]
