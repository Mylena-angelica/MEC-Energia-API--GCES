# Generated by Django 4.1 on 2023-10-19 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0010_energybill_energy_bill_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='energybill',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]