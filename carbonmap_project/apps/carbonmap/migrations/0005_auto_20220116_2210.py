# Generated by Django 3.2.7 on 2022-01-16 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carbonmap', '0004_auto_20220114_1423'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reporting_entity',
            new_name='ReportingEntity',
        ),
        migrations.RenameModel(
            old_name='Reporting_entity_address',
            new_name='ReportingEntityAddress',
        ),
    ]
