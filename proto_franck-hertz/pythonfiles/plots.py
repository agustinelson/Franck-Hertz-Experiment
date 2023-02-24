#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 22:29:50 2023

@author: legacy
"""

import matplotlib.pyplot as plt
import numpy as np
import os

namefiles = sorted(os.listdir('data'))

inf = 17


i = 0
ax = []

#plt.figure(figsize=(6,6))

for namefile in namefiles[inf:inf+6]:
    print(namefile)
    data = np.genfromtxt(f'data/{namefile}', usecols=(0,-2,-1), comments="#")
    ax.append(plt.subplot(6,1,1+i))
    plt.errorbar(data[:,0], data[:,1], yerr=data[:,2], xerr=0.005, label=(f"{i+1}.00V"), c = "k")
    
    i+=1
    
    
plt.xlabel(r"Acceleration Voltage ($V$)")
ax[3].set_ylabel(r"Electrical current ($\mu A$)")
plt.savefig(f"plots/collectorvoltage_{26}.00V_{31}.00V.svg")

    