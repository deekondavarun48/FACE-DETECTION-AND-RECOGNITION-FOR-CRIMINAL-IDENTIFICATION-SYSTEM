from ast import Return
from email.message import Message
from itertools import count
# from ssl import _PasswordType
from django.db.models import Avg,Max,Min,Sum,Count,StdDev,Variance
from django.shortcuts import render,redirect
from django.contrib import messages
from adminapp.models import *
from userapp.blockchainAlgo import *
import secrets
import string
import requests
from datetime import *




# admin views here.
def home_admin_login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username)
        print(password)

        if username == "admin" and password == "admin":
            messages.success(request, "Logged In Successfully.")
            return redirect('admin_index')
        else:
            messages.error(request,"Invalid Username or Password")
            return redirect('home_admin_login')
    return render(request,"home/home-admin-login.html")
   

def admin_index(request):
    ps_count = PoliceStationModel.objects.all().count()
    po_count = PoliceOfficerModel.objects.all().count()
    cl_count = CriminalModel.objects.all().count()
    cs_count = CrimeModel.objects.all().count()

    return render(request,"admin/admin-index.html",{'x':ps_count,'y':po_count,'z':cl_count,'a':cs_count})

def admin_add_criminals(request):
    today = date.today()
    
    if request.method == "POST" and request.FILES["profile"]:
        aadhar=request.POST.get("aadhar")
        name=request.POST.get("name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        city=request.POST.get("city")
        profile=request.FILES["profile"]
        s1 = CriminalModel.objects.create(criminal_aadhar=aadhar,
                                        criminal_name=name,
                                        criminal_email=email,
                                        criminal_contact=contact,
                                        criminal_city=city,
                                        criminal_profile=profile,
                                        criminal_crime_date= today
                                        )
        s1.save()
        if s1:
            s2 = CriminalModel.objects.get(criminal_aadhar=aadhar)
         
            key = "ndkh8syefuh983y4rjd38weuhw"
            #creating initial block
            block1 = CriminalBlock(key,s2.criminal_aadhar)
            print(block1.block_data)
            print(len(block1.block_hash))
            # c2.aadhar_block = block1.block_hash
            # c2.aadhar_block.save()

            block2 = CriminalBlock(block1.block_hash,s2.criminal_name)
            print(block2.block_data)
            print(len(block2.block_hash))
            # c2.name_block = block2.block_hash
            # c2.name_block.save()

            block3 = CriminalBlock(block2.block_hash,s2.criminal_email)
            print(block3.block_data)
            print(len(block3.block_hash))
            # c2.email_block = block3.block_hash
            # c2.email_block.save()

            block4 = CriminalBlock(block3.block_hash,s2.criminal_contact)
            print(block4.block_data)
            print(len(block4.block_hash))
            # c2.contact_block = block4.block_hash
            # c2.contact_block.save()

            block5 = CriminalBlock(block4.block_hash,s2.criminal_city)
            print(block5.block_data)
            print(len(block5.block_hash))
            # c2.city_block = block5.block_hash
            # c2.city_block.save()

            block6 = CriminalBlock(block5.block_hash,str(s2.criminal_profile))
            print(block6.block_data)
            print(len(block6.block_hash))
            # c2.profile_block = block6.block_hash
            # c2.profile_block.save()

            block7 = CriminalBlock(block6.block_hash,str(s2.criminal_crime_date))
            print(block7.block_data)
            print(block7.block_hash)
            # s2.date_block = block7.block_hash
            # s2.save()
        

        
            s2.aadhar_block = block1.block_hash
            s2.name_block = block2.block_hash
            s2.email_block = block3.block_hash
            s2.contact_block = block4.block_hash
            s2.city_block = block5.block_hash
            s2.profile_block = block6.block_hash
            s2.date_block = block7.block_hash
            s2.save(update_fields=['aadhar_block','name_block','email_block','contact_block','city_block','profile_block','date_block'])
            s2.save()
            print(s2.date_block,'asdasd')
            
                                        
            
                                        
        
        if s2:
            messages.success(request,"successfully added")
            return redirect('admin_add_criminals')
        else:
            messages.error(request,"Your form is not added, please try again")
            return redirect('admin_add_criminals')
    return render(request,"admin/admin-add-criminals.html")    

def admin_add_crime(request,id):
    s2=CriminalModel.objects.get(pk = id)
    today = date.today()

    if request.method == "POST":
        aadhar=request.POST.get("aadhar")
        crimetype=request.POST.get("crimetype")
        description=request.POST.get("description")

        s1=CrimeModel.objects.create(crime_aadhar=aadhar,
                                    crime_type=crimetype,
                                    crime_desc=description,
                                    crime_added_date = today

                                    )
        s1.save()
        if s1:

            key = "ndkh8syefuh983y4rjd38weuhw"
            crime1 = CriminalBlock(key,s1.crime_aadhar)
            print(crime1.block_data)
            print(len(crime1.block_hash))
            # i.aadhar_blk = crime1.block_hash
            # i.aadhar_blk.save()

            crime2 = CriminalBlock(crime1.block_hash,s1.crime_type)
            print(crime2.block_data)
            print(len(crime2.block_hash))
            # i.type_blk = crime2.block_hash
            # i.type_blk.save()

            crime3 = CriminalBlock(crime2.block_hash,s1.crime_desc)
            print(crime3.block_data)
            print(len(crime3.block_hash))
            # i.desc_blk = crime3.block_hash
            # i.desc_blk.save()
            print('udate')
            crime4 = CriminalBlock(crime3.block_hash,str(s1.crime_added_date))
            print(crime4.block_data)
            print(len(crime4.block_hash))
            

            
            s1.aadhar_blk=crime1.block_hash
            s1.type_blk = crime2.block_hash
            s1.desc_blk = crime3.block_hash
            s1.date_blk = crime4.block_hash
            s1.save(update_fields=['aadhar_blk','type_blk','desc_blk','date_blk'])
            s1.save()

                                        
            
            if s1:
                messages.success(request,"successfully added")
                return redirect('admin_view_criminals_list')
            else:
                messages.error(request,"form not added")
                return redirect('admin_view_criminals_list')
        
    return render(request,"admin/admin-add-crime.html",{'x':s2})

def admin_add_police_stations(request):
    if request.method == "POST":
        stt=request.POST.get("stt")
        city=request.POST.get("city")
        branch=request.POST.get("branch")
        locality=request.POST.get("locality")
        areacode=request.POST.get("areacode")
        contact=request.POST.get("contact")
        
        

        s1 = PoliceStationModel.objects.create(station_state=stt,station_city=city,station_name=branch,station_locality=locality,station_areacode=areacode,station_contact=contact)
        s1.save()
        if s1:
            messages.success(request,"successfully added")
        else:
            messages.error(request,"form not added,  try again")
            return redirect('admin_add_police_stations')
    
    return render(request,"admin/admin-add-police-stations.html")

def admin_add_police_officers(request):
    s2=PoliceStationModel.objects.all()
    if request.method == "POST" and request.FILES["profile"]:
        select=request.POST.get("select")
        badge=request.POST.get("badge")
        name=request.POST.get("name")
        email=request.POST.get("email")
        number=request.POST.get("number")
        
        profile=request.FILES["profile"]

        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        

        s1=PoliceOfficerModel.objects.create(officer_station=select,officer_badgeno=badge,officer_name=name,officer_email=email,officer_number=number,officer_password=password,officer_profile=profile)
        s1.save()
        s1=True
        if s1:
            
            url = "https://www.fast2sms.com/dev/bulkV2"
                # create a dictionary
            my_data = {'sender_id': 'FSTSMS', 
                            'message': 'Dear '+name+', your your login credentials are : Email : '+email+ 'Password : '+password+'Uses these for loging in.',
                            'language': 'english', 
                            'route': 'q', 
                            'numbers':number,
            }
            
                # create a dictionary
            headers = {
                    'authorization': "BHDFHdnBtRXSrBTvu6hYEHPoocj3TwmCk7hQlL1Y31AnHYwE78DWDpbtbV07",
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache"
            }
                # make a post request
            response = requests.request("POST",url,data = my_data,headers=headers)
            print(response,'akalskdalsd')
            
            messages.success(request,"successfully added")
            return redirect('admin_add_police_officers')
        else:
            messages.error(request,"invalid details ,try again")
            return redirect('admin_add_police_officers')
    return render(request,"admin/admin-add-police-officers.html",{'x':s2})



def admin_view_crime_records(request,id):
    
    s2=CriminalModel.objects.get(pk=id)
    print(s2)
    s1=CrimeModel.objects.filter(crime_aadhar= s2.criminal_aadhar ).order_by('-id')
    if request.method == "POST" and request.FILES["photo"]:
        aadhar=request.POST.get("aadhar")
        crimetype=request.POST.get("crimetype")
        description=request.POST.get("description")
        photo=request.FILES["photo"]
        print(aadhar,description,crimetype,photo)
        

        # s1=CrimeModel.objects.get(crime_aadhar=aadhar,crime_type=crimetype,crime_desc=description)
        # s1.save()

    # x4=CrimeModel.objects.get(crime)
    # x=CrimeModel.objects.get(pk=id)
    
    return render(request,"admin/admin-crime-records.html",{'s':s1,'y':s2})
    
    


def admin_criminal_records(request,id):

    x=CriminalModel.objects.get(pk=id)
    if request.method == "POST":
        
        aadhar=request.POST.get("aadhar")
        # photo=request.FILES["photo"]
        name=request.POST.get("name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        city=request.POST.get("city")
        
        x.criminal_aadhar = aadhar
        # x.criminal_profile = photo
        x.criminal_name = name
        x.criminal_email = email
        x.criminal_contact = contact
        x.criminal_city = city
        
        x.save()
        if x:
            messages.success(request,"admin_criminal_records")
        else:
            messages.error(request,'admin_criminal_records')
            return redirect("admin_manage_criminals")
    
    return render(request,"admin/admin-criminal-records.html",{'x':x})

def admin_edit_police_officers_details(request,id):
    s1=PoliceOfficerModel.objects.get(pk=id)
    
    if request.method=="POST":
    #  and request.FILES["photo"]:
        branchname=request.POST.get("branchname")
        badgeno=request.POST.get("badgeno")
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        contact=request.POST.get("contact")
        # photo=request.FILES["photo"]
        # photo=request.FILES["photo"]
        s1.officer_station = branchname
        s1.officer_badgeno = badgeno
        s1.officer_name = name
        s1.officer_email = email
        s1.officer_number = contact
        s1.officer_password = password
        # s1.officer_profile = photo

        s1.save()
        if s1:
            messages.success(request,"Update Succesfully")
        else:
            messages.error(request,"No changes Found")
            return redirect("admin_manage_police_officers")

    return render(request,"admin/admin-edit-police-officers-details.html",{'i':s1})

def admin_edit_station_details(request,id):
    s1=PoliceStationModel.objects.get(pk=id)
    
    if request.method=="POST":
        state=request.POST.get("state")
        city=request.POST.get("city")
        name=request.POST.get("name")
        locality=request.POST.get("locality")
        areacode=request.POST.get("areacode")
        contact=request.POST.get("contact")
        # photo=request.FILES["photo"]
        s1.station_city = city
        s1.station_state = state
        s1.station_name = name
        s1.station_locality = locality
        s1.station_areacode = areacode
        s1.station_contact = contact

        s1.save()
        if s1:
            messages.success(request,"Succesflly Updated")
                

        else:
            messages.error(request,"No changes detected")
            return redirect("admin_manage_police_stations")
    return render(request,"admin/admin-edit-station-details.html",{'i':s1})

def admin_manage_criminals(request):
    x4=CriminalModel.objects.all().order_by('-id')
    return render(request,"admin/admin-manage-criminals.html",{
        'x4':x4
    })
    # return render(request,"admin/admin-manage-criminals.html")

def admin_manage_crime(request):
    x4=CriminalModel.objects.all().order_by('-id')
    return render(request,"admin/admin-manage-crime.html",{
        'x4':x4})
    # return render(request,"admin/admin-manage-crime.html")

def admin_manage_police_officers(request):
    x2=PoliceStationModel.objects.all().order_by('-id')
    return render(request,"admin/admin-manage-police-officers.html",{
        'x2':x2
    })
    # return render(request,"admin/admin-manage-police-officers.html")

def admin_manage_police_stations(request):
    police_stations=PoliceStationModel.objects.all().order_by('-id')
    return render(request,"admin/admin-manage-police-stations.html",{
        'police_stations':police_stations
    })

def admin_view_police_officers_list(request,id):
    s2=PoliceStationModel.objects.get(pk=id)
    print(s2)
    s1=PoliceOfficerModel.objects.filter( officer_station = s2.station_name )
    if request.method == "POST" and request.FILES["photo"]:
        photo=request.FILES["photo"]
        badgeno=request.POST.get("badgeno")
        name=request.POST.get("name")
        email=request.POST.get("email")
        number=request.POST.get("number")
        print(photo,badgeno,name,email,number)
    
    return render(request,"admin/admin-view-police-officers-list.html",{'x':s1,'y':s2})

def admin_view_criminals_list(request):
    s1=CriminalModel.objects.all().order_by('-id')
    return render(request,"admin/admin-view-criminals-list.html",{
        'x':s1
    })
    # return render(request,"admin/admin-view-criminals-list.html")


def officer_delete(request,id):
    
    member = PoliceOfficerModel.objects.get( pk =id)
    member.delete()
    messages.info(request,"Deleted Successfully")
    return redirect('admin_manage_police_officers')

def officer_delete1(request,id):
    
    member = CriminalModel.objects.get( pk = id)
    member.delete()
    messages.info(request,"Deleted Successfully")
    return redirect('admin_index')

def officer_delete2(request,id):
    
    member = CrimeModel.objects.get( pk = id)
    member.delete()
    messages.info(request,"Deleted Successfully")
    return redirect('admin_manage_crime')