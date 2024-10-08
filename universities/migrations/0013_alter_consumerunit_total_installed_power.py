# Generated by Django 4.1 on 2024-08-28 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0012_alter_consumerunit_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumerunit',
            name='total_installed_power',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Potência total de geração de energia instalada em kw', max_digits=7, null=True),
        ),
    ]
