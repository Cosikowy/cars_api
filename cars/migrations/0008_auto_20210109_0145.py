# Generated by Django 3.1.5 on 2021-01-09 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_auto_20210109_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='rate',
            field=models.IntegerField(null=True),
        ),
    ]
