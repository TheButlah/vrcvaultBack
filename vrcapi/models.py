from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User


class vrcUser(models.Model):

	id = models.CharField(max_length=300,primary_key=True)
	username = models.CharField(max_length=300)
	displayName = models.CharField(max_length=300)
	bio = models.CharField(max_length=3000)
	has_avatars = models.CharField(max_length=5, default='?')
	fallbackAvatar = models.CharField(max_length=300, default='')
	currentAvatarImageUrl = models.CharField(max_length=300, default='')
	currentAvatarThumbnailImageUrl= models.CharField(max_length=300, default='')
	last_platform= models.CharField(max_length=300, default='')
	userIcon= models.CharField(max_length=300, default='')
	tags= models.CharField(max_length=300, default='')
	isFriend= models.CharField(max_length=300, default='')
	def __str__(self):
		return self.id

class Avatar(models.Model):

	id = models.CharField(max_length=100,primary_key=True)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=6001,default=' ')
	authorId = models.CharField(max_length=600,default=' ')
	authorName = models.CharField(max_length=300,default=' ')
	assetUrl = models.CharField(max_length=300,default=' ')
	imageUrl = models.CharField(max_length=300,default=' ')
	thumbnailImageUrl = models.CharField(max_length=300,default=' ')
	created_at = models.CharField(max_length=300,default=' ')
	updated_at = models.CharField(max_length=300,default=' ')
	releaseStatus = models.CharField(max_length=300,default=' ')
	user_checked = models.BooleanField(default=False)
	
	def __str__(self):
		return self.id

