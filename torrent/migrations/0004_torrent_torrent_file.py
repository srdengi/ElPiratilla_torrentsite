# Generated by Django 5.0.4 on 2024-04-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrent', '0003_alter_torrent_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='torrent',
            name='torrent_file',
            field=models.FileField(null=True, unique=True, upload_to='torrents'),
        ),
    ]
