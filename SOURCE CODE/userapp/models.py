from django.db import models

# Create your models here.
class Temp_imgModel(models.Model):
    
    criminal_img=models.ImageField(upload_to='images/',null=True)
    class Meta:
        db_table='temp_images'