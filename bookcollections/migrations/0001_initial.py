# Generated by Django 3.0.6 on 2020-05-14 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adquisitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adquisitions.Collection')),
            ],
        ),
    ]
