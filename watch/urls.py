"""activity_watch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from watch import views


urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home,name='home'),
    path('chetpet/', views.chetpet, name='chetpet'), 
    path('rajapalayam/', views.rajapalayam, name='rayapalayam'),
    path('media/', views.media, name='media'),
    path('accounts/', views.accounts, name='accounts'),
    path('database/', views.database, name='database'),
    path('database_developer/', views.database_developer, name='database_developer'),
    path('backup/', views.backup, name='backup'),
    path('instagram/', views.instagram, name='instagram'),
    path('database_chetpet/', views.database_chetpet, name='database_chetpet'),
    path('instagram_chetpet/', views.instagram_chetpet, name='instagram_chetpet'),
    path('overallchetpet/', views.overallchetpet, name='overallchetpet'),
    path('overallrajapalayam/', views.overallrajapalayam, name='overallrajapalayam'),
    path('api/',views.getdataapi, name='api'),
    path('logout',views.logout,name='logout'),
]
