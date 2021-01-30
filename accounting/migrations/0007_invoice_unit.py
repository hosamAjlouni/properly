# Generated by Django 3.1.1 on 2020-12-01 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0012_auto_20201123_2315'),
        ('accounting', '0006_auto_20201201_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='properties.unit'),
        ),
    ]
