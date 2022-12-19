from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
     path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
     path('forgot/',views.forgot,name="forgot"),
    path('contact/',views.contact,name="contact"),

    path('mainhome/',views.mainhome,name="mainhome"),
    path('gallery/',views.gallery,name="gallery"),
    path('course/',views.course,name="course")
]

