from django.conf.urls import url, include
from django.urls import path

from .views import tag_list, tag_detail, photo_list, photo_detail, home

urlpatterns = [
        path('tag_list/', tag_list),
        path('tag_detail/<int:pk>/', tag_detail),
        path('photo_list/', photo_list),
        path('photo_detail/<int:pk>/', photo_detail),
        path('home/', home)
]