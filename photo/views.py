from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.renderers import (
                                        HTMLFormRenderer,
                                        JSONRenderer,
                                        BrowsableAPIRenderer,
                                    )
from rest_framework.views import APIView

from photo.models import Photo, Tag, Associate
from rest_framework.decorators import api_view
from .serializers import TagSerializer, PhotoSerializer, PhotoUpdateSerializer
from rest_framework.response import Response


class CustomerApi(APIView):

    serializer_class = PhotoSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)


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
        serializer_context = {
            'request': request,
        }
        serializer = PhotoSerializer(photos, many=True, context=serializer_context)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer_context = {
            'request': request,
        }
        serializer = PhotoSerializer(data=request.data, context=serializer_context)

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
        serializer = PhotoUpdateSerializer(photo, data=request.data)


        if serializer.is_valid():
            tags_id = request.data['strtags'].split(',')
            print(tags_id)
            for tag_id in tags_id:
                tag_id = int(tag_id)
                try:
                    tag = Tag.objects.get(pk=tag_id)
                except Tag.DoesNotExist:
                    print("not tag")
                photo.tags.add(tag)
                # associate = Associate.objects.create(photo)
                # print(associate)

            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def home(request):
    return render(request, 'home.html')