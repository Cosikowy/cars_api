# Generated by Django 3.1.5 on 2021-01-09 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_auto_20210109_0210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ('-rate_count',)},
        ),
    ]