from distutils.command.upload import upload
import random
from django.db import models


class Tweet(models.Model):
    # id = models.AutoField(primary_key=True)
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
