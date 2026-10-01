from django import forms
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        label="Szukaj produktu",
        widget=forms.TextInput(attrs={'placeholder': 'Wpisz nazwę...'})
    )
    only_available = forms.BooleanField(
        required=False,
        label="Tylko dostępne"
    )


class ProductForm(forms.Form):
    CATEGORY_CHOICES = [
        ('elektronika', 'Elektronika'),
        ('odziez', 'Odzież'),
        ('dom', 'Dom i Ogród'),
    ]

    name = forms.CharField(max_length=100, label="Nazwa")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Cena")
    promo_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False, label="Cena promocyjna")
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="Kategoria")
    is_available = forms.BooleanField(required=False, label="Dostępny")
    description = forms.CharField(widget=forms.Textarea, required=False, label="Opis")

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and name.strip().lower() == 'test':
            raise ValidationError("Nazwa produktu nie może brzmieć 'test'.")
        return name

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        promo_price = cleaned_data.get('promo_price')

        if price and promo_price and promo_price >= price:
            self.add_error('promo_price', "Cena promocyjna musi być niższa niż cena regularna.")

        return cleaned_data
