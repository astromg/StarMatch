#!/usr/bin/env python3
import sys
import numpy as np
from starmatch_lib import *
from FitsView_gui import *
from PyQt5.QtWidgets import QApplication

import matplotlib.pyplot as plt

scale=sys.argv[1]    # scale = size file to size reference: sofi=ref; scale hawki/sofi = 7.5/5
file_name_1=sys.argv[2]
file_name_2=sys.argv[3]


if ".ap" in file_name_1:
   dane=loadap(file_name_1)
elif ".out" in file_name_1:
   dane=loadout(file_name_1)
else: dane=load_file(0,file_name_1)   

x_ref=dane[1]
y_ref=dane[2]
m_ref=dane[3]

if ".ap" in file_name_2:
   dane=loadap(file_name_2)
elif ".out" in file_name_2:
   dane=loadout(file_name_2)
else: dane=load_file(0,file_name_2)   

x_file=dane[1]
y_file=dane[2]
m_file=dane[3]

dist = StarMatch(x_ref,y_ref,m_ref,x_file,y_file,m_file,scale)

plt.hist(dist,1000)
plt.show()


'''
app = QApplication(sys.argv)
cfg=[] 
FV_window1 = FitsView(cfg) # run the Pymage Widget class 
FV_window1.fname="SMC24_131127_1_K.fits" # define FITS file name 
FV_window1.newFits() # execute new fits 
FV_window1.ext_x=[x_ref[wa],x_ref[wb],x_ref[wc]] 
FV_window1.ext_y=[y_ref[wa],y_ref[wb],y_ref[wc]] 
FV_window1.ext_l=["raz","dwa","trzy"] 
FV_window1.show() 
FV_window1.update() 

FV_window2 = FitsView(cfg) # run the Pymage Widget class 
FV_window2.fname="SMC24_181228_1_K.fits" # define FITS file name 
FV_window2.newFits() # execute new fits 
FV_window2.ext_x=[x_file[t1],x_file[t2],x_file[i_tmp[n]]] 
FV_window2.ext_y=[y_file[t1],y_file[t2],y_file[i_tmp[n]]] 
FV_window2.ext_l=["raz","dwa","trzy"] 
FV_window2.show() 
FV_window1.update() 

sys.exit(app.exec_())
'''