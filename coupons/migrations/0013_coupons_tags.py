# Generated by Django 4.1.4 on 2023-07-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0012_alter_coupons_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupons',
            name='tags',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
