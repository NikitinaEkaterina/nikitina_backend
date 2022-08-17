from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password

from .models import User, News, Tag

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id'] = user.name
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class NewsSerialiser(serializers.ModelSerializer):
     author = serializers.SlugRelatedField(
        slug_field='username', 
        queryset=User.objects
     )
     
     tag = serializers.SlugRelatedField(
        slug_field='name',
        many=True,
        queryset=Tag.objects
     )

     class Meta:
        model = News
        fields = ['id','title', 'text', 'image', 'author', 'tag', 'author_id']

class UserSerialiser(serializers.ModelSerializer):

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'avatar', 'author', 'password']


class TagSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
