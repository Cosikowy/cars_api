# Generated by Django 3.1.5 on 2021-01-08 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='make',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='rate',
            name='model',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
