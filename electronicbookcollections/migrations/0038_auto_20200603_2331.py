# Generated by Django 3.0.6 on 2020-06-03 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_books', '0008_digital_book_rating'),
        ('electronicbookcollections', '0037_auto_20200603_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronicbookcollection',
            name='digital_books',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='digital_books.Digital_Book'),
        ),
    ]
