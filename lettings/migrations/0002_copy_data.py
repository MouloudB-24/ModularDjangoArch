# Generated by Django 3.0 on 2025-01-28 14:39

from django.db import migrations


def copy_data_to_new_tables(apps, schema_editor):
    # Load olds modals
    old_address = apps.get_model('oc_lettings_site', 'Address')
    old_letting = apps.get_model('oc_lettings_site', 'Letting')

    # Load news modals
    Address = apps.get_model('lettings', 'Address')
    Letting = apps.get_model('lettings', 'Letting')

    # Copy data for Address
    for old_address in old_address.objects.all():
        Address.objects.create(
            id=old_address.id,
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
        )

    # Copy data for Letting
    for old_letting in old_letting.objects.all():
        Letting.objects.create(
            id=old_letting.id,
            title=old_letting.title,
            address_id=old_letting.address_id
        )

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_data_to_new_tables),
    ]