from django.contrib import admin
from .models import Gallery, Contact

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('type', 'title', 'img')  
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact_number', 'inquiry', 'message')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Gallery, GalleryAdmin)