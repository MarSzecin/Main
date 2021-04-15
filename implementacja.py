# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 12:36:08 2021

@author: marci
"""
import numpy as np
import matplotlib as plt

wezly = np.array([0, 1, 0.5, 0.75 ])

elementy = np.array([[1, 3],
                     [4, 2],
                     [3, 4]])

twb_L = 'D'
twb_R = 'D'
wwb_L = 0
wwb_R = 1

n = 100

def GenerujTabliceGeometrii(x_0,x_p,n):
    val = (x_p - x_0) / (n - 1)
    tablica = np.array([x_0])

    for i in range(1, n, 1):
        tablica = np.block([tablica, i * val + x_0])
    return i,tablica



# print(GenerujTabliceGeometrii(0,1,4))

Wezly, Tablica = GenerujTabliceGeometrii(0,1,4)
print('Liczba wezlow: ', Wezly+1)
print('Tablica wezlow: ', Tablica)

