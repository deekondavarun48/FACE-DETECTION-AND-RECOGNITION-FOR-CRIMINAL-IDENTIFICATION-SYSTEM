from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from adminapp.models import *
import os

def home_user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            officer = Police_OfficersModel.objects.get(officer_email=email, officer_password=password)
            request.session['officer_id'] = officer.officer_id
            messages.success(request, 'Login successful')
            return redirect('user_index')
        except:
            messages.error(request, 'Invalid email or password')
    return render(request, 'home/home-user-login.html')

def user_index(request):
    return render(request, 'user/user-index.html')

def user_my_profile(request):
    officer_id = request.session.get('officer_id')
    officer = None
    if officer_id:
        officer = Police_OfficersModel.objects.filter(officer_id=officer_id).first()
    return render(request, 'user/user-my-profile.html', {'officer': officer})

def user_search_criminal(request):
    criminals = Criminals_DetailsModel.objects.all()
    return render(request, 'user/user-search-criminal.html', {'criminals': criminals})

def criminal_validate(request, id):
    criminal = get_object_or_404(Criminals_DetailsModel, criminal_id=id)
    match_result = None
    
    if request.method == "POST" and request.FILES.get('captured_image'):
        # Lazy-import DeepFace inside function to prevent Gunicorn timeout on startup
        from deepface import DeepFace
        
        captured = request.FILES['captured_image']
        temp_path = f"media/temp_{captured.name}"
        with open(temp_path, 'wb+') as destination:
            for chunk in captured.chunks():
                destination.write(chunk)
                
        try:
            db_image_path = criminal.criminal_image.path
            result = DeepFace.verify(img1_path=temp_path, img2_path=db_image_path, enforce_detection=False)
            match_result = result.get('verified', False)
        except Exception as e:
            match_result = False
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
                
    return render(request, 'user/user-search-criminal.html', {'criminal': criminal, 'match_result': match_result})
