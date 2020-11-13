from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.blog, name='blog'),
    path('signup', views.signupUser, name='signupUser'),
    path('search', views.search, name='search'),
    path('login', views.loginUser, name='loginUser'),
    path('comments', views.postComments, name='postComments'),
    path('upload', views.uploadPost, name='uploadPost'),
    path('logout', views.logoutUser, name='logoutUser'),
    path('<str:slug>', views.post, name='post')
]