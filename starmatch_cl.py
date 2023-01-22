#!/usr/bin/env python3
import sys
import numpy as np
from starmatch_lib import *

#  arguments 

pixscale=1
starratio=1

if len(sys.argv)< 3:
   print("wrong format: \n./starmatch_cl.py reference.ap field.ap \n or")
   print("./starmatch_cl.py pixscale=2.3 starratio=0.7 reference.ap field.out")
   print("pixscale - field/reference pixscale (HAWKI/SOFI = 0.3680)")
   print("starratio - field/reference ratio of stars within magnitude range (HAWKI (1 CHIP)/SOFI = 0.58)")
   sys.exit(1)

elif len(sys.argv) == 3:
   file_name_1=sys.argv[1]
   file_name_2=sys.argv[2]
elif  len(sys.argv)> 3:
   file_name_1=sys.argv[-2]
   file_name_2=sys.argv[-1]
   for arg in sys.argv:
      if "pixscale" in arg:
         pixscale=arg.split("=")[1]
      elif "starratio" in arg:
         starratio=arg.split("=")[1]

# reference file load

if ".ap" in file_name_1:
   dane,bledy=loadap(file_name_1)
elif ".out" in file_name_1:
   dane=loadout(file_name_1)
elif ".coo" in file_name_1:
   dane=loadout(file_name_1)
else: dane=load_file(0,file_name_1)    


x_ref=dane[1]
y_ref=dane[2]
m_ref=dane[3]

# field file load

if ".ap" in file_name_2:
   dane,bledy=loadap(file_name_2)
elif ".out" in file_name_2:
   dane=loadout(file_name_2)
elif ".coo" in file_name_2:
   dane=loadout(file_name_2)   
else: dane=load_file(0,file_name_2)   

x_file=dane[1]
y_file=dane[2]
m_file=dane[3]

# script run

sm=StarMatch()
sm.loud=True
sm.nb_use=400
sm.pixscale=float(pixscale)           
sm.fieldStarsRatio=float(starratio)   
sm.ref_xr=x_ref
sm.ref_yr=y_ref
sm.ref_mr=m_ref
sm.field_xr=x_file
sm.field_yr=y_file
sm.field_mr=m_file
sm.go()
print(sm.mssg)
print("X field to reference: ",sm.p_fr_x)
print("Y field to reference: ",sm.p_fr_y)
print("X reference to field: ",sm.p_rf_x)
print("Y reference to field: ",sm.p_rf_y)

txt = "# reference="+file_name_1+" field="+file_name_2+"\n"
txt = txt+"# x' = px[0] + px[1] * x + px[2] * y + px[3] * x*y + px[4] * x*x + px[5] * y*y\n"
txt = txt+"# y' = py[0] + py[1] * x + py[2] * y + py[3] * x*y + py[4] * x*x + py[5] * y*y\n"
txt = txt+"# Field to Reference\n"
txt = txt+  "Px=  " + "".join(str(tmp)+" " for tmp in sm.p_fr_x)+"\n"
txt = txt+  "Py=  " + "".join(str(tmp)+" " for tmp in sm.p_fr_y)+"\n"
txt = txt+"# Reference to Field\n"
txt = txt+  "Px=  " + "".join(str(tmp)+" " for tmp in sm.p_rf_x)+"\n"
txt = txt+  "Py=  " + "".join(str(tmp)+" " for tmp in sm.p_rf_y)+"\n"

mch_file = file_name_2.split(".")[0]+".xytr"
with open(mch_file, 'w') as f:
     f.write(txt)




    




