from rest_framework import serializers
from .models import Avatar,vrcUser

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ['id', 'name','description','authorId','authorName','releaseStatus','updated_at','assetUrl','imageUrl','thumbnailImageUrl','created_at']

class vrcUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = vrcUser
        fields = ['id', 'username', 'displayName', 'bio']

