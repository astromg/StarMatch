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

Go=True
wa=3
wb=4
wc=5
t1=0
t2=1

#wa=4
#wb=5
#wc=6
#t1=2
#t2=7

while Go:

   diff_min=100.
   wa_x=x_ref[wa]
   wa_y=y_ref[wa]
   wa_m=m_ref[wa]
   
   wb_x=x_ref[wb]
   wb_y=y_ref[wb]
   wb_m=m_ref[wb]

   wc_x=x_ref[wc]
   wc_y=y_ref[wc]
   wc_m=m_ref[wc]

   r_ab = ((wa_x-wb_x)**2+((wa_y-wb_y))**2)**0.5
   r_ac = ((wa_x-wc_x)**2+((wa_y-wc_y))**2)**0.5  
   r_ac=r_ac/r_ab


   vector_1 = [wa_x-wb_x,wa_y-wb_y]
   vector_1 = vector_1 / np.linalg.norm(vector_1)
   vector_2 = [wa_x-wc_x,wa_y-wc_y]         
   vector_2 = vector_2 / np.linalg.norm(vector_2) 
   dot_product = np.dot(vector_1, vector_2)
   fi_bc = np.arccos(dot_product)
   #print(fi_bc)

   
   # szukanie 

   t1_x=x_file[t1]
   t1_y=y_file[t1]
   t1_m=m_file[t1]
   
   t2_x=x_file[t2]
   t2_y=y_file[t2]
   t2_m=m_file[t2]


   r_t1t2 = ((t1_x-t2_x)**2+((t1_y-t2_y))**2)**0.5

   vector_1 = [t1_x-t2_x,t1_y-t2_y]
   vector_1 = vector_1 / np.linalg.norm(vector_1)
   vector_2 = np.array([t1_x-x_file,t1_y-y_file])
   vector_2 = list(zip(*vector_2))
   vector_2[t1]=(vector_2[t1+1])    # aby uniknac dzielenia przez 0
   vector_2 = [v2/np.linalg.norm(v2) for v2 in vector_2]
   dot_product = [ np.dot(vector_1, v2) for v2 in vector_2]
   fi_t1t2 = [ np.arccos(dt) for dt in dot_product]
   fi_t1t2 = np.array(fi_t1t2,dtype=float)

   maska1 = fi_t1t2<(fi_bc+0.005)
   maska2 = fi_t1t2>(fi_bc-0.005)
   maska=maska1 & maska2
   i_file = np.arange(0,len(maska),1)

   x_tmp = x_file[maska]
   y_tmp = y_file[maska]
   m_tmp = m_file[maska]
   i_tmp = i_file[maska]

   r_t1t3 = ((t1_x-x_tmp)**2+((t1_y-y_tmp))**2)**0.5
   r_t1t3=r_t1t3/r_t1t2

   roznica = r_t1t3 - r_ac
   roznica2 = roznica*roznica
   
   mdiff=10
   if len(roznica2)>0:
      n = np.argmin(roznica2)
      if diff_min > roznica2[n]: 
         diff_min=roznica2[n]
         #print(roznica[n])
         #print(wa,wb,wc)
         #print(t1,t2,i_tmp[n]) 
         
         m1=m_ref[wa]
         m2=m_ref[wb]
         m3=m_ref[wc]
         dm12=m2-m1
         dm13=m3-m1

         q1=m_file[t1]
         q2=m_file[t2]
         q3=m_file[i_tmp[n]]   
         dq12=q2-q1
         dq13=q3-q1   

         mdiff=((dq12-dm12)**2+(dq13-dm13)**2)**0.5   

   if diff_min>0.005*0.005 or mdiff>0.5:
      t2=t2+1
   
      if t2==t1: 
         t2=t2+1
         
      if t2>5:
         t2=0
         t1=t1+1
         
         if t1==t2: 
            t1=t1+1
      if t1>5:
         t1=0
         wc=wc+1
      
         if wc==wb: 
            wc=wc+1
      
      if wc>5:
         wc=0
         wb=wb+1   
         if wb==wa: 
            wb=wb+1
            
      if wb>5:
         wb=0
         wa=wa+1  
  

   else:   
      Go=False
      print("DONE!")
      print(roznica[n])
      print(wa,wb,wc)
      print(t1,t2,i_tmp[n])
      print(x_file[t2],y_file[t2],m_file[t2])






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