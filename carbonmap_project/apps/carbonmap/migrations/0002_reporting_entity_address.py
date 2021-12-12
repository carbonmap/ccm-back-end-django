# Generated by Django 3.2.7 on 2021-12-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbonmap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporting_entity_address',
            fields=[
                ('id', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('street_address', models.CharField(max_length=60)),
                ('address_locality', models.CharField(max_length=60)),
                ('address_region', models.CharField(max_length=60)),
                ('postal_code', models.CharField(max_length=60)),
                ('address_country', models.CharField(max_length=60)),
            ],
        ),
    ]
