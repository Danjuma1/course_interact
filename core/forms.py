from django import forms

from .models import Notification, Message

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['content']

class NotificationForm(forms.ModelForm):

    class Meta:
        model = Notification
        fields = ['content']