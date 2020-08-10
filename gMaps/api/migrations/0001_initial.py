# Generated by Django 3.1 on 2020-08-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('street_number', models.CharField(max_length=20, null=True)),
                ('zip_code', models.CharField(max_length=100, null=True)),
                ('full_address', models.CharField(max_length=100)),
                ('lattitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
