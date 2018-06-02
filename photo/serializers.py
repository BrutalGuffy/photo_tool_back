from rest_framework import serializers
from .models import Tag, Photo


class TagSerializer(serializers.ModelSerializer):
    # tag = serializers.CharField(max_length=240)

    class Meta:
        model = Tag
        fields = ('tag',)


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'

