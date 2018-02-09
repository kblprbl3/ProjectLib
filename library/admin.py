from django.contrib import admin
from .models import *


class BookImageAndFileInline (admin.TabularInline):
    model = BookImageAndFile
    extra = 0


# Отображение таблицы в Admin Panel
class BooksAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Books._meta.fields]
    inlines = [BookImageAndFileInline]
    class Meta:
        module = Books


admin.site.register(Books, BooksAdmin)




# Отображение таблицы в Admin Panel
class GenreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Genre._meta.fields]

    class Meta:
        module = Genre


admin.site.register(Genre, GenreAdmin)


class BookImageAndFileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BookImageAndFile._meta.fields]

    class Meta:
        module = BookImageAndFile


admin.site.register(BookImageAndFile, BookImageAndFileAdmin)