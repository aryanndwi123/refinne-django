# Generated by Django 4.1.4 on 2023-02-19 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupons',
            name='active',
        ),
        migrations.RemoveField(
            model_name='coupons',
            name='timeStamp',
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
        migrations.AlterField(
            model_name='coupons',
            name='slug',
            field=models.CharField(max_length=130, unique=True),
        ),
    ]