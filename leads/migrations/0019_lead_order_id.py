# Generated by Django 5.1.1 on 2024-10-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0018_alter_lead_deposit_alter_lead_total_tariff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='order_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
