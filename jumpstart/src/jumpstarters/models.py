from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


 #Create your models here.

class jumpstarter(models.Model):
	
	name = models.CharField( max_length = 60)
	lastName = models.CharField( max_length = 60)
	email = models.EmailField()
	description = models.TextField( max_length = 200, null = True, blank = True)
	profileImg = models.ImageField(upload_to = 'photos', default = 'pic_folder/None/no-img.jpg', null = True, blank = True)
	joinDate = models.DateTimeField( auto_now_add = True, auto_now = False )	

	def __unicode__(self):
		return self.name