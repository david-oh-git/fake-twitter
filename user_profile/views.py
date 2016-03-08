
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from tweets.models import Tweet
from user_profile.models import UserProfile
from django.contrib.auth import logout, authenticate, login

from django.core.urlresolvers import reverse
from .forms import UserProfileCreationForm
# from tweets.views import PostTweet


# from django.contrib.auth import logout, login, authenticate
# from user_profile.forms import UserProfileCreationForm
# Create your views here.


class LogoutView(View):
	# for logging out using default logout

	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse('tweets:index'))



class RegisterView(View):
	# to register a new user 
	context = {}
	def get(self, request):
		# blank registration form 
		form = UserProfileCreationForm()
		context = {'form':form }
		return render(request, 'user_profile/register.html', context)

	def post(self, request):
		form = UserProfileCreationForm(data=self.request.POST)

		if form.is_valid():
			new_user = form.save()
			# log in user send to home page 
			auth_user = authenticate(username=new_user.username,password=self.request.POST['password1'])
			login(self.request, auth_user)
			return HttpResponseRedirect(reverse('tweets:index'))
		context = {'form':form }
		return render(request, 'user_profile/register.html', context)




