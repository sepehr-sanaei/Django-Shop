# Generated by Django 4.2.18 on 2025-02-12 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile/default.jpg', upload_to='profile/'),
        ),
    ]
