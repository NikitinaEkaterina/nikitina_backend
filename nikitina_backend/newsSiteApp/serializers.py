from rest_framework import serializers

from .models import User, News, Tag


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class NewsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class TagSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'