# Generated by Django 3.0.6 on 2020-05-31 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazine',
            name='quantity',
        ),
    ]
