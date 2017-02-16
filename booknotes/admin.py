from django.contrib import admin
from .models import Author, Book, Publisher

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
admin.site.register(Publisher)
