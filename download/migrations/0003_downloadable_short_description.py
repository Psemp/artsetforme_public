# Generated by Django 3.2.7 on 2021-09-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0002_alter_downloadable_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloadable',
            name='short_description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
