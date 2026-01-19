# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 14:36:15 2026

Updated algorithm to search for bisymmetric matrix factorizations. Only searches bisymmetric factors.
"""

import numpy as np
import csv

m= 1#minimum value of x
M =1000 #maximum value of x


with open("BisymDataNew"+str(m)+"to"+str(M)+".csv", 'w', newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['x','y','a','b','c','d'])
    for x in range(m,M+1):
        for AC in range(1,x):
            BD=x-AC
            for a in range(1,AC+1):
                if AC%a==0:
                    c=int(AC/a) 
                    for b in range(1, BD+1):
                        if BD%b==0:
                            d=int(BD/b)
                            y=a*d+b*c
                            if np.gcd(x,y)==1 and (x<y):
                                writer.writerow([x,y,a,b,c,d])
                                
#Note: y values will be out of order. Sort CSV file afterwards by x, y