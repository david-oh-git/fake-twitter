from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# from django.utils.translation import ugettext_lazy as _


# Create your models here.
class CustomUserManager(BaseUserManager):

	def create_user(self, username, email, password, is_admin,is_shinigami, **extra_fields):
		''' creates and saves a new user '''
		now = timezone.now()
		if not email:
			raise ValueError('##Provide email in the proper format##')
		
		user = self.model(username=username,email=self.normalize_email(email),
			is_admin=is_admin,is_active=True,is_shinigami=is_shinigami,last_login=now
			, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email,password, **extra_fields):
		user = self.create_user(username,email,password, True,True,
			**extra_fields)
		user.is_admin = True
		user.is_shinigami = True
		user.save(using=self._db)
		return user


class UserProfile(AbstractBaseUser):
	''' should be for custom user class  & attributes associated with'''
	username = models.CharField('username',max_length=20,
		unique=True, db_index=True)
	email = models.EmailField('email address',unique=True,)
	joined = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField('active',default=True)
	is_admin = models.BooleanField(default=False)
	is_shinigami = models.BooleanField(default=False)

	objects = CustomUserManager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email',]

	class Meta:
		verbose_name = 'user'
		verbose_name_plural = 'users'

	def get_full_name(self):
		# The user is identified by username not email 
		return self.username

	def get_short_name(self):
		# The user is identified by username not email 
		return self.username

	def __unicode__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		# does user have a specific permission 
		return True

	def has_module_perms(self, tweets):
		# if user has permission to view tweets app 
		return True

	def is_staff(self):
		# if user is staff 
		return self.is_admin


	# def __str__(self):
	# 	return self.username




		