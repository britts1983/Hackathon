from . import views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [

    path('register/',views.register, name="register"),
    path('admin/',admin.site.urls,name="admin"),
    path('',views.HOME, name="index"),
    path('regind/'
         '',views.regind, name="regind"),
    # Django JET URLS


]