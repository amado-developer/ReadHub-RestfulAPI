# Generated by Django 3.0.6 on 2020-05-27 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_books', '0001_initial'),
        ('inventories', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='book',
        ),
        migrations.AddField(
            model_name='inventory',
            name='digital_book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='digital_books.digital_book'),
        ),
    ]
