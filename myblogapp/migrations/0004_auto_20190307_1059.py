# Generated by Django 2.1.7 on 2019-03-07 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0003_auto_20190307_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.TextField(null=True),
        ),
    ]
