# Generated by Django 3.2.14 on 2022-07-31 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_profile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('token', models.TextField()),
                ('uid', models.IntegerField()),
            ],
        ),
    ]
