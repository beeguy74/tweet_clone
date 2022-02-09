from distutils.command.upload import upload
import random
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL #builtin django user model is great!


class Tweet(models.Model):
    # maps to sql
    # id = models.AutoField(primary_key=True)
    # many users can have many tweets
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #keeps tweets
    user = models.ForeignKey(User, on_delete=models.CASCADE) # delete all twets if user was deleted
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    # changing meta option gives us a descending order tweets on page
    # but dont forget makemigrations
    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }


# Create your models here.
