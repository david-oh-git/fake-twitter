from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
# def index(request):
# 	if request.method == 'GET':
# 		return HttpResponse('I am called from a get Request')
# 	elif request.method == 'POST':
# 		return HttpResponse('I am called from a post Request')



class Index(View):
	def get(self, request):
		context = {'name' : 'Django'}
		return render(request,'tweets/base.html',context)

	def post(self, request):
		return HttpResponse('a post request i am')