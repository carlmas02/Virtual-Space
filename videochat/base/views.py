from django.shortcuts import render
from django.http import JsonResponse
from django.http import request,HttpResponse
from agora_token_builder import RtcTokenBuilder
import random
import time
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from .models import *

def getToken(request):
	appId = '5f7dc3acd0244a25b98292f65d5d2063'
	appCertificate = 'c3795ffcc76844ffb37af64fb97715f3'
	channelName = request.GET.get('channel')
	uid = random.randint(1,230)
	privilegeExpiredTs =  time.time() + 3600*24
	role = 1
	token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

	return JsonResponse({'token':token,'uid':uid},safe =False)

def lobby(request):

	return render(request,'lobby.html')


def room(request):

	return render(request,'room.html')

def signup(request):
	if request.method == "POST":
		username = request.POST['username']
		name = request.POST['name']
		password = request.POST['password']
		email = request.POST['email']
		try :
			mod = request.POST['moderator']
			mod =1
		except:
			mod = 0

		if not (User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists() ):
			user = User.objects.create_user(username=username,password= password,email=email,first_name=name)
			user.save()

			user = authenticate(request,username=username,password=password)
			login(request,user)

			user_model = User.objects.get(username=username)
			new_profile = Profile.objects.create(user=user_model,id_user =user_model.id,moderator =mod)
			new_profile.save()



	return render(request,'signup.html')

def settings(request):
	rooms = Room.objects.filter(user =request.user)
	context = {'rooms':rooms}

	if request.method =="POST":
		room = request.POST['room']
		user = request.POST['user']

		user = User.objects.get(username=user)
		room = Room.objects.get(name = room)
		print(user,room)
		Room_User.objects.create(room_user = user,room=room)

		return render(request,'settings.html',context)

	

	return render(request,'settings.html',context)


def create(request):

	if request.method =="POST":
		appId = '5f7dc3acd0244a25b98292f65d5d2063'
		appCertificate = 'c3795ffcc76844ffb37af64fb97715f3'
		channelName = request.POST['room']
		uid = random.randint(1,230)
		privilegeExpiredTs =  time.time() + 3600*24
		role = 1
		token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
			
		user = User.objects.get(username=request.user)
		my_room = Room.objects.create(user = user,name=channelName,token=token,uid=uid)		

		return render(request,'create-room.html')

	return render(request,'create-room.html')