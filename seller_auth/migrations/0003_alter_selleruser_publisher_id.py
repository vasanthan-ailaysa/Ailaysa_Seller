# Generated by Django 5.0.6 on 2024-06-24 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ailaysa_app', '0004_rename_genre_type_genre_genre_alter_book_author_and_more'),
        ('seller_auth', '0002_selleruser_publisher_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selleruser',
            name='publisher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffs', related_query_name='staff', to='Ailaysa_app.publisher'),
        ),
    ]