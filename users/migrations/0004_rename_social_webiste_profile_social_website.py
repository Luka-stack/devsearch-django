# Generated by Django 4.0.4 on 2022-05-27 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_webiste',
            new_name='social_website',
        ),
    ]
