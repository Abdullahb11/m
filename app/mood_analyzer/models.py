from django.db import models
from django.utils import timezone

# Create your models here.
class ImageAnalysis(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('fearful', 'Fearful'),
        ('disgust', 'Disgust'),
        ('surprise', 'Surprise'),
        ('neutral', 'Neutral'),
    ]
    
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, null=True, blank=True)
    confidence = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"Image {self.id} - Mood: {self.mood}"
