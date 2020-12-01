#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:06:15 2020

@author: katiewhitby
"""

from astropy.io import fits
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt

hdulist = fits.open('A1_mosaic.fits')
# hdulist[0].header to see info about the header type in the console

# hdulist[0].data  to see the data as an array type in console


data = hdulist[0].data
data1 = data.flatten()              #go from 2D to 1D
data2=[]


for i in data1:                     #choosing the relevant data, if you get rid of this there a lot of higher values
    if 2000<i<3750:
        data2.append(i)
       
plt.hist(data2, bins=150)
plt.xlabel('Pixel value')
plt.ylabel('intensity')
plt.show()

standard_dev=np.std(data2)
mean=np.mean(data2)


hdulist.close('A1_mosaic.fits')


"""
I am still not 100% sure this is the correct info that we want to see in the histogram
"""