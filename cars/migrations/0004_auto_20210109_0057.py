# Generated by Django 3.1.5 on 2021-01-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20210109_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='make',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='rate',
            name='model',
            field=models.CharField(max_length=64),
        ),
    ]
