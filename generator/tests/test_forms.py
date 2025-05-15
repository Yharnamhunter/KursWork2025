import pytest
from django.contrib.auth.models import User
from ..forms import RegisterForm, LoginForm
from django.contrib.auth.password_validation import validate_password

@pytest.mark.django_db
def test_register_form_password_mismatch():
    data = {
        'username': 'user1',
        'email': 'u@e.com',
        'password1': 'Abc12345!',
        'password2': 'Different1!'
    }
    form = RegisterForm(data)
    assert not form.is_valid()
    assert 'password2' in form.errors

def test_register_form_success(db):
    data = {
        'username': 'user2',
        'email': 'u2@e.com',
        'password1': 'StrongPass1!',
        'password2': 'StrongPass1!'
    }
    form = RegisterForm(data)
    assert form.is_valid()
    user = form.save()
    assert User.objects.filter(username='user2').exists()

def test_login_form_empty():
    form = LoginForm(data={})
    assert not form.is_valid()
    assert 'username' in form.errors
    assert 'password' in form.errors

@pytest.mark.django_db
def test_login_form_success():
    user = User.objects.create_user(username='foo', email='foo@example.com', password='bar')
    form = LoginForm(request=None, data={'username': 'foo', 'password': 'bar'})
    assert form.is_valid()