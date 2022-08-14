from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.ForeignKey(User,on_delete= models.CASCADE)
	id_user = models.IntegerField()
	moderator = models.BooleanField()

	def __str__(self):
		return self.user.username



class Room(models.Model):
	user = models.ForeignKey(User,on_delete= models.CASCADE,default="")
		 = models.TextField()
	token = models.TextField()
	uid = models.IntegerField()

	def __str__(self):
		return self.name

class Room_User(models.Model):
	room = models.ForeignKey(Room,on_delete= models.CASCADE,default="")
	room_user = models.ForeignKey(User,on_delete= models.CASCADE,default="")

	def __str__(self):
		return str(self.room)
