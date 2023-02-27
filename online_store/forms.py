from django import forms
from django.core.exceptions import ValidationError

from online_store.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "category", "price", "image", "balance", "description"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 2:
            raise ValidationError("Заголовок должен быть длиннее двух символов")
        return title

    def clean_balance(self):
        balance = self.cleaned_data.get("balance")
        if balance < 0:
            raise ValidationError("Остаток должен быть больше одного")
        return balance


class SearchForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Search Product...",
                    "style": "border-color: #da7b93; font-size: 16px; position: absolute;",
                }
            )
        }
        labels = {"title": ""}
