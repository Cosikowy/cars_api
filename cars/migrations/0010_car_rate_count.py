# Generated by Django 3.1.5 on 2021-01-09 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_auto_20210109_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='rate_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
