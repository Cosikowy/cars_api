# Generated by Django 3.1.5 on 2021-01-09 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20210109_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='avg_rate',
            field=models.FloatField(default=0),
        ),
    ]