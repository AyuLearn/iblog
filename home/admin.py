from django.contrib import admin
from .models import Post, BlogComments

# Register your models here.
admin.site.register((Post, BlogComments))