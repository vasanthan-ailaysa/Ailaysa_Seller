# Generated by Django 5.0.6 on 2024-06-27 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller_auth', '0002_alter_user_publisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='publisher',
        ),
    ]
