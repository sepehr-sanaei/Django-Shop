# Generated by Django 4.2.16 on 2024-12-03 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productmodel',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='productmodel',
            name='brief_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]