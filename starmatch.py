#!/usr/bin/env python3
import sys
import numpy as np
from starmatch_lib import *
from FitsView_gui import *
from PyQt5.QtWidgets import QApplication

import matplotlib.pyplot as plt

ratio=sys.argv[1]    # scale = field (x or y) size file to size reference field: sofi=ref; scale hawki/sofi = 7.5/5
file_name_1=sys.argv[2]
file_name_2=sys.argv[3]


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
sm.fieldStarsRatio=ratio
sm.nb_use=400
sm.pixscale=2.71
sm.ref_xr=x_ref
sm.ref_yr=y_ref
sm.ref_mr=m_ref
sm.field_xr=x_file
sm.field_yr=y_file
sm.field_mr=m_file

sm.go()




xx1=sm.trainglesMatch_ref_x
yy1=sm.trainglesMatch_ref_y
xx2=sm.trainglesMatch_field_x
yy2=sm.trainglesMatch_field_y

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
