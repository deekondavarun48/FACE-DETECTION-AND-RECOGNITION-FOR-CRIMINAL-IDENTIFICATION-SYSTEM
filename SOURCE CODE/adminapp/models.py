from asyncio.windows_events import NULL
from django.db import models

# Create your models here.


# add-police-stations-models
class PoliceStationModel(models.Model):
    station_state=models.CharField(max_length=100,null=True)
    station_city=models.CharField(max_length=100,null=True)
    station_name=models.CharField(max_length=100,null=True)
    station_locality=models.CharField(max_length=100,null=True)
    station_areacode=models.CharField(max_length=10,null=True)
    station_contact=models.CharField(max_length=12,null=True)

    class Meta:
        db_table='police_station_details'

class PoliceOfficerModel(models.Model):
    officer_station=models.CharField(max_length=100,null=True)
    officer_badgeno=models.CharField(max_length=100,null=True)
    officer_name=models.CharField(max_length=100,null=True)
    officer_email=models.EmailField(max_length=100,null=True)
    officer_number=models.CharField(max_length=100,null=True)
    officer_password=models.CharField(max_length=100,null=True)
    officer_profile=models.ImageField(upload_to='images/',null=True)
    
   
    class Meta:
        db_table='police_officers_details'



class CrimeModel(models.Model):
    crime_aadhar=models.CharField(max_length=100,null=True)
    crime_type=models.CharField(max_length=100,null=True)
    crime_desc=models.CharField(max_length=100,null=True)
    crime_added_date=models.DateField(null=True)
    #hash value columns
    aadhar_blk=models.CharField(max_length=100,null=True)
    type_blk=models.CharField(max_length=100,null=True)
    desc_blk=models.CharField(max_length=100,null=True)
    date_blk=models.CharField(max_length=100,null=True)

    class Meta:
        db_table='crime_details'


class CriminalModel(models.Model):
    criminal_aadhar=models.CharField(max_length=100,null=True)
    criminal_name=models.CharField(max_length=100,null=True)
    criminal_email=models.EmailField(max_length=100,null=True)
    criminal_contact=models.CharField(max_length=100,null=True)
    criminal_city=models.CharField(max_length=100,null=True)
    criminal_profile=models.ImageField(upload_to='images/',null=True)
    
    criminal_crime_date=models.DateField(null=True)
    #hash value columns
    aadhar_block=models.CharField(max_length=100,null=True)
    name_block=models.CharField(max_length=100,null=True)
    email_block=models.CharField(max_length=100,null=True)
    contact_block=models.CharField(max_length=100,null=True)
    city_block=models.CharField(max_length=100,null=True)
    profile_block=models.CharField(max_length=100,null=True)
    date_block=models.CharField(max_length=100,null=True)



    class Meta:
        db_table='criminals_details'
 