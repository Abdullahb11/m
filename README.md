# Mood Detector Web App

A Django web application that detects mood from uploaded images using DeepFace.

## Features

- Upload images to detect mood
- Analyze emotions (happy, sad, angry, fearful, disgust, surprise, neutral)
- Display confidence scores for each emotion
- Mobile-friendly design

## Requirements

- Python 3.8+
- Django 4.2.0
- DeepFace 0.0.79
- OpenCV
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:
```
git clone <repository-url>
cd mood
```

2. Create a virtual environment and activate it:
```
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Apply migrations:
```
cd app
python manage.py migrate
```

5. Run the development server:
```
python manage.py runserver
```

6. Open your browser and navigate to http://127.0.0.1:8000/

## Deployment on Railway

1. Create a new project on Railway
2. Connect your GitHub repository
3. Set up the environment variables:
   - `PORT=8000`
   - `ALLOWED_HOSTS=your-railway-domain.up.railway.app`
   - `DEBUG=False`
4. Deploy the application

## License

MIT 