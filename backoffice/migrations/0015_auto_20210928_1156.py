# Generated by Django 3.2.7 on 2021-09-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0014_auto_20210928_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='attachment_1',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='attachment_2',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='image_body_1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='image_body_2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
