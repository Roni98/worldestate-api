# Generated by Django 3.1 on 2020-08-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200811_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='full_address',
            field=models.CharField(max_length=250),
        ),
    ]