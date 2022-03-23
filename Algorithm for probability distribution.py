                                                                                                                    # -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:12:50 2021

@author: Manoj
"""

MEAN=int(input("ENTER THE MEAN VALUES:"))
SIGMA=int(input("ENTER THE SIGMA VALUES:"))
SD=int(input("Enter the value:"))
DD=int(input("Enter the 2d value:"))
from statistics import NormalDist
SM=NormalDist( mu = MEAN, sigma=SIGMA)
M=SM.cdf(SD)
D=SM.cdf(DD)
N=M-D

if M>0:
    print("ANSWER IS",M)
elif D>0:
    print("ANSWER IS",D)
else:
    print("ANSWER IS",N)
