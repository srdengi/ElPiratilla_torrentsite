# Generated by Django 5.0.4 on 2024-04-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrent', '0002_remove_torrent_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torrent',
            name='language',
            field=models.CharField(choices=[('FR', 'FRENCH'), ('CS', 'CASTELLANO'), ('EN', 'ENGLISH')], max_length=2),
        ),
    ]
