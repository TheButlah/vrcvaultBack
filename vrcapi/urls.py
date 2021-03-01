
from django.urls import path
from .serializers import AvatarSerializer
from .views import	logout,login,CurrentUserData,getModerations,getUserDataById,searchAvatars,getRandomAvatar

urlpatterns = [
	path('logout',logout, name="logout" ),
    path('login',login, name="login" ),
    path('getuserdata/<slug:userID>',getUserDataById, name="get-user-data"),
    path('currentuserdata',CurrentUserData,name="current-user-data"),
    path('search/',searchAvatars, name="search-avatar"),
    path('randomavatar',getRandomAvatar,name="random-avatar"),
]
