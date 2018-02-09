from django.db import models

# Create your models here.

class Genre (models.Model):
    genre = models.CharField(max_length=50,blank=True ,null=True , default=None )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  "Жанр %s" % self.genre

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Books (models.Model):
    name_genre = models.ForeignKey(Genre , on_delete=models.CASCADE , blank=True ,null=True , default=None)
    name_book=models.CharField(max_length=50 , blank=True , null=True , default=None)
    name_author = models.CharField(max_length=50 , blank=True , null=True, default=None)
    name_country = models.CharField(max_length=50 , blank=True, null=True, default=None)
    year_data = models.CharField(max_length=50 , blank=True, null=True , default=None)
    discriptions = models.TextField(blank=True,null=True , default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Книга %s" % self.name_book

    class Meta:
        verbose_name = "Книг"
        verbose_name_plural = "Книги"


class BookImageAndFile(models.Model):
    book = models.ForeignKey(Books , on_delete=models.CASCADE , blank=True , null=True, default=None)
    book_image = models.ImageField('/media/books_images/')
    pdf_file = models.FileField('/media/books_file/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "фотография и файл %s" % self.id

    class Meta:
        verbose_name = "Фотография и файл"
        verbose_name_plural = "Фотографии и файлы"