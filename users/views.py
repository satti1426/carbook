from django.shortcuts import render,redirect
# from .models import Post
# from django.http import HttpResponse
from django.contrib.auth.models import make_password
# from django.contrib.auth.models import AbstractUser
from .models import User
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login,logout,authenticate
from django.views.generic import View,TemplateView
from django.contrib import messages
from users.models import *
# from .serializers import  UserSerializer
from django.http import JsonResponse


# def user_info(request):
#     stu=User.objects.all()
#     serial=UserSerializer(stu,many=True)
#     return JsonResponse(serial.data, safe=False)




# from .utils import *


# Create your views here.

class AdminLoginView(TemplateView):
    def get(self, request, *args, **kwargs):
        return redirect('users:login')



def signup(request):
        # signup_detail=signup.object.all()
        if request.method == 'GET':
            return render(request,'signup.html')
        
             
        if request.method == 'POST':
            if User.objects.filter(email=request.POST.get('email')).exists():
                return render(request,'signup.html',{'message':'email already exixts!'})
            
            User.objects.create(first_name=request.POST.get('firstName'),username=request.POST.get('email'),email=request.POST.get('email'),password=make_password(request.POST.get('password')))
        return redirect('users:login')
            

def Login(request):
    if request.method == 'GET':
            if request.user.is_authenticated and request.user.is_superuser:
                return redirect('admin:index')
            elif request.user.is_authenticated and not request.user.is_superuser:
                return redirect('users:homepage')
            return render(request,'login.html')
     
    #  if request.method=='GET':
    #       return redirect(request,'signup.html')
    if request.method=='POST':
       username=request.POST.get('username')
       pass1=request.POST.get('password')
       user=authenticate(request,username=username,password=pass1)

    #    print(user,'11111111111')
       if user is not None:
            login(request,user)
            if user.is_superuser:
                 return redirect('admin:index')
            return redirect("user:homepage")
       else:
            messages.success(request, 'Incorrect Password!')
            return render(request,'login.html')
       


def Logout(request):
    logout(request)
    return redirect('users:login')
     
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .helpers import *

@login_required(login_url='/')
def homepage(request):

    car=Car.objects.all()
    company=Comapany.objects.all()
    
    notify=notification.objects.filter(created_for=request.user)
    # print(notify)
    

    # data=pagination(request,car)
    return render(request,'homepage.html',{'cars':car,'compani':company,'notification':notify})


def dashboard(request):
     return render(request,'dashboard.html')

def Userss(request):
        # signup_detail=signup.object.all()
        if request.method == 'GET':
         obj1=User.objects.all().exclude(is_superuser=True).order_by("-created_on")
         
         return render(request,'admin/USER/user.html',{'user':obj1})
        
        if request.method == 'POST':
           User.objects.create(first_name=request.POST.get('firstName'),username=request.POST.get('email'),email=request.POST.get('email'),password=make_password(request.POST.get('password')))
        return redirect('users:User')
        

def ViewUser(request,id):   
    user=User.objects.get(id=id)
    return render(request,'admin/USER/view-user.html',{'user':user})


def EditUser(request,id):
    user=User.objects.get(id=id)
    if request.method == 'GET':
        return render(request,'admin/USER/edit-user.html',{'user':user})
    if request.method=='POST':
        user.email=request.POST.get('email')
        user.first_name=request.POST.get('firstname')
        user.save()
        return redirect('users:view_user', id=user.id)
    
def deleteUser(request,id):
    User.objects.get(id=id).delete()
    return redirect('users:User')


def AddCompany(request):
     
    if request.method=='GET':
        obj=Comapany.objects.all().order_by("-created_ons")
        company,cars=[],[]
        # for s in state:
        #     states.append(s)
        #     districts.append([[i,Treks.objects.filter(district_id=i.id)] for i in s.districts_set.all()])
        # lst=list(zip(states,districts))

        for i in obj:
            company.append(i)
            cars.append(Car.objects.filter(company_id=i.id))
        lst=list(zip(company,cars))    

        # print(lst,'1111111111111111')
        # user1=User.object.all()
        return render (request,'admin/COMPANY/company.html',{'obj':obj,'lst':lst})
    if request.method == 'POST':
         
         Comapany.objects.create(name=request.POST.get('company_name'),user=request.user)
        #  obj.save()
         return redirect('users:comapany')

def viewCompany(request,id):
    company=Comapany.objects.get(id=id)

    
    return render (request,'admin/COMPANY/view-company.html',{'companys':company})

def editcompany(request,id):
      company = Comapany.objects.get(id=id)
      if request.method == 'GET': 
       return render(request,'admin/COMPANY/edit-company.html',{'company':company})
       
      if request.method=='POST':
         company.name = request.POST.get('name')
         company.save()
         return redirect('users:view_company',id=company.id)
         
def DeleteCompany(request,id):
     Comapany.objects.get(id=id).delete()
     return redirect('users:comapany')   


def car(request):
    if request.method == 'GET':
        
        car=Car.objects.all().order_by("-created_on")
        # print(car.values())
        company=Comapany.objects.all()
        return render(request,'admin/CAR/carss.html',{'cars':car,'companies':company,})
    
    if request.method == 'POST':
        car = Car.objects.create(company=Comapany.objects.get(id=request.POST.get('company')),car_name=request.POST.get('carname'), car_type=request.POST.get('car_type'), model=request.POST.get('model'))
        # messages.success(request, "  New Car Added In List.")
        users=User.objects.all()
        for user in users:
            notification.objects.create(created_for=user,created_by=request.user,title='new car added')
       
        return redirect('users:carss')
    
    

def ViewCar(request,id): 
     car=Car.objects.get(id=id)
     companies = Comapany.objects.all()
     return render(request,'admin/CAR/view-car.html',{'cars':car,'companies':companies})

def editcar(request,id):

     car=Car.objects.get(id=id)
     companies = Comapany.objects.all()
     if request.method == 'GET':
         return render(request,'admin/CAR/edit-car.html',{'car':car,'companies':companies})
     if request.method=='POST':
        car.car_name = request.POST.get('car_name')
        car.company_id = request.POST.get('company')
        car.model = request.POST.get('model')
        car.car_type = request.POST.get('car_type')
        car.save()
        return redirect("users:view_car",id=car.id)

def DeleteCar(request,id):
     Car.objects.get(id=id).delete()
     return redirect('users:carss')



  

    
# def userdelete(request,id):
#     if request.method=='GET':
#      user=User.objects.get(id==id)
#      user.delete()
#      return render(request,'admin/user.html',{'user':user})


    # return redirect('users:user')

# def (request):
#     pass

     

      