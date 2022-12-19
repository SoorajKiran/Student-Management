from django.contrib import admin
from .models import Contact,Course,Staff

class Customerdetails(admin.ModelAdmin):
    list_display=('name','phno','email')

admin.site.register(Contact,Customerdetails)
admin.site.register(Course)
admin.site.register(Staff)
# Register your models here.
