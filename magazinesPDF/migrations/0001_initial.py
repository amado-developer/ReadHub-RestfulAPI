# Generated by Django 3.0.6 on 2020-06-02 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('magazines', '0003_auto_20200531_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='MagazinesPDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='')),
                ('magazine', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='magazines.Magazine')),
            ],
        ),
    ]