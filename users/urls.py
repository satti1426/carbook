from django.contrib import admin
from django.urls import path
from .views import *




app_name = 'users'

urlpatterns = [
    path('signup/', signup,name='signup'),
    path('',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('homepage/',homepage,name='homepage'),

    
    path('user/',Userss,name='User'),
    path('view-user/<int:id>/',ViewUser,name='view_user'),
    path('edit-user/<int:id>/',EditUser,name='edit_user'),
    path('delete-user/<int:id>/',deleteUser,name='deleteUser'),


    path('company/',AddCompany,name='comapany'),
    path('view-company/<int:id>/',viewCompany,name='view_company'),
    path('edit-company/<int:id>/',editcompany,name='edit_company'),
    path('delete-company/<int:id>/',DeleteCompany,name='delete_company'),

    path('carss/',car,name='carss'),
    path('view-car/<int:id>/',ViewCar,name='view_car'),
    path('edit-car/<int:id>/',editcar,name='editcar'),
    path('delete-car/<int:id>/',DeleteCar,name='delete_car')

    

]
    
   
   
  
   
    
   
    
    # path('userdelete/<int:id>/',userdelete,name='userdelete')


    # path('edit/',Edit,name='edit')

