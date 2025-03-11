import pytest

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_creation():
    """Test address creation and verify attributes"""

    address = Address.objects.create(
        number=100,
        street='Street hatfield',
        city='HATFIELD', state='PS',
        zip_code=1001,
        country_iso_code='USA')

    # Checks
    assert address.number == 100
    assert address.street == 'Street hatfield'
    assert address.city == 'HATFIELD'
    assert address.zip_code == 1001
    assert address.country_iso_code == 'USA'


@pytest.mark.django_db
def test_address_str():
    """Test __str__ method of the Address model"""

    address = Address.objects.create(
        number=100,
        street='Street hatfield',
        city='HATFIELD', state='PS',
        zip_code=1001,
        country_iso_code='USA')

    assert str(address) == '100 Street hatfield'


@pytest.mark.django_db
def test_letting_creation():
    """Test letting creation and verify attributes"""
    address = Address.objects.create(
        number=100,
        street='Street hatfield',
        city='HATFIELD', state='PS',
        zip_code=1001,
        country_iso_code='USA')

    letting = Letting.objects.create(title='LettingTest', address=address)

    # Checks
    assert letting.title == 'LettingTest'
    assert letting.address == address


@pytest.mark.django_db
def test_letting_str():
    """Test __str__ method of the Letting model"""
    address = Address.objects.create(
        number=100,
        street='Street hatfield',
        city='HATFIELD', state='PS',
        zip_code=1001,
        country_iso_code='USA')

    letting = Letting.objects.create(title='LettingTest', address=address)

    # Checks
    assert str(letting) == 'LettingTest'
