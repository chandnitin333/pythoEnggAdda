from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.index,name="ShopHome"),
    path('about/',views.about,name="About"),
    path('event/',views.event,name="Event"),
    path('menu/',views.menu,name="Menu"),
    path('contact/',views.contact,name="Contact"),
    path('booktable/',views.bookTable,name="bookTable"),
    
    
    
    
]