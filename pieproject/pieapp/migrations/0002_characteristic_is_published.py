# Generated by Django 4.1.7 on 2023-03-29 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteristic',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Published'),
        ),
    ]
