# Generated by Django 4.2.1 on 2023-05-19 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=13),
        ),
    ]