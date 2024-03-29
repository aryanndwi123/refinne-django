# Generated by Django 2.2.7 on 2022-12-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('offer', models.IntegerField(default=10)),
                ('code', models.TextField()),
                ('conditions', models.TextField(default=0, max_length=6, unique=True)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=130)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
