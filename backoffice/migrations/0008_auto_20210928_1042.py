# Generated by Django 3.2.7 on 2021-09-28 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0007_auto_20210928_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='global_title',
            field=models.CharField(default='Newsletter - Atelier Arts & Forme', max_length=255),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='subject_1',
            field=models.CharField(default='Titre section 1', max_length=255),
        ),
    ]