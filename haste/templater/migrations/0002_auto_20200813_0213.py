# Generated by Django 3.0.7 on 2020-08-13 02:13

from django.db import migrations
from templater.resources.migration_utils import add_equipment_templates


class Migration(migrations.Migration):

    dependencies = [
        ('templater', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_equipment_templates)
    ]
