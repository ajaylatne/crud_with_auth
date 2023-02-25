from django import forms
from .models import Items

products = [('laptop', 'Laptop'), ('phone', 'SmartPhone'), ('Mixer', 'Mixer'), ('TV', 'TV'), ('Toy', 'Toy')]


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        exclude = ['order_no']
        widgets = {'address': forms.Textarea(attrs={'rows': 4}),
                   'delivery_date': forms.DateInput(attrs={'type': 'date'}),
                   'product_name': forms.Select(choices=products)
                   }
