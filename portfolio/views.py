from django.shortcuts import render, redirect
from .models import Gallery, Contact

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
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        inquiry = request.POST.get('inquiry')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, contact_number=contact_number, inquiry=inquiry, message=message)
        contact.save()
        return redirect('contact')
    
    return render(request, 'contact.html')