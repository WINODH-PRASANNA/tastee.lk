# Generated by Django 5.2.1 on 2025-06-08 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_remove_product_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
