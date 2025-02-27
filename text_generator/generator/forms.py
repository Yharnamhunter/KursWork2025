from django import forms

class TextGenerationForm(forms.Form):
    topic = forms.CharField(max_length=120, label='Тема')
    language = forms.ChoiceField(choices=[('ru', 'Русский'), ('en', 'Английский')], label='Язык')
