from rest_framework import serializers
from .models import Tag, Photo


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('tag', 'value')


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'

class PhotoUpdateSerializer(serializers.ModelSerializer):

    strtags = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = Photo
        fields = ('is_checked', 'strtags')