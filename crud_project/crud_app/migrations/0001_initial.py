# Generated by Django 4.1.7 on 2023-02-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('order_no', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('delivery_date', models.DateField()),
            ],
        ),
    ]
