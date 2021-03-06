# Generated by Django 2.0.2 on 2018-02-09 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookimageandfile',
            name='book_image',
            field=models.ImageField(upload_to='', verbose_name='/media/books_images/'),
        ),
        migrations.AlterField(
            model_name='bookimageandfile',
            name='pdf_file',
            field=models.FileField(upload_to='', verbose_name='/media/books_file/'),
        ),
    ]
