# Generated by Django 4.1 on 2024-07-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_usertoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertoken',
            name='invalid_tried_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
