# Generated by Django 3.0.6 on 2020-06-06 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_books', '0008_digital_book_rating'),
        ('electronicbookcollections', '0062_auto_20200606_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronicbookcollection',
            name='digital_books',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='digital_books.Digital_Book'),
        ),
    ]
