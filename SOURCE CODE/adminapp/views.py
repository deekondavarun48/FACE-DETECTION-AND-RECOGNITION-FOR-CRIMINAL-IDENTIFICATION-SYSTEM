from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from adminapp.models import *

def home_admin_login(request):
    if request.method == "POST":
        admin_name = request.POST.get('username')
        admin_pass = request.POST.get('password')
        if admin_name == 'admin' and admin_pass == 'admin':
            request.session['admin'] = 'admin'
            messages.success(request, 'Admin login successful')
            return redirect('admin_index')
        else:
            messages.error(request, 'Invalid admin credentials')
    return render(request, 'home/home-admin-login.html')

def admin_index(request):
    total_criminals = Criminals_DetailsModel.objects.count()
    total_officers = Police_OfficersModel.objects.count()
    total_stations = Police_StationsModel.objects.count()
    total_crimes = Crime_DetailsModel.objects.count()
    return render(request, 'admin/admin-index.html', {
        'total_criminals': total_criminals,
        'total_officers': total_officers,
        'total_stations': total_stations,
        'total_crimes': total_crimes,
    })

def admin_add_criminals(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        crime = request.POST.get('crime')
        image = request.FILES.get('image')
        Criminals_DetailsModel.objects.create(
            criminal_name=name,
            criminal_age=age,
            criminal_gender=gender,
            criminal_crime=crime,
            criminal_image=image
        )
        messages.success(request, 'Criminal details added successfully')
        return redirect('admin_manage_criminals')
    return render(request, 'admin/admin-add-criminals.html')

def admin_manage_criminals(request):
    criminals = Criminals_DetailsModel.objects.all()
    return render(request, 'admin/admin-manage-criminals.html', {'criminals': criminals})

def admin_add_police_officers(request):
    stations = Police_StationsModel.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        station_id = request.POST.get('station')
        station = Police_StationsModel.objects.get(station_id=station_id)
        Police_OfficersModel.objects.create(
            officer_name=name,
            officer_email=email,
            officer_phone=phone,
            officer_password=password,
            officer_station=station
        )
        messages.success(request, 'Police officer added successfully')
        return redirect('admin_manage_police_officers')
    return render(request, 'admin/admin-add-police-officers.html', {'stations': stations})

def admin_manage_police_officers(request):
    officers = Police_OfficersModel.objects.all()
    return render(request, 'admin/admin-manage-police-officers.html', {'officers': officers})

def admin_add_police_stations(request):
    if request.method == "POST":
        name = request.POST.get('name')
        location = request.POST.get('location')
        city = request.POST.get('city')
        Police_StationsModel.objects.create(station_name=name, station_location=location, station_city=city)
        messages.success(request, 'Police station added')
        return redirect('admin_manage_police_stations')
    return render(request, 'admin/admin-add-police-stations.html')

def admin_manage_police_stations(request):
    stations = Police_StationsModel.objects.all()
    return render(request, 'admin/admin-manage-police-stations.html', {'stations': stations})

def admin_add_crime(request, id):
    return render(request, 'admin/admin-add-crime.html', {'id': id})

def admin_manage_crime(request):
    crimes = Crime_DetailsModel.objects.all()
    return render(request, 'admin/admin-manage-crime.html', {'crimes': crimes})

def admin_view_crime_records(request, id):
    return render(request, 'admin/admin-crime-records.html', {'id': id})

def admin_criminal_records(request, id):
    return render(request, 'admin/admin-criminal-records.html', {'id': id})

def admin_edit_police_officers_details(request, id):
    officer = get_object_or_404(Police_OfficersModel, officer_id=id)
    return render(request, 'admin/admin-edit-police-officers-details.html', {'officer': officer})

def admin_edit_station_details(request, id):
    station = get_object_or_404(Police_StationsModel, station_id=id)
    return render(request, 'admin/admin-edit-station-details.html', {'station': station})

def admin_view_police_officers_list(request, id):
    return render(request, 'admin/admin-view-police-officers-list.html', {'id': id})

def admin_view_criminals_list(request):
    criminals = Criminals_DetailsModel.objects.all()
    return render(request, 'admin/admin-view-criminals-list.html', {'criminals': criminals})

def officer_delete(request, id):
    Police_OfficersModel.objects.filter(officer_id=id).delete()
    return redirect('admin_manage_police_officers')

def officer_delete1(request, id):
    return redirect('admin_manage_police_officers')

def officer_delete2(request, id):
    return redirect('admin_manage_police_officers')
