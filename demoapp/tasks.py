from __future__ import absolute_import

from celery import shared_task
import os
from django.core.mail import EmailMessage,send_mail


@shared_task
def add(x, y):
    t=0
    for z in range(0,100000000,1):
        t=t+x+y
    return t


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def exefsw(Array):

    os.system('mkdir '+str(Array['id']))
    try:
        send_mail('Data Submitted For Stir welding','Your Request for stir welding submission is submitted .Your processing data id is '+str(Array['id']),'lalitc375@gmail.com',[Array['email']])
    except:
        pass
    print('Directory Created')
    os.chdir(str(Array['id']))
    print('Directory Changed')


    fo = open('input.txt', "wb")
    fo.write('!-----Material selection------------------------------------------------------\n')
    fo.write('!1=AA6061,2=1018Steel,3=304L SS,6=Tungsten, 7=Cu-0.9Cr-0.12Zr, 8=Ti-6Al-4V,11=AA2024,9-WE43 Mg\n')
    fo.write(str(Array['advancingMaterial'])+'\t !Workpiece material on advancing side \n')
    fo.write(str(Array['toolMaterial'])+'\t!tool material\n')
    fo.write(str(Array['retreatingMaterial'])+'\t!Workpiece material on retreating side \n')
    fo.write('!-----Tool geometry-----------------------------------------------------------\n')
    fo.write(str(Array['shoulderRadius'])+'\t!shoulder radius(cm)\n')
    fo.write(str(Array['pinRadiusRoot'])+'\t !pin radius at shoulder (cm)\n')
    fo.write(str(Array['pinRadiusTip'])+'\t!pin radius at the tip (cm)\n')
    fo.write(str(Array['pinLength'])+'\t!pin length (cm)\n')
    fo.write(str(Array['threadPitch'])+'\t!thread pitch (cm) \n')
    fo.write('!-----Welding parameters------------------------------------------------------\n')
    fo.write(str(Array['xLocTool'])+'\t!x-location of the tool\n')
    fo.write(str(Array['yLocTool'])+'\t!y-location of the tool\n')
    fo.write(str(Array['feedRate'])+'\t!welding velocity (cm/sec)\n')
    fo.write(str(Array['toolRpm'])+'\t!rotational velocity (rpm)\n')
    fo.write(str(Array['axialPressure'])+'\t!axial pressure (MPa)\n')
    fo.write(str(Array['tiltAngle'])+'\t!Tilt angle (degrees)\n')
    fo.write('!-----Numerical scheme parameters---------------------------------------------\n')
    fo.write(str(Array['maxIteration'])+'\t!maximum number of iterations\n')
    fo.write(str(Array['underRelaxationUVelocity'])+'\t!underrelaxation for u-velocity\n')
    fo.write(str(Array['underRelaxationVVelocity'])+'\t!underrelaxation for v-velocity\n')
    fo.write(str(Array['underRelaxationWVelocity'])+'\t!underrelaxation for w-velocity\n')
    fo.write(str(Array['underRelaxationPressure'])+'\t!underrelaxation for pressure\n')
    fo.write(str(Array['underRelaxationTemp'])+'\t!underrelaxation for temperature\n')
    fo.write('0                  !index for saving file  (1 = save)\n')
    fo.write('0      	   	   !index for loading file (1 = load)\n')
    fo.write(str(Array['noMonLoc'])+'\t!Number of monitoring locations\n')
    fo.write(str(Array['monYLocString']).replace('@',' ')+'\t!y coordinates of monitoring locations \n')
    fo.write(str(Array['monZLocString']).replace('@',' ')+'\t!z coordinates of monitoring locations \n')
    fo.write('!-----Boundary conditions----------------------------------------------------- \n')
    fo.write(str(Array['heatCoffWest'])+'\t!heat transfer coefficient at west face   (cal/cm2-s-K) \n')
    fo.write(str(Array['heatCoffEast'])+'\t!heat transfer coefficient at east face   (cal/cm2-s-K\n')
    fo.write(str(Array['heatCoffNorth'])+'\t!heat transfer coefficient at north face  (cal/cm2-s-k)\n')
    fo.write(str(Array['heatCoffSouth'])+'\t!heat transfer coefficient at south face  (cal/cm2-s-k)\n')
    fo.write(str(Array['heatCoffTop'])+'\t!heat transfer coefficient at top face    (cal/cm2-s-K) \n')
    fo.write(str(Array['tempWest'])+'\t!temperature at west face   (K) \n')
    fo.write(str(Array['tempEast'])+'\t!temperature at east face   (K)\n')
    fo.write(str(Array['tempNorth'])+'\t!temperature at north face  (K)\n')
    fo.write(str(Array['tempSouth'])+'\t!temperature at south face  (K)\n')
    fo.write(str(Array['tempBottom'])+'\t!temperature at bottom face (K)\n')
    fo.write(str(Array['preHeatTemp'])+'\t!preheat temperature (K)\n')
    fo.write(str(Array['ambientTemp'])+'\t!ambient temperature (K)\n')
    fo.write('!-----Grids------------------------------------------------------------------\n')
    fo.write(str(Array['noXZone'])+'\t!number of x-zones \n')
    fo.write(str(Array['XLocString']).replace('@',' ')+'\t!length of each x-zone (cm)\n')
    fo.write(str(Array['XControlString']).replace('@',' ')+'\t!number of control volumes in each x-zone \n')
    fo.write(str(Array['XEpoConString']).replace('@',' ')+'\t!exponents to locate control volume interfaces \n')
    fo.write(str(Array['noYZone'])+'\t!number of y-zones\n')
    fo.write(str(Array['YLocString']).replace('@',' ')+'\t!length of each y-zone (cm)\n')
    fo.write(str(Array['YControlString']).replace('@',' ')+'\t!number of control volumes in each y-zone \n')
    fo.write(str(Array['YEpoConString']).replace('@',' ')+'\t!exponents to locate control volume interfaces \n')
    fo.write(str(Array['noZZone'])+'\t!number of z-zones\n')
    fo.write(str(Array['ZLocString']).replace('@',' ')+'\t!length of each z-zone (cm)\n')
    fo.write(str(Array['ZControlString']).replace('@',' ')+'\t!number of control volumes in each z-zone \n')
    fo.write(str(Array['ZEpoConString']).replace('@',' ')+'\t!exponents to locate control volume interfaces \n')
    fo.write('!-----Uncertain parameters----------------------------------------------------\n')
    fo.write(str(Array['fricCoff'])+'\t!adjustable parameter for friction coefficient\n')
    fo.write(str(Array['slip'])+'\t!adjustable parameter for slip\n')
    fo.write(str(Array['heatCoffBottom'])+'\t!heat transfer coefficient at bottom (cal/cm2-s-k)\n')
    fo.write(str(Array['convFactMechHeat'])+'\t!conversion factor, mechanical to heat energy\n')
    fo.write(str(Array['adjViscousDiss'])+'\t!adjustable parameter for viscous dissipation\n')
    fo.write(str(Array['fracEnterWork'])+'\t!fraction of heat energy entering the work-piece\n')
    fo.write('1.e9		   !Boundary value for viscosity\n')
    fo.close()

    import numpy as nmp
    import matplotlib.pyplot as pyl
    import scipy.interpolate
    import time



    def find_nearest(array,value):
        idx = (nmp.abs(array-value)).argmin()
        return array[idx]

    if(os.system('../fsw >out1.txt')==0):


        print ("File Uploading Start")
        xii, yii, zii, tii = nmp.genfromtxt(r'tecout', unpack=True,skip_header=4,usecols=(0,1,2,6))

        ziimax=zii.max()
    #print (T)
        x=nmp.array([])
        y=nmp.array([])
        t=nmp.array([])
        i=0
        for Z in zii:
            if(Z==ziimax ):
        #print(Z)
                x=nmp.append(x,xii[i])
                y=nmp.append(y,yii[i])
                t=nmp.append(t,tii[i])
            i=i+1


        N=1000
        print (time.time())
        print ("Griding ")

        xi = nmp.linspace(x.min(), x.max(), N)
        yi = nmp.linspace(y.min(), y.max(), N)
        print (time.time())

        print ("Griding End")
        txyi = scipy.interpolate.griddata((x, y),t, (xi[None,:], yi[:,None]), method='cubic',fill_value=300)

        print (time.time())
        print ("InterPolation Completed")
#print (zi)

        pyl.figure()
        pyl.contour(xi,yi,txyi,[0,400,500,600,700,800,1000])
        CSF=pyl.contourf(xi,yi,txyi,[0,400,500,600,700,800,1000])
        pyl.axis([x.min(),x.max(),y.min(),y.max()])
        CB=pyl.colorbar(CSF,shrink=0.8,extend='both')
        CB.set_ticklabels([r'',r'$<400$',500,600,700,r'$>800$'])
        pyl.xlabel('X Axis')
        pyl.ylabel('Y Axis')
    #pyl.axis()
    #cs=pyl.title('Contour 2',)
        pyl.savefig('contour1.jpg')
        print (time.time())
        print ("1st Figure Plotting Completed")


        x=nmp.array([])
        z=nmp.array([])
        t=nmp.array([])
        i=0

        yiiNearestToZero=find_nearest(yii,0)
        for Y in yii:
            if(Y==yiiNearestToZero):
            #print(Z)
                z=nmp.append(z,zii[i])
                x=nmp.append(x,xii[i])
                t=nmp.append(t,tii[i])
            i=i+1
        N=100
        zi = nmp.linspace(z.min(), z.max(), N)
        xi = nmp.linspace(x.min(), x.max(), N)
#print ("Griding End")
        txzi = scipy.interpolate.griddata((x,z),t, (xi[None,:], zi[:,None]), method='cubic',fill_value=300)
        print ("InterPolation Completed")
#print (zi)
        pyl.figure()
        pyl.contour(xi,zi,txzi,[0,400,500,600,700,800,1000])
        CSF=pyl.contourf(xi,zi,txzi,[0,400,500,600,700,800,1000])
        pyl.axis([x.min(),x.max(),z.min(),z.max()])
        CB=pyl.colorbar(CSF,shrink=0.8,extend='both')
        CB.set_ticklabels([r'',r'$<400$',500,600,700,r'$>800$'])
        pyl.xlabel('X Axis')
        pyl.ylabel('Z Axis')
#pyl.axis()
#cs=pyl.title('Contour 2',)
        pyl.savefig('contour2.jpg')
        print (time.time())
        print ("2nd Figure Plotting Completed")

        y=nmp.array([])
        z=nmp.array([])
        t=nmp.array([])
        i=0

        xiiNearestToZero=find_nearest(xii,0)
        for X in xii:
            if(X==xiiNearestToZero):
        #print(Z)
                z=nmp.append(z,zii[i])
                y=nmp.append(y,yii[i])
                t=nmp.append(t,tii[i])
            i=i+1
        N=100
        zi = nmp.linspace(z.min(), z.max(), N)
        yi = nmp.linspace(y.min(), y.max(), N)

        print (time.time())

#print ("Griding End")
        tyzi = scipy.interpolate.griddata((y,z),t, (yi[None,:], zi[:,None]), method='cubic',fill_value=300)


        print ("InterPolation Completed")
#print (zi)

        pyl.figure()
        pyl.contour(yi,zi,tyzi,[0,400,500,600,700,800,1000])
        CSF=pyl.contourf(yi,zi,tyzi,[0,400,500,600,700,800,1000])
        pyl.axis([y.min(),y.max(),z.min(),z.max()])
        CB=pyl.colorbar(CSF,shrink=0.8,extend='both')
        CB.set_ticklabels([r'',r'$<400$',500,600,700,r'$>800$'])
        pyl.xlabel('Y Axis')
        pyl.ylabel('Z Axis')
#pyl.axis()
#cs=pyl.title('Contour 2',)
        pyl.savefig('contour3.jpg')

        print ("3rd Figure Plotting Completed")
        try:
            email = EmailMessage('Result', 'Attached Contours are result of Query '+str(Array['id']), 'lalitc375@gmail.com',
                [Array['email']])
            email.attach_file('contour1.jpg')
            email.attach_file('contour2.jpg')
            email.attach_file('contour3.jpg')
            email.send()
        except:
            send_mail('Error in Performing Simualtion','There Might be Some Error in input Data query '+Array['id']+'\n Please Try after Some Time.',\
                   'lalitc375@gmail.com',[Array['email']])
    else:
        try:
            send_mail('Error in Performing Simualtion','There Might be Some Error in input Data query '+Array['id']+'\n Please Try after Some Time.',\
                   'lalitc375@gmail.com',[Array['email']])
        except:
            pass

    os.chdir('..')
    return  0
