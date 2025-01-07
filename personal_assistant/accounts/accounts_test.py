import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test import Client


@pytest.fixture
def user():
    return get_user_model().objects.create_user(username="testuser", password="password123")


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_signupuser(client):
    url = reverse('accounts:signup')

    response = client.get(url)
    assert response.status_code == 200
    assert 'form' in response.context

    data = {'username': 'newuser', 'password1': 'newpassword', 'email': 'testuser@example.com',
            'password2': 'newpassword'}
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse('news:index')

    data = {'username': 'newuser', 'password1': 'newpassword', 'password2': 'wrongpassword'}
    response = client.post(url, data)
    assert response.status_code == 200
    assert 'form' in response.context
    assert 'password' in response.context['form'].errors


@pytest.mark.django_db
def test_loginuser(client, user):
    url = reverse('accounts:login')

    response = client.get(url)
    assert response.status_code == 200
    assert 'form' in response.context

    data = {'username': user.username, 'password': 'password123'}
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse('news:index')

    data = {'username': user.username, 'password': 'wrongpassword'}
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse('accounts:login')

    response = client.get(reverse('accounts:login'))
    messages = list(get_messages(response.wsgi_request))
    assert len(messages) == 1
    assert str(messages[0]) == "Username or password didn't match"


@pytest.mark.django_db
def test_logoutuser(client, user):
    client.login(username='testuser', password='password123')
    url = reverse('accounts:logout')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == reverse('news:index')


@pytest.mark.django_db
def test_reset_password(client):
    url = reverse('accounts:reset-password')

    response = client.get(url)
    assert response.status_code == 200
    assert 'form' in response.context

    data = {'email': 'testuser@example.com'}
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse('accounts:password_reset_done')
