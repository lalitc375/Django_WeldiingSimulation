from django.http import *
from django.template import *
from django.shortcuts import *
from .models import *
from django.core.mail import send_mail
from django.utils import timezone
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
import json
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.utils.encoding import force_text
from djangular import *
from django.views.generic import View
# Create your views here
from demoapp.tasks import *
def index(request):
    if "username" in request.session:
        if "type" in request.session:
            if(request.session['type']=='Basic'):
                return HttpResponseRedirect('/webinterface/basicinput')
            elif(request.session['type']=='Advance'):
                return HttpResponseRedirect('/webinterface/basicinput')
        else:
            request.session.flush()
            return render(request, 'webinterface/index.html')
    else:
        return render(request, 'webinterface/index.html')

def forgotPassword(request):
    if "username" in request.session:
        if "type" in request.session:
            if(request.session['type']=='Basic'):
                return HttpResponseRedirect('/webinterface/basicinput')
            elif(request.session['type']=='Advance'):
                return HttpResponseRedirect('/webinterface/basicinput')
        else:
            request.session.flush()
    else:
        return render(request, 'webinterface/forgotPassword.html')

class requestPassword(View):
    def post(self,request):
        Array=json.loads(request.body)
        response={}
        try:
            count=DbUser.objects.filter(email=Array['email']).count()

            if(count==1):
                user=DbUser.objects.get(email=Array['email'])
                try:
                    send_mail('Password Recovery','Your Password For Stir Welding Account is <b>'+str(user.password)+'</b>','lalitc375@gmail.com',[Array['email']])
                    response['status']=1
                except:
                    response['status']=2
            else:
                response['status']=3
        except:
            response['status']=3
        return HttpResponse(json.dumps(response))





def signup(request):
    if "username" in request.session:
        if "type" in request.session:
            if(request.session['type']=='Basic'):
                return HttpResponseRedirect('/webinterface/basicinput')
            elif(request.session['type']=='Advance'):
                return HttpResponseRedirect('/webinterface/basicinput')
        else:
            request.session.flush()
    else:
        return render(request, 'webinterface/signup.html')


def login(request):

    if request.method == 'POST':

        count=DbUser.objects.filter(email=request.POST['useremail'],password = request.POST['password']).count()


        if (count==1) :
            user=DbUser.objects.get(email=request.POST['useremail'],password = request.POST['password'])
            if (user.permission==1):
                request.session['username']=user.name
                request.session['type']=user.type
                request.session['email']=user.email
            else:
                return render(request, 'webinterface/index.html',{'error_message':'Admin Approval Pending'})

        else:
            return render(request, 'webinterface/index.html',{'error_message':'Incorrect Email Address And UserName'})
        if(user.type=='Basic'):
                return HttpResponseRedirect('/webinterface/basicinput')
        elif (user.type=='Advance'):
                return HttpResponseRedirect('/webinterface/advanceinput')


    else:
         return HttpResponseRedirect('/webinterface/index')

def basicinput(request):
    if "username" in request.session:
        if (request.session['type']=='Basic'):
            return render(request,'webinterface/input.html',{'username':request.session['username']})
        elif(request.session['type']=='Advance'):
            return HttpResponseRedirect('/webinterface/advanceinput')
        else:
            return HttpResponseRedirect('/webinterface/logout')
    else:
        return HttpResponseRedirect('/webinterface/index')


def advanceinput(request):
    if "username" in request.session:
        if (request.session['type']=='Advance'):
            return render(request,'webinterface/advinput.html',{'username':request.session['username']})
        elif(request.session['type']=='Basic'):
            return HttpResponseRedirect('/webinterface/basicinput')
        else:
            return HttpResponseRedirect('/webinterface/logout')
    else:
        return HttpResponseRedirect('/webinterface/index')

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/webinterface/index')

class signUpData(View):
    def post(self,request):
        Array=json.loads(request.body)
        count=DbUser.objects.filter(email=Array['email']).count()
        response={}
        if (count==0):
            user=DbUser()
            user.name=Array['name']
            user.email=Array['email']
            user.address=Array['address']
            user.company=Array['company']
            user.designation=Array['designation']
            user.phone_no=Array["ph_no"]
            user.permission=0
            user.profession=Array['profession']
            user.type=Array['type1']
            user.password=Array['password']
            try:
                user.save()
                response['status']=0
            except:
                response['status']=1
        else:
            response['status']=2
        return HttpResponse(json.dumps(response))



class basicInputData(View):
    def post(self, request):
        Array=json.loads(request.body)
        data=inputData()
        data.email=request.session['email']
        data.recordCreatedOn=timezone.now()
        data.workpiece_material_advancing_side=Array['advancingMaterial']
        data.workpiece_material_retreating_side=Array['advancingMaterial']
        data.tool_material=Array['toolMaterial']
        data.no_monitoring_locations=Array['noMonLoc']
        data.axial_pressure=Array['axialPressure']
        data.tilt_angle=Array['tiltAngle']
        data.pin_length=Array['pinLength']
        data.pin_radius_root=Array['pinRadiusRoot']
        data.pin_radius_tip=Array['pinRadiusTip']
        data.shoulder_radius=Array['shoulderRadius']
        data.ylocation_monitoring_locations=Array['monYLocString']
        data.zlocation_monitoring_locations=Array['monZLocString']
        data.rotational_velocity=Array['toolRpm']
        data.welding_velocity=Array['feedRate']
        data.thread_pitch=Array['threadPitch']
        data.length_zzones=str(Array['thicknessWorkpiece'])

        try:
            data.save()
            Array['id']=data.id
            Array['retreatingMaterial']=data.workpiece_material_retreating_side
            Array['email']=request.session['email']
            Array['noXZone']=data.number_xzone
            Array['noYZone']=data.number_yzone
            Array['noZZone']=data.number_zzone
            Array['XLocString']=data.length_xzones
            Array['YLocString']=data.length_yzones
            Array['ZLocString']=data.length_zzones
            Array['XControlString']=data.no_control_volume_xzone
            Array['YControlString']=data.no_control_volume_yzone
            Array['ZControlString']=data.no_control_volume_zzone
            Array['XEpoConString']=data.exponent_locate_control_volume_xzone
            Array['YEpoConString']=data.exponent_locate_control_volume_yzone
            Array['ZEpoConString']=data.exponent_locate_control_volume_zzone
            Array['maxIteration']=data.max_iterations
            Array['underRelaxationPressure']=data.underrelaxation_pressure
            Array['underRelaxationTemp']=data.underrelaxation_temperature
            Array['underRelaxationUVelocity']=data.underrelaxation_u_velocity
            Array['underRelaxationVVelocity']= data.underrelaxation_v_velocity
            Array['underRelaxationWVelocity']= data.underrelaxation_w_velocity
            Array['tempBottom']=data.temp_bottom_face
            Array['tempNorth']=data.temp_north_face
            Array['tempEast']=data.temp_east_face
            Array['tempWest']=data.temp_west_face
            Array['tempSouth']=data.temp_south_face
            Array['heatCoffBottom']=data.heat_transfer_coff_bottom_face
            Array['heatCoffEast']=data.heat_transfer_coff_east_face
            Array['heatCoffNorth']= data.heat_transfer_coff_north_face
            Array['heatCoffSouth']=data.heat_transfer_coff_south_face
            Array['heatCoffTop']=data.heat_transfer_coff_top_face
            Array['heatCoffWest']=data.heat_transfer_coff_west_face
            Array['fricCoff']=data.adjustable_parameter_friction_coefficient
            Array['slip']=data.adjustable_parameter_slip
            Array['adjViscousDiss']=data.adjustable_parameter_viscous_dissipation

            Array['ambientTemp']=data.ambient_temp
            Array['preHeatTemp']=data.preheat_temp
            Array['convFactMechHeat']=data.conv_factor_mech_heat
            Array['fracEnterWork']=data.fraction_heatenergy_entering_workpiece
            Array['xLocTool']=data.x_location_tool
            Array['yLocTool']=data.y_location_tool
            result=exefsw.delay(Array)
            response={}
            response['status']=1;
            response['id']=Array['id']
            return HttpResponse(json.dumps(response))

        except:
            response={}
            response['status']=0;
            return HttpResponse(json.dumps(response))

class advanceInputData(View):
    def post(self, request):
        Array=json.loads(request.body)
        data=inputData()
        data.email=request.session['email']
        data.recordCreatedOn=timezone.now()
        data.workpiece_material_advancing_side=Array['advancingMaterial']
        data.workpiece_material_retreating_side=Array['retreatingMaterial']
        data.tool_material=Array['toolMaterial']
        data.no_monitoring_locations=Array['noMonLoc']
        data.axial_pressure=Array['axialPressure']
        data.tilt_angle=Array['tiltAngle']
        data.pin_length=Array['pinLength']
        data.pin_radius_root=Array['pinRadiusRoot']
        data.pin_radius_tip=Array['pinRadiusTip']
        data.shoulder_radius=Array['shoulderRadius']
        data.ylocation_monitoring_locations=Array['monYLocString']
        data.zlocation_monitoring_locations=Array['monZLocString']
        data.rotational_velocity=Array['toolRpm']
        data.welding_velocity=Array['feedRate']
        data.x_location_tool=Array['xLocTool']
        data.y_location_tool=Array['yLocTool']
        data.thread_pitch=Array['threadPitch']

        data.number_xzone=Array['noXZone']
        data.number_yzone=Array['noYZone']
        data.number_zzone=Array['noZZone']
        data.length_xzones=Array['XLocString']
        data.length_yzones=Array['YLocString']
        data.length_zzones=Array['ZLocString']
        data.no_control_volume_xzone=Array['XControlString']
        data.no_control_volume_yzone=Array['YControlString']
        data.no_control_volume_zzone=Array['ZControlString']
        data.exponent_locate_control_volume_xzone=Array['XEpoConString']
        data.exponent_locate_control_volume_yzone=Array['YEpoConString']
        data.exponent_locate_control_volume_zzone=Array['ZEpoConString']
        data.max_iterations=Array['maxIteration']
        data.underrelaxation_pressure=Array['underRelaxationPressure']
        data.underrelaxation_temperature=Array['underRelaxationTemp']
        data.underrelaxation_u_velocity=Array['underRelaxationUVelocity']
        data.underrelaxation_v_velocity=Array['underRelaxationVVelocity']
        data.underrelaxation_w_velocity=Array['underRelaxationWVelocity']
        data.temp_bottom_face=Array['tempBottom']
        data.temp_north_face=Array['tempNorth']
        data.temp_east_face=Array['tempEast']
        data.temp_west_face=Array['tempWest']
        data.temp_south_face=Array['tempSouth']
        data.heat_transfer_coff_bottom_face=Array['heatCoffBottom']
        data.heat_transfer_coff_east_face=Array['heatCoffEast']
        data.heat_transfer_coff_north_face=Array['heatCoffNorth']
        data.heat_transfer_coff_south_face=Array['heatCoffSouth']
        data.heat_transfer_coff_top_face=Array['heatCoffTop']
        data.heat_transfer_coff_west_face=Array['heatCoffWest']
        data.adjustable_parameter_friction_coefficient=Array['fricCoff']
        data.adjustable_parameter_slip=Array['slip']
        data.adjustable_parameter_viscous_dissipation=Array['adjViscousDiss']

        data.ambient_temp=Array['ambientTemp']
        data.preheat_temp=Array['preHeatTemp']
        data.conv_factor_mech_heat=Array['convFactMechHeat']
        data.fraction_heatenergy_entering_workpiece=Array['fracEnterWork']
        try:
            data.save()
            Array['id']=data.id
            Array['email']=request.session['email']
            result=exefsw.delay(Array)
            response={}
            response['status']=1;
            response['id']=Array['id']
            return HttpResponse(json.dumps(response))

        except:
            response={}
            response['status']=0;
            return HttpResponse(json.dumps(response))

def updateProfile(request):
    if "username" in request.session:
        if (request.session['type']=='Basic' or request.session['type']=='Advance'):
            user=DbUser.objects.get(email=request.session['email'])
            return render(request,'webinterface/updateProfile.html',{'address':user.address,'company':user.company,'designation':user.designation,\
                                                                     'profession':user.profession,'name':user.name,'contact':user.phone_no\

                                                                     });

        else:
            return HttpResponseRedirect('/webinterface/logout')
    else:
        return HttpResponseRedirect('/webinterface/index')

class updateProfileData(View):
    def post(self,request):
        print ('lalit');
        Array=json.loads(request.body)
        response={}
        try:
            DbUser.objects.filter(email=request.session['email']).update(name=Array['name'],company=Array['company'],designation=Array['designation']\
                                                                     ,profession=Array['profession'],address=Array['address'],phone_no=Array['ph_no'])
            response['status']=0;
        except:
            response['status']=1;

        return HttpResponse(json.dumps(response))






