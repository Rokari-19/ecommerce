# Generated by Django 4.2.7 on 2024-03-01 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
