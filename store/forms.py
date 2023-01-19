from django import forms
from store.models import Product

class addProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("thumbnail", "categorie" )


