# Generated by Django 3.1 on 2020-08-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200811_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='property_description',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='property_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
