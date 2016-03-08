
from django import forms
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import UserProfile

class UserProfileCreationForm(forms.ModelForm):
	''' a form that creates a new user '''
	password1 = forms.CharField(label="password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="password confirmation", 
		widget=forms.PasswordInput)

	class Meta:
		model = UserProfile
		fields = ["username","email"]

	def clean_password2(self):
		# confirm that both passwords match 
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("passwords dont match")

		return password2

	def save(self, commit=True):
		# save the provided password 
		user = super(UserProfileCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class UserProfileChangeForm(forms.ModelForm):
	''' for updating user details '''
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = UserProfile
		fields = ["username","email","is_active","is_admin","is_shinigami"]

	def clean_password(self):
		# provides initial value of password
		return self.initial["password"]


			
		