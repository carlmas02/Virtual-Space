# Generated by Django 3.2.14 on 2022-07-31 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_profile_type_profile_moderator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
