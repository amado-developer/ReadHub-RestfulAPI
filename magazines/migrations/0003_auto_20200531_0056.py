# Generated by Django 3.0.6 on 2020-05-31 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0002_remove_magazine_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='cover',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='magazine',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]