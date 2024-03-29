# Generated by Django 3.1.1 on 2020-10-18 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year_built', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('size', models.IntegerField()),
                ('market_rent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='units', to='properties.property')),
            ],
        ),
    ]
