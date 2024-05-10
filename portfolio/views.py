from django.shortcuts import render, redirect
from .models import Gallery, Contact
from django.http import JsonResponse
import json

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    gallery = Gallery.objects.all().order_by('-id')
    
    context = {
        'gallery': gallery,
    }
    
    return render(request, 'gallery.html', context)

def contact(request):
    if request.method == "POST":
        data = json.load(request)
        name = data.get('name')
        email = data.get('email')
        contact_number = data.get('contactNumber')
        inquiry = data.get('inquiry')
        message = data.get('message')
        contact = Contact(name=name, email=email, contact_number=contact_number, inquiry=inquiry, message=message)
        contact.save()
        return JsonResponse({'response': 'Success'})
    
    return render(request, 'contact.html')