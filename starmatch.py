#!/usr/bin/env python3
import sys
import numpy as np
from FitsView_gui import *
from PyQt5.QtWidgets import QApplication

file_name_1=sys.argv[1]
file_name_2=sys.argv[2]

x_ref=[]
y_ref=[]
m_ref=[]

with open(file_name_1, 'r') as plik:
   i=0
   for line in plik:
      if i>2 and len(line.split())>1: 
         x_ref.append(float(line.split()[1]))
         y_ref.append(float(line.split()[2]))
         m_ref.append(float(line.split()[3]))
      i=i+1


x_file=[]
y_file=[]
m_file=[]

with open(file_name_2, 'r') as plik:
   i=0
   for line in plik:
      if i>2 and len(line.split())>1: 
         x_file.append(float(line.split()[1]))
         y_file.append(float(line.split()[2]))
         m_file.append(float(line.split()[3]))
      i=i+1


m_ref,x_ref,y_ref = zip(*sorted(zip(m_ref, x_ref, y_ref)))  
m_file,x_file,y_file = zip(*sorted(zip(m_file, x_file, y_file))) 

x_ref=np.array(x_ref)
y_ref=np.array(y_ref)
m_ref=np.array(m_ref)

x_file=np.array(x_file)
y_file=np.array(y_file)
m_file=np.array(m_file)





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