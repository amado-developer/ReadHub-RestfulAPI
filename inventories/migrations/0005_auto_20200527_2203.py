# Generated by Django 3.0.6 on 2020-05-27 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_books', '0007_auto_20200527_2137'),
        ('inventories', '0004_auto_20200527_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='digital_book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='digital_books.Digital_Book'),
        ),
    ]
