# Generated by Django 3.1 on 2021-10-27 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20211024_1351'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuynowItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('variations', models.ManyToManyField(blank=True, to='store.Variation')),
            ],
        ),
    ]
