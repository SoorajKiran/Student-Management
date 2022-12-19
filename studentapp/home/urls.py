from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.Home.as_view(),name='home'),
    path('enquiry/',views.Enquiry.as_view(),name='enquiry'),
    path('staff/',views.Staffs.as_view(),name='staff'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('studentadd/',views.StudentAdd.as_view(),name='studentadd'),
    path('showstudents/',views.ShowStudents.as_view(),name="showstudents"),
    path('studentedit/',views.Edit.as_view(),name="studentedit"),
    path('delete/',views.Delete.as_view(),name="delete"),
    path('editprofile/',views.EditProfile.as_view(),name='editprofile'),
    
]

