from django.shortcuts import render
from django.http import Http404
from .forms import ProductForm


# Rozszerzona lista do dokładnie 5 elementów (dodano ID 4 i 5)
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 2999, "category": "laptops", "is_available": True},
    {"id": 2, "name": "Mysz", "price": 49, "category": "accessories", "is_available": False},
    {"id": 3, "name": "Klawiatura", "price": 199, "category": "accessories", "is_available": True},
    {"id": 4, "name": "Monitor", "price": 899, "category": "monitors", "is_available": False},  # <-- NOWY
    {"id": 5, "name": "Słuchawki", "price": 250, "category": "audio", "is_available": True},    # <-- NOWY
]


def index(request):
    return render(request, template_name='shop/index.html', context={"project_name": "Sklep 4TP", "user_name": "Ania"})


def product_list(request):
    return render(request, template_name='shop/product_list.html', context={'products': PRODUCTS})


def product_detail(request, product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if product is None:
        raise Http404("Nie ma takiego produktu")  # Dzięki importowi z linii 2 to teraz zadziała
    return render(request, template_name='shop/product_detail.html', context={'product': product})


def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            PRODUCTS.append({"id": len(PRODUCTS) + 1, **data})
            return redirect("shop:product_list")
    else:
        form = ProductForm()
    return render(request, template_name='shop/product_form.html', context={'form': form})
