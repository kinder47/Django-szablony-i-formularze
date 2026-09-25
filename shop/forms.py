from .forms import ProductForm, SearchForm


def product_list(request):
    form = SearchForm(request.GET)
    products = PRODUCTS
    if form.is_valid():
        q = form.cleaned_data["q"]
        if q:
            products = [p for p in products if q.lower() in p["name"].lower()]
        if form.cleaned_data["only_available"]:
            products = [p for p in products if p["is_available"]]
    return render(request, "shop/product_list.html", {"products": products, "form": form})