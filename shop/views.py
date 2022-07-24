from django.shortcuts import redirect, render
from django.http  import HttpResponse
from django.urls import is_valid_path
from .models import BookTable
from .forms import BookTableFrom
from . models import Food

# Create your views here.


def index(request):
    return render(request,'shop/about.html')


def about(request):
    return render(request,'shop/about.html')

def event(request):
    return render(request,'shop/event.html')

def menu(request):
    foods =  Food.objects.values('food_name', 'food_price','food_description')
   
    context = {'foodDetails': foods}
    print(context)
    return render(request,'shop/menu.html',context)


def contact(request):
    return render(request,'shop/booktable.html')


def bookTable(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        people = request.POST.get('people')
        bdate = request.POST.get('date')
        btime = request.POST.get('time')
        booktable = BookTable(name=name,email=email,phone=phone,message=message,people=people,bdate=bdate,btime=btime)
    
        booktable.save()
        # print(booktable)
        # print(BookTable.objects.all())
    # return render(request,'shop/booktable.html')
    return  redirect('/shop/contact')
        




def getFoodDetails(request):
    foods =  Food.objects.get()
    print(foods)




# request.POST.get('my_field')
#   if request.method == 'POST':
#         form  = BookTableFrom(request.POST)
#         if(form.is_valid()):
#             form.save()