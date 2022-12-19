#!/usr/bin/env python3
import sys
import numpy 


def StarMatch(xr,yr,mr,xf,yf,rf,scale):
    dist=[]
    print(len(xr))
    xr=numpy.array(xr).astype(numpy.float)
    yr=numpy.array(yr).astype(numpy.float)
    for i,tmp in enumerate(xr):
        x=xr[i]
        y=yr[i]
        numpy.delete(xr,i)
        numpy.delete(yr,i)
        d=((x-xr)**2+(y-yr)**2)**0.5
        dist.extend(d)
    return(dist)  
        


#wczytuje plik od lini
#dane=load_file(10,smc01.txt)
def load_file(min,file):
    f=open(file,'r')
    i=0
    dane=[]
    for line in f:
       if i>min-1 and line.strip()[0]!="#" and len(line.split())>0: dane.append(line.split())
       i=i+1
    dane=list(zip(*dane))   
    return dane	 

#---------------------------------------------------------------
#wczytuje plik .ap
#dane,bledy=loadap(smc01.ap)
def loadap(file):
    f=open(file,'r')
    i=0
    dane=[]
    bledy=[]
    przelacznik=2
    for line in f:
       if i>2 and len(line.split())>0:
	       if przelacznik == 0:
	          dane.append(line.split())
	          przelacznik=1
	       elif przelacznik == 1:
	          bledy.append(line.split())
	          przelacznik=2
	       elif przelacznik == 2:
	          przelacznik=0
       i=i+1
    dane=list(zip(*dane))
    bledy=list(zip(*bledy))
    return dane, bledy

#---------------------------------------------------------------

#wczytuje plik .out 
#dane=loadout(smc01.out)
def loadout(file):
    f=open(file,'r')
    i=0
    dane=[]
    for line in f:
       if i>2 and len(line.split())>0: dane.append(line.split())
       i=i+1
    dane=list(zip(*dane))
    return dane	 




