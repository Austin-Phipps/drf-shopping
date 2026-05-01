import pytest
from shopping_list.models import User
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.fixture(autouse=True)
def disable_throttling(settings):
    settings.REST_FRAMEWORK = {
        **settings.REST_FRAMEWORK,
        'DEFAULT_THROTTLE_CLASSES': [],
    }

from shopping_list.models import ShoppingItem, ShoppingList

@pytest.fixture
def create_user():
    def _create_user(username='testuser'):
        return User.objects.create_user(username, f'{username}@example.com', 'password')

    return _create_user

@pytest.fixture
def create_authenticated_client():
    def _create_authenticated_client(user):
        client = APIClient()
        client.force_authenticate(user=user)
        return client

    return _create_authenticated_client

@pytest.fixture
def create_shopping_list():
    def _create_shopping_list(user, name='Test Shopping List'):
        shopping_list = ShoppingList.objects.create(name=name)
        shopping_list.members.add(user)
        return shopping_list

    return _create_shopping_list

@pytest.fixture
def create_shopping_item():
    def _create_shopping_item(name, user):
        shopping_list = ShoppingList.objects.create(name='My shopping list')
        shopping_list.members.add(user)
        shopping_item = ShoppingItem.objects.create(name=name, purchased=False, shopping_list=shopping_list)
        return shopping_item

    return _create_shopping_item