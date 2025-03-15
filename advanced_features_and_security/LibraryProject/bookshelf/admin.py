from django.contrib import admin

from .models import Book, CustomUser, CustomUserManager


class BookAdmin(admin.ModelAdmin):
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'author')

'''
"list_filter", "author", "publication_year"
'''
# Register your models here.
# admin.site.register(Book)
admin.ModelAdmin(Book,BookAdmin)

admin.site.register(CustomUser,CustomUserManager)