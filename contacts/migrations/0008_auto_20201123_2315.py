# Generated by Django 3.1.1 on 2020-11-23 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20201023_2206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['first']},
        ),
    ]
