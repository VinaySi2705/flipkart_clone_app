# Generated by Django 3.2.9 on 2021-11-03 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0004_auto_20211103_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cutomer',
            new_name='customer',
        ),
    ]