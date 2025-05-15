import pytest
from django.contrib.auth.models import User
from ..models import TextGeneration, BatchGeneration

@pytest.mark.django_db
def test_text_generation_model():
    user = User.objects.create_user('alice', 'a@b.com', 'pass')
    tg = TextGeneration.objects.create(
        user=user, prompt='hello', result='world', language='ru'
    )
    assert tg.pk is not None
    assert tg.created_at is not None
    assert tg.prompt == 'hello'
    assert tg.result == 'world'
    assert tg.language == 'ru'

@pytest.mark.django_db
def test_batch_generation_model():
    user = User.objects.create_user('bob', 'b@c.com', 'pass')
    bg = BatchGeneration.objects.create(
        user=user, prompt='test', count=3, language='en', file_format='txt'
    )
    assert bg.pk is not None
    assert bg.count == 3
    assert bg.file_format == 'txt'
