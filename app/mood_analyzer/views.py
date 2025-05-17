from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ImageAnalysis
from deepface import DeepFace
import numpy as np
import cv2
import os
import tempfile

# Create your views here.
def home(request):
    return render(request, 'mood_analyzer/home.html')

def analyze_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        
        # Save the uploaded image to the database
        analysis = ImageAnalysis(image=image_file)
        analysis.save()
        
        # Get the image path
        image_path = analysis.image.path
        
        try:
            # Analyze the image using DeepFace
            result = DeepFace.analyze(img_path=image_path, 
                                     actions=['emotion'],
                                     enforce_detection=False)
            
            # Extract the emotion with highest score
            emotions = result[0]['emotion']
            dominant_emotion = result[0]['dominant_emotion']
            confidence = emotions[dominant_emotion]
            
            # Map DeepFace emotions to our model's emotions
            emotion_mapping = {
                'happy': 'happy',
                'sad': 'sad',
                'angry': 'angry',
                'fear': 'fearful',
                'disgust': 'disgust',
                'surprise': 'surprise',
                'neutral': 'neutral'
            }
            
            # Update the analysis record
            analysis.mood = emotion_mapping.get(dominant_emotion, dominant_emotion)
            analysis.confidence = confidence
            analysis.save()
            
            return render(request, 'mood_analyzer/result.html', {
                'analysis': analysis,
                'emotions': emotions
            })
            
        except Exception as e:
            # If analysis fails, delete the image and return an error
            analysis.image.delete()
            analysis.delete()
            return render(request, 'mood_analyzer/home.html', {
                'error': f"Error analyzing image: {str(e)}"
            })
    
    return redirect('home')
