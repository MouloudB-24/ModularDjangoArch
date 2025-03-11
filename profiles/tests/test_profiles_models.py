import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_creation():
    """Test profile creation and verify attributes"""

    user = User.objects.create(username='Victor')

    profile = Profile.objects.create(user=user, favorite_city='Paris')

    assert profile.user.username == 'Victor'
    assert profile.favorite_city == 'Paris'


@pytest.mark.django_db
def test_profile_str():
    """Test __str__ method of the profile model"""

    user = User.objects.create(username='Emily')

    profile = Profile.objects.create(user=user, favorite_city='New York')

    assert str(profile) == 'Emily'
