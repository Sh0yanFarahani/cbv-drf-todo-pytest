from rest_framework.test import APIClient
from django.urls import reverse
import pytest 
from django.contrib.auth.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client
@pytest.fixture
def common_user():
    user = User.objects.create(username='shayan232sh3', password='sh123@3426', is_active=True, is_staff=True)
    return user

@pytest.mark.django_db
class TestTaskApi:
    def test_get_task_response_403_status(self, api_client):
        url = reverse('task:todo-api:todo-list')
        response = api_client.get(url)
        assert response.status_code == 403

    def test_get_task_response_200_status(self, common_user, api_client):
        url = reverse('task:todo-api:todo-list')
        user = common_user
        api_client.force_login(user=user)
        response = api_client.get(url)
        assert response.status_code == 200    

    def test_create_task_response_201_status(self, api_client, common_user):
        url = reverse('task:todo-api:todo-list')
        data = {
            'name':'test',
            'done':False,
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    
    def test_create_task_response_400_status(self, api_client, common_user):
        url = reverse('task:todo-api:todo-list')
        data = {
            'done':False,
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400
