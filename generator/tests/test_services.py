import pytest
from requests.exceptions import HTTPError
from unittest.mock import patch
from ..yandex_services import generate_text

@patch('generator.yandex_services.requests.post')
def test_generate_text_success(mock_post, monkeypatch):
    monkeypatch.setenv('YANDEX_GPT_ID', 'fake_id')
    monkeypatch.setenv('YANDEX_API_KEY','fake_key')
    mock_post.return_value.json.return_value = {
        'result': {'alternatives': [{'message': {'text':'hello world'}}]}
    }
    mock_post.return_value.raise_for_status.return_value = None

    text = generate_text('topic','ru', retries=1, backoff=0)
    assert text == 'hello world'

@patch('generator.yandex_services.requests.post')
def test_generate_text_http_error(mock_post, monkeypatch):
    monkeypatch.setenv('YANDEX_GPT_ID','fake')
    monkeypatch.setenv('YANDEX_API_KEY','fake')
    mock_post.side_effect = HTTPError("fail")
    text = generate_text('topic','ru', retries=1, backoff=0)
    assert text == ""
