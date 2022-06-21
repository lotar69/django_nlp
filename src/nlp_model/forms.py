from django import forms
from nlp_model.models import Tweet


class Tweet(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            "tweet"
        ]
        labels = {"tweet": "Tweet"}