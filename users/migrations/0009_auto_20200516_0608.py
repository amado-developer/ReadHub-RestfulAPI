# Generated by Django 3.0.6 on 2020-05-16 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200516_0606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='collection_id',
            new_name='id_coll',
        ),
    ]
