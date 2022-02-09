from django.contrib import admin

# Register your models here.
from .models import Tweet


class TweetAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user'] #__str__ method is defaulting to Tweet model
    search_fields = ['content', 'user__username']
    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetAdmin) #adding searchfield to /admin/tweets search by user