# Generated by Django 4.0.4 on 2022-05-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_location_profile_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='priority',
            field=models.IntegerField(null=True),
        ),
    ]
