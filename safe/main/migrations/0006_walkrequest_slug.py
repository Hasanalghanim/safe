# Generated by Django 3.1.7 on 2021-04-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210326_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='walkrequest',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
