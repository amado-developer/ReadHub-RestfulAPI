# Generated by Django 3.0.6 on 2020-05-30 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital_books', '0007_auto_20200527_2137'),
        ('electronicbookcollections', '0002_auto_20200530_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronicbookcollection',
            name='digital_books',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='digital_books.Digital_Book'),
        ),
    ]
