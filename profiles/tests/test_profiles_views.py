import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_index():
    # Create users
    user1 = User.objects.create(username='user1')
    user2 = User.objects.create(username='user2')
    Profile.objects.create(user=user1, favorite_city='Paris')
    Profile.objects.create(user=user2, favorite_city='London')

    # Create a test client instance
    client = Client()

    # Make a GET request to the profile_index view
    url = reverse('profiles:index')
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.context) == 2


@pytest.mark.django_db
def test_profiles():
    # Create users
    user = User.objects.create(username='Emily')
    profile = Profile.objects.create(user=user, favorite_city='Paris')

    # Create a test client instance
    client = Client()

    # Make a GET request to the profile_index view
    url = reverse('profiles:profile', args=[user.username])
    response = client.get(url)

    assert response.status_code == 200
    assert response.context['profile'] == profile

