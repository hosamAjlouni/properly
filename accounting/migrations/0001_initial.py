# Generated by Django 3.1.1 on 2020-11-23 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leases', '0008_auto_20201123_2315'),
        ('contacts', '0008_auto_20201123_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('due_date', models.DateField()),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='contacts.contact')),
                ('lease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lease', to='leases.lease')),
            ],
        ),
    ]
