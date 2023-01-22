#!/usr/bin/env python3
import sys
import numpy as np
from starmatch_lib import *
from FitsView_gui import *
from PyQt5.QtWidgets import QApplication

import matplotlib.pyplot as plt


file_name_1=sys.argv[1]
file_name_2=sys.argv[2]


if ".ap" in file_name_1:
   dane,bledy=loadap(file_name_1)
elif ".out" in file_name_1:
   dane=loadout(file_name_1)
else: dane=load_file(0,file_name_1)   

x_ref=dane[1]
y_ref=dane[2]
m_ref=dane[3]


if ".ap" in file_name_2:
   dane,bledy=loadap(file_name_2)
elif ".out" in file_name_2:
   dane=loadout(file_name_2)
else: dane=load_file(0,file_name_2)   

x_file=dane[1]
y_file=dane[2]
m_file=dane[3]



sm=StarMatch()
sm.loud=True
sm.nb_use=400
sm.pixscale=0.3680           # HAWKI
sm.fieldStarsRatio=0.58    # HAWKI
sm.ref_xr=x_ref
sm.ref_yr=y_ref
sm.ref_mr=m_ref
sm.field_xr=x_file
sm.field_yr=y_file
sm.field_mr=m_file

sm.go()
print(sm.mssg)
print(sm.p_fr_x)
print(sm.p_fr_y)
print(sm.p_rf_x)
print(sm.p_rf_y)


# transformacje:    x = p[0] + p[1] * x + p[2] * y + p[3] * x*y + p[4] * x*x + p[5] * y*y
# transformacje:    y = p[0] + p[1] * x + p[2] * y + p[3] * x*y + p[4] * x*x + p[5] * y*y

# sm.p_fr_x  - x field -> reference
# sm.p_fr_y  - y field -> reference

# sm.p_rf_x  - x reference -> field
# sm.p_rf_y  - x reference -> field

# sm.ref_match_x            - lista gwiazd zmatchowanych featureami 
# m.field_match_x
# sm.trainglesMatch_ref_x   - lista gwiazd zmatchowanych trujkatami
# sm.trainglesFail_ref_x    - lista gwiazd odrzucona przez trujkaty

#xx1=sm.trainglesMatch_ref_x
#yy1=sm.trainglesMatch_ref_y
xx2=sm.trainglesMatch_field_x
yy2=sm.trainglesMatch_field_y

x=numpy.array(sm.trainglesMatch_field_x)
y=numpy.array(sm.trainglesMatch_field_y)

xx1,yy1= coo_trans(x,y,sm.p_fr_x,sm.p_fr_y)

#xx1=sm.p_fr_x[0]+sm.p_fr_x[1]*x+sm.p_fr_x[2]*y+sm.p_fr_x[3]*x*y+sm.p_fr_x[4]*x*x+sm.p_fr_x[5]*y*y
#yy1=sm.p_fr_y[0]+sm.p_fr_y[1]*x+sm.p_fr_y[2]*y+sm.p_fr_y[3]*x*y+sm.p_fr_y[4]*x*x+sm.p_fr_y[5]*y*y



    



#xx1=sm.trainglesFail_ref_x
#yy1=sm.trainglesFail_ref_y
#xx2=sm.trainglesFail_field_x
#yy2=sm.trainglesFail_field_y


#dist = CountDist(x_ref,y_ref)

#plt.hist(dist,1000)
#plt.show()



app = QApplication(sys.argv)
cfg=[] 
FV_window1 = FitsView(cfg) # run the Pymage Widget class 
FV_window1.fname=file_name_1.split(".")[0]+".fits" # define FITS file name 
FV_window1.newFits() # execute new fits 
FV_window1.ext_x=[xx1] 
FV_window1.ext_y=[yy1] 
FV_window1.show() 
FV_window1.update() 

FV_window2 = FitsView(cfg) # run the Pymage Widget class 
FV_window2.fname=file_name_2.split(".")[0]+".fits" # define FITS file name 
FV_window2.newFits() # execute new fits 
FV_window2.ext_x=[xx2] 
FV_window2.ext_y=[yy2] 
FV_window2.show() 
FV_window2.update() 

sys.exit(app.exec_())
