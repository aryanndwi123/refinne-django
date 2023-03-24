# Generated by Django 2.2.7 on 2022-12-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0004_auto_20221223_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupons',
            name='validfrom',
        ),
        migrations.RemoveField(
            model_name='coupons',
            name='validto',
        ),
        migrations.AddField(
            model_name='coupons',
            name='img_loc',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coupons',
            name='code',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='coupons',
            name='conditions',
            field=models.TextField(default=0),
        ),
    ]
