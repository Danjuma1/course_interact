from django.db import models
from django.contrib.auth.models import User

from accounts.models import Course

class Message(models.Model):
    content = models.CharField(max_length=500)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender + " : " + self.sent_on


class Notification(models.Model):
    content = models.CharField(max_length=500)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    sent_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sent_on
