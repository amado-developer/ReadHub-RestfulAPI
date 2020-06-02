# Generated by Django 3.0.6 on 2020-06-02 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_books', '0008_digital_book_rating'),
        ('adquisitions', '0018_auto_20200602_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='digital_books.Digital_Book'),
        ),
    ]
