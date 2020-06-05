# Generated by Django 3.0.6 on 2020-06-04 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_books', '0008_digital_book_rating'),
        ('comments', '0029_auto_20200604_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='digital_books.Digital_Book'),
        ),
    ]