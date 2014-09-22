from django.db import models
from django.utils.encoding import unicode


 #Create your models here.

class jumpstarter(models.Model):
	
	name = models.CharField( max_length = 60)
	lastName = models.CharField( max_length = 60)
	email = models.EmailField()
	description = models.CharField( max_length = 200, null = True, blank = True)
	profileImg = models.ImageField(upload_to = 'photos', null = True, blank = True)
	joinDate = models.DateTimeField( auto_now_add = True, auto_now = False )	

	def __unicode__(self):
		return self.name