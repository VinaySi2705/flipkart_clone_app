# Generated by Django 3.2.8 on 2021-11-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0006_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
