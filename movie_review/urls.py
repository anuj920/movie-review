"""movie_review URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',views.HomeView.as_view(),name='home'),
    path('movie_default/',views.movie_default, name='movie_default'),
    path('movie_serach/',views.movie_search, name='movie_search'),
    path('movie_detail/<pk>/',views.movie_detail, name='movie_detail'),
    path('next/<int:nex>/<quer>/',views.movie_next_page, name='next_page'),
    path('prev/<int:prev>/<quer>/',views.movie_prev_page, name='prev_page'),
    path('first/<quer>/',views.movie_first_page, name='first_page'),
    path('last/<int:pag>/<quer>/',views.movie_last_page, name='last_page'),
    path('review_movie/<pk>',views.review, name='review'),
    path('dash/',views.OwnList.as_view(),name='dash'),
    path('review_detail/<pk>/',views.movie_review_detail,name = 'movie_review_detail'),
    path('profile/',views.ProfileView.as_view(),name='profile')
]
