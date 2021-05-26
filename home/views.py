from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import feedback
from home.models import order
from django.contrib import messages

# Create your views here.
def index(request): 
    if request.method=="POST":
         name=request.POST.get('name')
         email=request.POST.get('email')
         phone=request.POST.get('phone')
         description=request.POST.get('description')
         contact =feedback(name=name, email=email,phone=phone, description= description,date=datetime.today())
         contact.save()
         messages.success(request, 'Feedback has been sent.')

    return render(request, 'index.html') 

def gallery(request):
    if request.method=="POST":
         name=request.POST.get('name')
         email=request.POST.get('email')
         phone=request.POST.get('phone')
         description=request.POST.get('description')
         contact =feedback(name=name, email=email,phone=phone, description= description,date=datetime.today())
         contact.save()
         messages.success(request, 'Feedback has been sent.')

    return render(request, 'gallery.html')

def about(request):
    if request.method=="POST":
         name=request.POST.get('name')
         email=request.POST.get('email')
         phone=request.POST.get('phone')
         description=request.POST.get('description')
         contact =feedback(name=name, email=email,phone=phone, description= description,date=datetime.today())
         contact.save()
         messages.success(request, 'Feedback has been sent.')

    return render(request, 'about.html')

def orders(request):
    if request.method=="POST":
         name=request.POST.get('name')
         email=request.POST.get('email')
         phone=request.POST.get('phone')
         description=request.POST.get('description')
         contact =feedback(name=name, email=email,phone=phone, description= description,date=datetime.today())
         contact.save()
         messages.success(request, 'Feedback has been sent.')

    return render(request, 'order.html')

def order1(request):
    if  request.method=="POST":
        print(request.POST)
        print(request.FILES)
        name1=request.POST.get('name1')
        email1=request.POST.get('email1')
        phone1=request.POST.get('phone1')
        description1=request.POST.get('description1')
        image=request.FILES.get('image')
        print(image)
        ordercontact=order(name1=name1, email1=email1,phone1=phone1, description1= description1, image=image,date=datetime.today())
        ordercontact.save()
        messages.success(request, 'Order has been sent! wait for confirmation')

    return render(request, 'order.html')