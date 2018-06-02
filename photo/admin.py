from django.contrib import admin

from .models import Tag, Photo, Associate, Profile

admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(Associate)
admin.site.register(Profile)