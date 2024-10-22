# Generated by Django 5.1.1 on 2024-10-03 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0015_remove_lead_age_remove_lead_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='vehicle_deposit',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='vehicle_tariff',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
