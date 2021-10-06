# Generated by Django 3.2.7 on 2021-09-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Downloadable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_uploaded', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]