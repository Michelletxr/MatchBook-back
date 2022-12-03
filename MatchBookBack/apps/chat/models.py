from django.contrib.auth import get_user_model
from django.db import models

from MatchBookBack.abstracts.base_models import BaseModel

User = get_user_model()

class Room(BaseModel):
    users = models.ManyToManyField(User, related_name='rooms')

    class Meta():
        app_label = 'chat'

class Message(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()

    class Meta():
        app_label = 'chat'
