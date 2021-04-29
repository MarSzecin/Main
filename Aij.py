# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 10:39:26 2021

@author: marci
"""

def Aij(dphi1, dphi2,c,phi1,phi2):
    
    Aij=lambda x: -dphi1(x)*dphi2(x) + c*phi1(x)*phi2(x)
    
    
    
    return Aij