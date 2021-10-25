from django.contrib import admin
from .models import Course, Message, Notification

admin.site.register(Course)
admin.site.register(Message)
admin.site.register(Notification)