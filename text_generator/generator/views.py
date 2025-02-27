import requests
from django.shortcuts import render
from .forms import TextGenerationForm
from django.conf import settings



def home(request):
    generated_text = None

    if request.method == 'POST':
        form = TextGenerationForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            language = form.cleaned_data['language']
            generated_text = generate_text_on_topic(topic, language)
            
    else:
        form = TextGenerationForm()

    return render(request, 'generator/home.html', {'form': form, 'generated_text': generated_text})
'''
def generate_text_with_gemini(theme, language):
    API_KEY = settings.GEMINI_API_KEY
    MODEL = 'gemini-1.5-flash-001'
    URL = f'https://generativelanguage.googleapis.com/v1/models/{MODEL}:generateContent'
    headers = {
        'Content-Type': 'application/json',
        'x-goog-api-key': API_KEY
    }

    data = {
        'contents': [{'parts':[{'text': f'Write a small text for 100-120 words in {language} about {theme}'}]}]
    }

    response = requests.post(URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        return f'Error: {response.status_code}. {response.text}'
'''

def generate_text_on_topic(topic, language='ru'):
    gpt_id = settings.YANDEX_GPT_ID
    token = settings.YANDEX_API_KEY
    
    prompt = {
        "modelUri": f"gpt://{gpt_id}/yandexgpt-lite/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0.5,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": f"Ты ассистент, способный помочь с темами на языке {language}."
            },
            {
                "role": "user",
                "text": f"Привет! Мне нужно узнать больше о {topic}. Напиши мне об этой теме текст на 100-120 слов."
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {token}"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()

    return result['result']['alternatives'][0]['message']['text']