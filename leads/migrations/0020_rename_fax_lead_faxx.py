# Generated by Django 5.1.1 on 2024-10-03 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0019_lead_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='fax',
            new_name='faxx',
        ),
    ]