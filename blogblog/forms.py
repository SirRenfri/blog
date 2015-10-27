from django import forms
from .models import Message

#Старая форма
class New_messageForm(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок')
    message = forms.CharField(widget=forms.Textarea, label='Текст:')