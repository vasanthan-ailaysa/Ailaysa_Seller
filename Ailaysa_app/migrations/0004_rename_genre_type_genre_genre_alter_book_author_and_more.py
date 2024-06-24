# Generated by Django 5.0.6 on 2024-06-24 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ailaysa_app', '0003_author_publisher_remove_book_format_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre_type',
            new_name='genre',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='book', to='Ailaysa_app.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='book', to='Ailaysa_app.publisher'),
        ),
    ]