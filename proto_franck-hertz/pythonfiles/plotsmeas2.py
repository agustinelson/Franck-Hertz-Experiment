#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 15:42:02 2023

@author: legacy
"""
#%%%
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
#%%%
files = os.listdir(os.path.dirname(os.path.abspath(__file__))+"/measurements2/collectorVoltage3.00V/decelerationVoltage1.00V")
files.remove('README.md')
files.sort()
print(files)
#%%%

voltage=np.arange(32)
#%%%

data = []
for file in files:
    file=path=os.path.dirname(os.path.abspath(__file__))+"/measurements2/collectorVoltage3.00V/decelerationVoltage1.00V/"+file
    data.append(pd.read_csv(file)["Unnamed: 1"].dropna().mean())
#%%%
plt.plot(voltage, data)