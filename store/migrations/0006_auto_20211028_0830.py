# Generated by Django 3.1 on 2021-10-28 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20211027_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='actual_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='offer',
            field=models.IntegerField(null=True),
        ),
    ]
