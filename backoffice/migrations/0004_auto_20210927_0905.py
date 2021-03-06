# Generated by Django 3.2.7 on 2021-09-27 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0003_newletter_attachement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newletter',
            old_name='attachement',
            new_name='attachement_1',
        ),
        migrations.RenameField(
            model_name='newletter',
            old_name='body',
            new_name='body_1',
        ),
        migrations.RenameField(
            model_name='newletter',
            old_name='subject',
            new_name='subject_1',
        ),
        migrations.AddField(
            model_name='newletter',
            name='attachement_2',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='newletter',
            name='body_2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='newletter',
            name='image_body1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='newletter',
            name='image_body2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='newletter',
            name='subject_2',
            field=models.CharField(blank=True, default='Newsletter - Atelier Arts & Forme', max_length=255),
        ),
    ]
