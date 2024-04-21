from django.contrib import admin
from .models import Recipe, Cuisine, Comment


admin.site.register(Recipe)
admin.site.register(Cuisine)
admin.site.register(Comment)
