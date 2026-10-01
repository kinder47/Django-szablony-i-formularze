## Migracja szablonu product_list.html z Flask (Jinja2) do Django (DTL)

Podczas przepisywania widoku tabeli listy produktów z Flaska na Django Template Language (DTL), wprowadzono **5 kluczowych zmian**:

| Lp. | Element we Flasku (Jinja2) | Element w Django (DTL) | Opis zmiany |
| :--- | :--- | :--- | :--- |
| **1.** | `loop.index` | `forloop.counter` | W DTL licznik pętli do iterowania wierszy tabeli (od 1) nazywa się `forloop.counter` zamiast Flaskowego `loop.index`. |
| **2.** | `url_for('product_detail', id=item.id)` | `url 'shop:product_detail' item.id` | Zmiana składni generowania URL na format Django bez nawiasów, z uwzględnieniem przestrzeni nazw (`shop:`) oraz przekazaniem ID jako argumentu pozycyjnego. |
| **3.** | `{% if not products %} ... {% endif %}` | `{% empty %}` | Zastąpienie zewnętrznego warunku sprawdzającego Flask natywną sekcją rezerwową `{% empty %}` wewnątrz pętli `{% for %}` w DTL. |
| **4.** | `item.is_available` (tekstowo) | `item.is_available\|yesno:"Dostępny,Niedostępny"` | Zamiast instrukcji warunkowej `if/else` dla wyświetlania statusu, w DTL użyto wbudowanego filtra `\|yesno` mapującego wartość logiczną na polskie odpowiedniki tekstowe. |
| **5.** | Ogólna składnia komentarzy `{# ... #}` | Komentarze szablonu Django | Komentarze w DTL przyjmują postać jednoulinijkową `{# komentarz #}` (użyte w liniach 25 i 30) zamiast składni blokowej lub specyficznej dla Jinja2. |
