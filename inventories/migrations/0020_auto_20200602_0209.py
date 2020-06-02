# Generated by Django 3.0.6 on 2020-06-02 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_books', '0007_auto_20200527_2137'),
        ('inventories', '0019_auto_20200531_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='digital_book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='digital_books.Digital_Book'),
        ),
    ]
