import pytest
from django.test import Client
from django.urls import reverse

from lettings.models import Letting, Address


@pytest.mark.django_db
def test_lettings_index():
    """Test the lettings_index view."""

    address = Address.objects.create(
        number=101, street="Street", city="London", state="XX",
        zip_code=12345, country_iso_code="England"
    )
    Letting.objects.create(title="Apartment", address=address)

    # Create a test client instance
    client = Client()

    # Make a GET request to the lettings index view
    url = reverse('lettings:index')
    response = client.get(url)

    # Checks
    assert response.status_code == 200
    assert "Apartment" in response.content.decode()


@pytest.mark.django_db
def test_letting_view():
    """Test the letting view."""
    # Create sample data
    address = Address.objects.create(
        number=202, street="Avenue", city="New York", state="NY",
        zip_code=10000, country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Apartment", address=address)


    # Create a test client instance
    client = Client()

    # Make a GET request to the letting detail view
    url = reverse('lettings:letting', args=[letting.id])
    response = client.get(url)

    # Checks
    assert response.status_code == 200
    assert "Apartment" in response.content.decode()
    assert "202 Avenue" in response.content.decode()