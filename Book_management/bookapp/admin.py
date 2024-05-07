# book_management_app/admin.py
from django.contrib import admin
from .models import User, Book, Author, ReadingList, ReadingListBook

class ReadingListBookInline(admin.TabularInline):
    model = ReadingListBook
    extra = 1

class ReadingListAdmin(admin.ModelAdmin):
    inlines = (ReadingListBookInline,)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'publication_date')
    search_fields = ('title', 'genre')
    filter_horizontal = ('authors',)

admin.site.register(User)
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(ReadingList, ReadingListAdmin)
