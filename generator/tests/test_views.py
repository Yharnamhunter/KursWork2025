import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_register_and_login_view(client):
    url = reverse('register')
    resp = client.post(url, {
        'username':'testu',
        'email':'t@u.com',
        'password1':'Strong1!',
        'password2':'Strong1!'
    })
    assert resp.status_code == 302 
    assert User.objects.filter(username='testu').exists()

    url = reverse('login')
    resp = client.post(url, {'username':'testu','password':'Strong1!'})
    assert resp.status_code in (302, 200)


@pytest.mark.django_db
def test_batch_download_view(client, settings, tmp_path):
    batch_dir = tmp_path / 'batch'
    batch_dir.mkdir()
    f = batch_dir / 'file.txt'
    f.write_text('hello')
    settings.MEDIA_ROOT = str(tmp_path)

    user = User.objects.create_user('u','u@e.com','p')
    client.force_login(user)
    url = reverse('batch_download', args=['file.txt'])
    resp = client.get(url)
    assert resp.status_code == 200
    assert resp['Content-Type'].startswith('text/plain')
    content = b''.join(resp.streaming_content)
    assert content == b'hello'
