"""Criminal_Tracker_Face_Detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from turtle import home
from django.contrib import admin
from django.urls import path
from adminapp  import views as adminapp_views
from homeapp import views as homeapp_views
from userapp import views as userapp_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-index',adminapp_views.admin_index,name='admin_index'),
    path('admin-add-criminals',adminapp_views.admin_add_criminals,name='admin_add_criminals'),
    path('admin-add-crime/<int:id>',adminapp_views.admin_add_crime,name='admin_add_crime'),
    path('admin-add-police-officers',adminapp_views.admin_add_police_officers,name='admin_add_police_officers'),
    path('admin-add-police-stations',adminapp_views.admin_add_police_stations,name='admin_add_police_stations'),
    path('admin-view-crime-records/<int:id>',adminapp_views.admin_view_crime_records,name='admin_view_crime_records'),
    path('admin-criminal-records/<int:id>',adminapp_views.admin_criminal_records,name='admin_criminal_records'),
    path('admin-edit-police-officers-details/<int:id>',adminapp_views.admin_edit_police_officers_details,name='admin_edit_police_officers_details'),
    path('admin-edit-station-details/<int:id>',adminapp_views.admin_edit_station_details,name='admin_edit_station_details'),
    path('admin-manage-criminals',adminapp_views.admin_manage_criminals,name='admin_manage_criminals'),
    path('admin-manage-crime',adminapp_views.admin_manage_crime,name='admin_manage_crime'),
    path('admin-manage-police-officers',adminapp_views.admin_manage_police_officers,name='admin_manage_police_officers'),
    path('admin-manage-police-stations',adminapp_views.admin_manage_police_stations,name='admin_manage_police_stations'),
    path('admin-view-police-officers-list/<int:id>',adminapp_views.admin_view_police_officers_list,name='admin_view_police_officers_list'),
    path('officer-delete/<int:id>',adminapp_views.officer_delete,name='officer_delete'),
    path('officer-delete1/<int:id>',adminapp_views.officer_delete1,name='officer_delete1'),
    path('officer-delete2/<int:id>',adminapp_views.officer_delete2,name='officer_delete2'),

    path('admin-view-criminals-list',adminapp_views.admin_view_criminals_list,name='admin_view_criminals_list'),
    
    
    # home urls
    path('',homeapp_views.home_index,name='home_index'),
    path('home-admin-login',adminapp_views.home_admin_login,name='home_admin_login'),
    path('home-user-login',userapp_views.home_user_login,name='home_user_login'),
    path('home-about',homeapp_views.home_about,name='home_about'),
    path('home-contact',homeapp_views.home_contact,name='home_contact'), 

    # user url
    
    path('user-index',userapp_views.user_index,name='user_index'),
    path('user-my-profile',userapp_views.user_my_profile,name='user_my_profile'),
    path('user-search-criminal',userapp_views.user_search_criminal,name='user_search_criminal'),
    path('criminal_validate/<int:id>/',userapp_views.criminal_validate,name='criminal_validate'),
    
    
    
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)