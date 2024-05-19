from django import forms
from .models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"  # ou liste os campos que você quer no formulário
