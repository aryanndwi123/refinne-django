# Generated by Django 4.1.4 on 2023-07-01 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0010_coupons_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupons',
            name='image',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
