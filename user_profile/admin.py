from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
# Register your models here.
from user_profile.models import UserProfile
from .forms import UserProfileChangeForm, UserProfileCreationForm

class UserProfileAdmin(BaseUserAdmin):
	form = UserProfileChangeForm
	add_form = UserProfileCreationForm

	list_display = ['username','email','is_admin','is_shinigami']
	list_filter = ['is_admin','is_shinigami']

	fieldsets = ((None,{'fields':('username','email','password')}),
	  ('Permissions',{'fields':('is_active','is_admin','is_shinigami',
	'is_superuser')}),
	   ('Important_dates',{'fields':('last_login','joined')}), )

	add_fieldsets = (
		(None,{'classes':('wide',),
			'fields':('username','email',
	'password1','password2')} ),  )

	
	
	search_fields = ('username','email',)
	ordering = ('username',)
	filter_horizontal = ()

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.unregister(Group)