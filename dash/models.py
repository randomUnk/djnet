from django.db import models

# Create your models here.
class ProjectDetails(models.Model):
    vehicle_type    = models.CharField(max_length=40) 
    brand           = models.CharField(max_length=40)
    model           = models.CharField(max_length=40)
    engine_type     = models.CharField(max_length=40)
    make_year       = models.CharField(max_length=40)
    mileage_range   = models.CharField(max_length=40)
    region          = models.CharField(max_length=40)
    mileage         = models.CharField(max_length=40)
                
    oil_filter                  = models.CharField(max_length=40)
    washer_plug_drain           = models.CharField(max_length=40)
    Wheel_alignment_and_balance = models.CharField(max_length=40)
    Fuel_filter                 = models.CharField(max_length=40)
    Break_fluid                 = models.CharField(max_length=40)
    Transmission_Fluid          = models.CharField(max_length=40)
    clutch                      = models.CharField(max_length=40)

    Engine_Oil                  = models.CharField(max_length=40)
    Dust_and_pollen_filter      = models.CharField(max_length=40)
    Air_clean_filter            = models.CharField(max_length=40)
    Spark_plug                  = models.CharField(max_length=40)
    Break_and_Clutch_oil        = models.CharField(max_length=40)
    Break_Pads                  = models.CharField(max_length=40)
    Coolant                     = models.CharField(max_length=40)
    # img                         = models.ImageField(upload_to='media')
    

    