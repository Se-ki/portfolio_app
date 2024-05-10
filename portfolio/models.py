from django.db import models

# Create your models here.

class Contact(models.Model):
    TYPE_CHOICES = (
        ('Advertising', 'Advertising'),
        ('Editorial', 'Editorial'),
        ('Men\'s Grooming', 'Men\'s Grooming'),
        ('Runaway Show', 'Runaway Show'),
        ('ws', 'Wig Styling'),
    )
    
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    inquiry = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.email
    
    class Meta:
        db_table = "contacts"
    
class Gallery(models.Model):
    TYPE_CHOICES = (
        ('advertisement', 'Advertisement'),
        ('editorial', 'Editorial'),
        ('mg', 'Men\'s Grooming'),
        ('rs', 'Runaway Show'),
        ('ws', 'Wig Styling'),
    )
    
    type = models.CharField(max_length=100, choices=TYPE_CHOICES) 
    title = models.CharField(max_length=100)
    img = models.ImageField(default="no-image.jpg", upload_to="gallery")
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = "gallery"