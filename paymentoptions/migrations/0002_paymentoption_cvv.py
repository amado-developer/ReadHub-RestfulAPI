# Generated by Django 3.0.6 on 2020-06-03 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentoptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentoption',
            name='cvv',
            field=models.CharField(default=0, max_length=50),
        ),
    ]