# Generated by Django 3.0.8 on 2021-12-11 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0009_auto_20210423_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('no_hp', models.CharField(max_length=50)),
            ],
        ),
    ]
