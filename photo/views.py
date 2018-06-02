from django.shortcuts import render, redirect
from rest_framework import status

from photo.models import Photo, Tag
from rest_framework.decorators import api_view
from .serializers import TagSerializer, PhotoSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def tag_list(request):
    if request.method == 'GET':

        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def tag_detail(request, pk):
    try:
        tag = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'GET':
        serializer = TagSerializer(tag)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def photo_list(request):
    if request.method == 'GET':

        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PhotoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def photo_detail(request, pk):
    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'GET':
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = PhotoSerializer(photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def home(request):
    return render(request, 'home.html')