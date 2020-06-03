# Generated by Django 3.0.6 on 2020-06-02 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_books', '0008_digital_book_rating'),
        ('inventories', '0040_auto_20200602_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='digital_book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='digital_books.Digital_Book'),
        ),
    ]