from django.shortcuts import render
from django.http import HttpResponse

books = [
    {'id': 1, 'name': 'SOS', 'author': 'Jon Miller', 'price': 37000},
    {'id': 2, 'name': 'Athom Odatlar', 'author': 'Jeyms Klir', 'price': 40000},
    {'id': 3, 'name': 'Urush va Tinchlik', 'author': 'Lev Tolstoy', 'price': 85000},
    {'id': 4, 'name': 'Telba', 'author': 'Dostoyevskiy', 'price': 100000}
]


def home(request):
    context = {
        'books': books
    }
    return render(request, 'main/index.html', context)


def book_detail(request, book_id):
    for book in books:
        if book.get('id') == book_id:
            context = {
                'book': book
            }
            return render(request, 'main/detail.html', context)
    return HttpResponse('Bunday book mavjud emas', status=404)