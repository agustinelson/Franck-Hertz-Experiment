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

inf = 0
nplots = 5

i = 0
ax = []



for namefile in namefiles[inf:inf+nplots]:
    print(namefile)
    data = np.genfromtxt(f'data/{namefile}', usecols=(0,-2,-1), comments="#")
    ax.append(plt.subplot(nplots,1,1+i))
    
    plt.errorbar(data[:,0], data[:,1],
                 yerr=data[:,2], xerr=0.005, 
                 label=(f"{i+1}.00V"), 
                 c="k",
                 marker =".",barsabove="True",
                 ecolor="k")
    
    i+=1
    
    
plt.xlabel(r"Acceleration Voltage ($V$)")
ax[int(nplots/2)].set_ylabel(r"Electric current ($\mu A$)")


for _ax in ax: _ax.set_ylim((0.01,1))


#ax[3].set_ylim((0.10,0.15))

#ax[3].set_ylabel(r"Electrical current ($\mu A$)")


#plt.show()
plt.savefig(f"plots/collectorvoltage_{inf+1}.00V_{inf+nplots}.00V.svg")

    