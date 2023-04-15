# Generated by Django 3.0.8 on 2021-03-16 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0002_buku_jumlah'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kelompok',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=9)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='buku',
            name='kelompok_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.Kelompok'),
        ),
    ]
