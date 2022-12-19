from django.shortcuts import render, redirect
from django.contrib import messages
from .models  import Contact,Course,Staff

# Create your views here.
def index(request):
    return render(request,'mainhome.html')

def contact(request):
    if request.method=="POST":
        if request.POST['name'] is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            #messages.sucess(request,'contact soon')
            dicts={ 'out':1,'name': request.POST['name'] }
            return render(request,'contact.html',dicts)
    return render(request,'contact.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST["password"]
        try:
            check_user = Staff.objects.get(email=email,password=password)
            request.session['email']=check_user.email
            request.session['name']=check_user.name
            request.session['phno']=check_user.phno
            return redirect('home')
        except Staff.DoesNotExist:
            messages.error(request,'Invalid username or password !')
            return redirect('login')
    return render(request,'index.html')

def signup(request):

    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        phno=request.POST['phno']
        password2=request.POST['password2']

        if password==password2:
            if Staff.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('signup')
            else:
                customer= Staff.objects.create(email = email, name = name, password = password, phno = phno )
                customer.save()
                messages.info(request,'User created succesfully')
                return redirect('login')

        else:
            messages.info(request,'Password doesnt match')
            return redirect('signup')

    else:
        return render(request,'signup.html')

def forgot(request):
    return render(request,'forgot.html')

def gallery(request):
    return render(request,'gallery.html')


def mainhome(request):
    return render(request,'mainhome.html')

def course(request):
  courses={
  'course':Course.objects.all()
  }
  return render(request,'course.html',courses)

def forgot(request):

    if request.method == "POST":
        email= request.POST['email']
        password= request.POST['password']
        if Staff.objects.filter(email=email).exists():
            Staff.objects.filter(email=email).update(password=password)
            return redirect('login')
        
        else:
            messages.error(request,"Invalid email id")
            return redirect('forgot')
    return render(request,'forgot.html')