# Generated by Django 3.0.6 on 2020-06-05 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_books', '0008_digital_book_rating'),
        ('digitalBooksPDF', '0043_auto_20200605_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitalbookpdf',
            name='book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='digital_books.Digital_Book'),
        ),
    ]