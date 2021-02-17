# Generated by Django 3.1.5 on 2021-02-17 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('avg_rate', models.FloatField(default=0, null=True)),
                ('rate_count', models.IntegerField(default=0, null=True)),
            ],
            options={
                'ordering': ('-rate_count',),
                'unique_together': {('make', 'model')},
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=64)),
                ('make', models.CharField(max_length=64)),
                ('rate', models.IntegerField(null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
    ]
