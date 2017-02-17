from django.shortcuts import render
from booknotes.models import Book

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'query' in request.GET and request.GET['query']:
        query = request.GET['query']
        books = Book.objects.filter(title__icontains=query)
        return render(request, 'search_result.html',
                {'books': books, 'query': query})
    else:
        return render(request, 'search_form.html', {'error': True})
