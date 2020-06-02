# Generated by Django 3.0.6 on 2020-05-14 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreBrach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('employee_quantity', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=50)),
                ('schedule', models.CharField(max_length=50)),
            ],
        ),
    ]