# Generated by Django 3.2.7 on 2021-09-25 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0002_newletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='newletter',
            name='attachement',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
