from django.shortcuts import render
from booknotes.models import Book

def search(request):
    if 'query' in request.GET:
        query = request.GET['query']

        if not query:
            return render(request, 'search_form.html', {'error': True})

        books = Book.objects.filter(title__icontains=query)
        return render(request, 'search_result.html',
                {'books': books, 'query': query})
    else:
        return render(request, 'search_form.html', {'error': False})
