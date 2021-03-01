from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from django.views.generic.edit import DeleteView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from .models import Avatar, vrcUser
from django.http import JsonResponse
import simplejson as json
from .serializers import AvatarSerializer,vrcUserSerializer
from django.shortcuts import redirect
from requests.auth import HTTPBasicAuth
import datetime
import requests,base64
from requests.structures import CaseInsensitiveDict
from django.urls import reverse
from django.core import serializers
from django.db.models import Q
import random

#CONSTANT VARIABLES

apiURL="https://api.vrchat.cloud/api/1/"
apiKey="JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26"

#MAIN FUNCTION USED FOR AUTH REQUESTS


@csrf_exempt
def authrequest(request,url):

	if request.session.get('loggedin'):

		print(url, flush=True)

		userpass = request.session.get('username') + ':' + request.session.get('password')

		encodedBytes = base64.b64encode(userpass.encode("utf-8"))
		encodedStr = str(encodedBytes, "utf-8")

		headers = CaseInsensitiveDict()
		headers["Authorization"] = "Basic " + encodedStr
		headers["User-Agent"] = "SomeRandomAPI"
		
		resp = requests.get(url, headers=headers)

		return resp.json()

	else:

		return HttpResponse('You need to be logged in')

@csrf_exempt
def POSTauthrequest(request,data,url):

	if request.session.get('loggedin'):

		print(url, flush=True)

		userpass = request.session.get('username') + ':' + request.session.get('password')

		encodedBytes = base64.b64encode(userpass.encode("utf-8"))
		encodedStr = str(encodedBytes, "utf-8")

		headers = CaseInsensitiveDict()
		headers["Authorization"] = "Basic " + encodedStr
		headers["User-Agent"] = "SomeRandomAPI"
		
		resp = requests.post(url,data, headers=headers)

		return resp.json()

	else:

		return HttpResponse('You need to be logged in')


#LOGIN AND LOGOUT RELATED FUNCTIONS

@csrf_exempt
def logintest(username,password,url = 'https://api.vrchat.cloud/api/1/auth/user'):

	userpass = username + ':' + password

	encodedBytes = base64.b64encode(userpass.encode("utf-8"))
	encodedStr = str(encodedBytes, "utf-8")

	headers = CaseInsensitiveDict()
	headers["Authorization"] = "Basic " + encodedStr
	headers["User-Agent"] = "SomeRandomAPI"
	
	resp = requests.get(url, headers=headers)

	return resp

@csrf_exempt
def login(request):

	if request.method=='POST':

		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)

		username = body['username']
		password = body['password']

		if not (username==None) and not (password==None):

			logintestdata = logintest(username,password).json()

			if not "error" in logintestdata:

				request.session['username']=username
				request.session['password']=password
				request.session['loggedin']=True


				if request.GET.get('addfavorite') != None:

					return addfavorite(request)

				if request.GET.get('moderations',None) == 'true':

					return getModerations(request)

				if request.GET.get('userdata',None) == 'true':

					return CurrentUserData(request)

				else:

					return JsonResponse({"Login":"Succesful"}, safe=False)

			else:

				return JsonResponse(logintestdata)
		else:

			return HttpResponse('Login Failed, fields must not be empty')

	else:
		
		return HttpResponse('Method not Allowed')


@csrf_exempt
def logout(request):

	request.session['username']=None
	request.session['password']=None
	request.session['loggedin']=None

	return HttpResponse('Logged Out')


#INFORMATION REQUEST FUNCTIONS


@csrf_exempt
def CurrentUserData(request):
	

	url = apiURL + "auth/user?apiKey=" + apiKey 

	data = authrequest(request,url)

	return JsonResponse(data,safe=False)



@csrf_exempt
def getUserDataById(request,userID):

	url = apiURL + "users/" + userID + "?apiKey=" + apiKey 

	print(url)
	data = authrequest(request,url)

	return JsonResponse(data,safe=False)

@csrf_exempt
def getUserDataByName(request,username):

	url = apiURL + "users/" + username + "/name" + "?apiKey=" + apiKey 

	print(url)
	data = authrequest(request,url)

	return JsonResponse(data,safe=False)


@csrf_exempt
def getModerations(request):


	url = apiURL + "auth/user/playermoderated" + "?apiKey=" + apiKey
	data = authrequest(request,url)

	return JsonResponse(data,safe=False)

@csrf_exempt
def getFriends(request):


	url = apiURL + "auth/user/friends"
	data = authrequest(request,url)

	return JsonResponse(data,safe=False)

@csrf_exempt
def searchUsers(request,n,name, offset):


	url = apiURL + "users?apiKey=" + apiKey +"&search=" + name +"&n=" + n
	data = authrequest(request,url)

	return JsonResponse(data,safe=False)

@csrf_exempt
def getAvatarsFromUser(request,userID):


	url = apiURL + "avatars?apiKey=" + apiKey + "&userId=" + userID
	data = authrequest(request,url)

	return JsonResponse(data,safe=False)

@csrf_exempt
def getAvatarData(request,avatarID):

	url = apiURL + "avatars?apiKey=" + apiKey + "&userId=" + userID
	data = authrequest(request,url)

	return JsonResponse(data,safe=False)

@csrf_exempt
def getRandomAvatar(request):

	avatar = random.choice(Avatar.objects.filter(releaseStatus="public").values())
	
	avatar_json = json.dumps(avatar)

	return HttpResponse(avatar_json, content_type='application/json')


def searchAvatars(request):

	authorName = request.GET.get('authorname',None)
	authorId = request.GET.get('authorId',None)
	avatarName = request.GET.get('avatarname', None)
	avatarId = request.GET.get('avatarid',None)
	releaseStatus = request.GET.get('releasestatus','public')


	filters = {}

	if authorName != None:
		filters['authorName__icontains'] = authorName
	if authorId != None:
		filters['authorId__icontains'] = authorId
	if avatarName != None:
		filters['name__icontains'] = avatarName
	if avatarId != None:
		filters['id__icontains'] = avatarId
	
	filters['releaseStatus__icontains'] = releaseStatus


	avatar_responselist = list(Avatar.objects.filter(**filters).values())
	avatar_json = json.dumps(avatar_responselist)

	return HttpResponse(avatar_json, content_type='application/json')

def addfavorite(request):

	url = apiURL + "favorites" + "?apiKey=" + apiKey
	
	json_data = {"type":"avatar","favoriteId":request.GET.get('addfavorite'),"tags":["avatars1"]}

	data = POSTauthrequest(request,json_data,url)

	return JsonResponse(data,safe=False)


"""
#/login params:

addfavorite=<string avatarId> -> Adds your avatar to your VRC account's favorites
moderations=<boolean> -> If True, it will return your account's moderations
userdata=<boolean> -> If True, it will return your account's user data

#/search params:

FILTER BY:

authorname=<string author name>
authorId=<string author name>
avatarname=<string avatar name>
avatarid=<string avatar ID>
releasestatus=<string public/private>

"""
