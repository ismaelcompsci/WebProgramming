from django.db import models

# Create your models here.
# class TwtichUser(models.Model):
#     twtich_user = models.CharField(max_length=64)
#     chats = models.ManyToManyField("Chat")

# class Chat(models.Model):
#     channel = models.CharField(max_length=64),
#     displayName = models.CharField(max_length=64),
#     raw = models.CharField(),
#     text = models.CharField(max_length=500),
#     timestamp = models.DateTimeField(),
#     username = models.CharField(max_length=64)

#     def serialize(self):
#         return {
#             "id": self.id,
#             "channel" : self.channel,
#             "displayName": self.displayName,
#             "raw": self.raw,
#             "text": self.text,
#             "timestamp": self.timestamp,
#             "username": self.username
#         }

