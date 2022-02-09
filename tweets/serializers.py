from rest_framework import serializers
from .models import Tweet

from tweet_clone.settings import MAX_TWEET_lENGTH


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content']

    def validate_content(self, value):
        if len(value) > MAX_TWEET_lENGTH:
            raise serializers.ValidationError("Tweet is too long!")
        return value 