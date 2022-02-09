from django import forms
from .models import Tweet
from tweet_clone.settings import MAX_TWEET_lENGTH



class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_lENGTH:
            raise forms.ValidationError("Tweet is too long!")
        return content
