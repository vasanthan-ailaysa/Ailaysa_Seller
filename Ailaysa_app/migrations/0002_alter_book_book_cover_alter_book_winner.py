# Generated by Django 5.0.6 on 2024-06-27 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ailaysa_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='winner',
            field=models.TextField(blank=True, null=True),
        ),
    ]
