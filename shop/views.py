from django.shortcuts import render


def index(request):
    return render(request, "shop/index.html", {"project_name": "Sklep 4TP", "user_name": "Ania"})

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 2999, "category": "laptops", "is_available": True},
    {"id": 2, "name": "Mysz", "price": 49, "category": "accessories", "is_available": False},
    {"id": 3, "name": "Klawiatura", "price": 199, "category": "accessories", "is_available": True},
]


def product_list(request):
    return render(request, "shop/product_list.html", {"products": PRODUCTS})


def product_detail(request, product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if product is None:
        raise Http404("Nie ma takiego produktu")
    return render(request, "shop/product_detail.html", {"product": product})

def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            PRODUCTS.append({"id": len(PRODUCTS) + 1, **data})
            return redirect("shop:product_list")
    else:
        form = ProductForm()
    return render(request, "shop/product_form.html", {"form": form})