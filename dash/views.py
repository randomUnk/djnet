from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ProjectDetails as ProjectDetails
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
# Create your views here.

# @login_required
def index(request):
    mem1 = ProjectDetails.objects.all()
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request,'sign_in.html')
    
def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return render(request,'sign_in.html')
    
def table(request):
    if request.user.is_authenticated:
        return render(request,'table.html')
    else:
        return render(request,'sign_in.html')
    
def blank(request):
    if request.user.is_authenticated:
        return render(request,'blank.html')
    else:
        return render(request,'sign_in.html')
    
def test(request):
    print('ado wede goda')
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request,'sign_in.html')
    
def data_entry(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST['VehicleDetails']=='1':
                vehicle_type    = request.POST['vehicleType']
                brand           = request.POST['vehicleBrand']
                model           = request.POST['vehicleModel']
                engine_type     = request.POST['engineType']
                make_year       = request.POST['makeYear']
                mileage_range   = request.POST['mileage_range']
                region          = request.POST['region']
                mileage         = request.POST['Mileage']
                # img             = request.POST['file']
                
                oil_filter                  = request.POST.getlist('formCheck-1')
                washer_plug_drain           = request.POST.getlist('formCheck-3')
                Wheel_alignment_and_balance = request.POST.getlist('formCheck-5')
                Fuel_filter                 = request.POST.getlist('formCheck-7')
                Break_fluid                 = request.POST.getlist('formCheck-9')
                Transmission_Fluid          = request.POST.getlist('formCheck-11')
                clutch                      = request.POST.getlist('formCheck-13')
                
                Engine_Oil                  = request.POST.getlist('formCheck-2')
                Dust_and_pollen_filter      = request.POST.getlist('formCheck-4')
                Air_clean_filter            = request.POST.getlist('formCheck-6')
                Spark_plug                  = request.POST.getlist('formCheck-8')
                Break_and_Clutch_oil        = request.POST.getlist('formCheck-10')
                Break_Pads                  = request.POST.getlist('formCheck-12')
                Coolant                     = request.POST.getlist('formCheck-14')
                
                # print(vehicle_type,brand,model,engine_type,make_year,mileage_range,region,mileage)

                # ticks = (oil_filter,
                #         washer_plug_drain,
                #         Wheel_alignment_and_balance,
                #         Fuel_filter,
                #         Break_fluid,
                #         Transmission_Fluid,
                #         clutch,
                #         Engine_Oil,
                #         Dust_and_pollen_filter,
                #         Air_clean_filter,
                #         Spark_plug,
                #         Break_and_Clutch_oil,
                #         Break_Pads,
                #         Coolant)
                
                # for i in ticks:
                #     i if i else i.append(0) 
                    
                # print(ticks[0])
                

                oil_filter                  if oil_filter                   else oil_filter.append(0)
                washer_plug_drain           if washer_plug_drain            else washer_plug_drain.append(0)
                Wheel_alignment_and_balance if Wheel_alignment_and_balance  else Wheel_alignment_and_balance.append(0)
                Fuel_filter                 if Fuel_filter                  else Fuel_filter.append(0)
                Break_fluid                 if Break_fluid                  else Break_fluid.append(0)
                Transmission_Fluid          if Transmission_Fluid           else Transmission_Fluid.append(0)
                clutch                      if clutch                       else clutch.append(0)
                Engine_Oil                  if Engine_Oil                   else Engine_Oil.append(0)
                Dust_and_pollen_filter      if Dust_and_pollen_filter       else Dust_and_pollen_filter.append(0)
                Air_clean_filter            if Air_clean_filter             else Air_clean_filter.append(0)
                Spark_plug                  if Spark_plug                   else Spark_plug.append(0)
                Break_and_Clutch_oil        if Break_and_Clutch_oil         else Break_and_Clutch_oil.append(0)
                Break_Pads                  if Break_Pads                   else Break_Pads.append(0)
                Coolant                     if Coolant                      else Coolant.append(0)
                
                
                # print(oil_filter[0],
                #       washer_plug_drain[0], Wheel_alignment_and_balance[0], Fuel_filter[0],Break_fluid[0], Transmission_Fluid[0], clutch[0], Engine_Oil[0], Dust_and_pollen_filter[0], Air_clean_filter[0], Spark_plug[0], Break_and_Clutch_oil[0], Break_Pads[0], Coolant[0])
                
                Details = ProjectDetails(
                    vehicle_type = vehicle_type,    
                    brand = brand,           
                    model = model,           
                    engine_type = engine_type,     
                    make_year = make_year,       
                    mileage_range = mileage_range,   
                    region = region,          
                    mileage = mileage,         
                                
                    oil_filter                  = oil_filter[0],
                    washer_plug_drain           = washer_plug_drain[0],
                    Wheel_alignment_and_balance = Wheel_alignment_and_balance[0],
                    Fuel_filter                 = Fuel_filter[0],
                    Break_fluid                 = Break_fluid[0],
                    Transmission_Fluid          = Transmission_Fluid[0],
                    clutch                      = clutch[0],

                    Engine_Oil                  = Engine_Oil[0],
                    Dust_and_pollen_filter      = Dust_and_pollen_filter[0],
                    Air_clean_filter            = Air_clean_filter[0],
                    Spark_plug                  = Spark_plug[0],
                    Break_and_Clutch_oil        = Break_and_Clutch_oil[0],
                    Break_Pads                  = Break_Pads[0],
                    Coolant                     = Coolant[0],
                    # img                         = img,
                )
                Details.save()
                
        return render(request,'dataentry.html')
    else:
        return render(request,'sign_in.html')
         
def logout(request):
    auth.logout(request)
    return render(request,'sign_in.html')
