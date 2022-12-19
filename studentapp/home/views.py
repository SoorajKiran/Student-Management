from django.shortcuts import render,redirect
from django.views import View
from account.models import Staff,Contact
from .forms import StudentForm
from .models import Student
from django.contrib import messages
# Create your views here.


class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Enquiry(View):
    def get(self,request):
        customer=Contact.objects.all()

        return render(request,'enquiry.html',{'form':customer})

class Staffs(View):
    def get(self,request):
        staff=Staff.objects.all()
        return render(request,'staff.html',{'form':staff})

class Profile(View):
    def get(self,request):
        return render(request,'profile.html')

class StudentAdd(View):
    def get(self,request):
        form=StudentForm()
        return render(request,'studentadd.html',{'forms':form})
    def post(self,request):
        if request.method=="POST":
            form=StudentForm(request.POST)
            if form.is_valid():
                form.save()
                students=Student.objects.all()
                return render(request,'showstudents.html',{'form':students})
            else:
                print("Form not valid")
            return redirect("showstudents")

class ShowStudents(View):
    def get(self,request):
        student=Student.objects.all()
        return render(request,'showstudents.html',{'form':student})

class Edit(View):
    def get(self,request):
        edit1=request.GET['edit']
        edit=Student.objects.filter(student_id=edit1)
        return render(request,'studentedit.html',{'forms':edit})
    def post(self,request):
        edit1=request.GET['edit']
        if request.method == 'POST':
            if Student.objects.filter(student_id=edit1).exists():
                if request.POST['stud_address']:
                    Student.objects.filter(student_id=edit1).update(stud_address=request.POST['stud_address'])
                if request.POST['stud_place']:            
                    Student.objects.filter(student_id=edit1).update(stud_place=request.POST['stud_place'])
                if request.POST['stud_name']:            
                    Student.objects.filter(student_id=edit1).update(stud_name=request.POST['stud_name'])
                if request.POST['stud_email']:            
                    Student.objects.filter(student_id=edit1).update(stud_email=request.POST['stud_email'])
                if request.POST['stud_phone']:            
                    Student.objects.filter(student_id=edit1).update(stud_phone=request.POST['stud_phone'])
                student=Student.objects.all()
                return render(request,'showstudents.html',{'form':student})

class Delete(View):
    def get(self,request):
        delete=request.GET['delete']
        Student.objects.filter(student_id=delete).delete()
        student=Student.objects.all()
        return render(request,'showstudents.html',{'form':student})


class Profile(View):
    def get(self,request):
        if request.session['email'] is not None:
            customer=Staff.objects.filter(email=request.session['email'])
        return render(request,'profile.html',{'customer':customer})

class EditProfile(View):
    def get(self,request):
        edit1=request.session['email']
        edit=Staff.objects.filter(email=edit1)
        return render (request,'editprofile.html',{'forms':edit})
    def post(self,request):
        edit1=request.session['email']
        if request.method == 'POST':
            if Staff.objects.filter(email=edit1).exists():
                if request.POST['password']:
                    Staff.objects.filter(email=edit1).update(password=request.POST['password'])
                if request.POST['name']:
                    Staff.objects.filter(email=edit1).update(name=request.POST['name'])
                if request.POST['email']:
                    if Staff.objects.filter(email=request.POST['email']).exists():
                        edit=Staff.objects.filter(email=edit1)
                        messages.error(request,"Email id already exists")
                        return render(request,'editprofile.html',{'forms':edit})
                    else:
                        Staff.objects.filter(email=edit1).update(email=request.POST['email'])
                        request.session['email']=request.POST['email']
                    
                if request.POST['phno']:
                    Staff.objects.filter(email=edit1).update(phno=request.POST['phno'])

                customer=Staff.objects.filter(email=request.session['email'])
                return render(request,'profile.html',{'customer':customer})
                
