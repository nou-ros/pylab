# Generated by Django 3.1 on 2021-06-07 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
            preserve_default=False,
        ),
    ]
