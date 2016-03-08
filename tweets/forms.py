
from django import forms
from .models import Tweet
from user_profile.models import UserProfile


class TweetForm(forms.ModelForm):
	class Meta:
		model = Tweet
		fields = ['text','country']
		labels = {'text':'','country':''}
		widgets = {'text': forms.Textarea(attrs={'rows':1,'cols':85}),
		'country': forms.HiddenInput() }
