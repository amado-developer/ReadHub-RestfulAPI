# Generated by Django 3.0.6 on 2020-05-14 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
