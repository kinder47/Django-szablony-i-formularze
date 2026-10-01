from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        label="Szukaj produktu",
        widget=forms.TextInput(attrs={'placeholder': 'Wpisz nazwę...'})
    )
    only_available = forms.BooleanField(
        required=False,
        label="Tylko dostępne produkty"
    )

class ProductForm(forms.Form):
    CATEGORY_CHOICES = [
        ('elektronika', 'Elektronika'),
        ('odziez', 'Odzież'),
        ('dom', 'Dom i Ogród'),
    ]

    name = forms.CharField(max_length=100, label="Nazwa produktu")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Cena (zł)")
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="Kategoria")
    is_available = forms.BooleanField(required=False, initial=True, label="Dostępny w sklepie")
    description = forms.CharField(widget=forms.Textarea, required=False, label="Opis produktu")
