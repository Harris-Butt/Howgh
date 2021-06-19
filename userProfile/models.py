from django.db import models
from account.models import Account
# Create your models here.

class Profile(models.Model):
	user  = models.OneToOneField(Account,on_delete=models.CASCADE,related_name="profile")
	user_profile_name = models.CharField(max_length=50)
	user_image = models.FileField(null=True,upload_to='user_profile_images/')
	user_profession =  models.CharField(max_length=255)
	user_phone_number = models.CharField(max_length=55)
	user_address = models.TextField()
