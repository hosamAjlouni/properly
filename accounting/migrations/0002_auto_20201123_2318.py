# Generated by Django 3.1.1 on 2020-11-23 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leases', '0008_auto_20201123_2315'),
        ('contacts', '0008_auto_20201123_2315'),
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transaction',
            new_name='Invoice',
        ),
    ]
