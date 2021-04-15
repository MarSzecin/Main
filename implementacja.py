# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 12:36:08 2021

@author: marci
"""
import numpy as np
import matplotlib.pyplot as plt

wezly = np.array([0, 1, 0.5, 0.75 ])

elementy = np.array([[1, 3],
                     [4, 2],
                     [3, 4]])

twb_L = 'D'
twb_R = 'D'
wwb_L = 0
wwb_R = 1

n = 100


#def Inicjalizacja_paramatrow_sterujacych(przedzial,war_brzeg)


def GenerujTabliceGeometrii(x_0,x_p,n):
    
    val = (x_p-x_0)/(n-1)
    tablica1 = np.array([x_0])
    
    for indeks_tab1 in range(1,n,1):
        tablica1 = np.block([tablica1, indeks_tab1 * val + x_0])
    
    tablica2 = np.zeros((n-1,2))
        
    for indeks_tab2 in range(0, n-1, 1):
        tablica2[indeks_tab2][0] = indeks_tab2+1
        tablica2[indeks_tab2][1] = indeks_tab2+2

    
    return indeks_tab1,tablica1,tablica2


def Rysuj_geometrie(tablica1,tablica2, n):
    tab=np.zeros((n))
    l1 = plt.plot(tablica1,tab)
    for i in range(0,n,1):
        plt.text(tablica1[i], -0.01, str(i+1))
        plt.text(tablica1[i], 0, "|")
        plt.text(tablica1[i+1]/2+tablica1[i]/2, 0.005 ,str(i+1))
    
    
    




Wezly, Tablica1, Tablica2 = GenerujTabliceGeometrii(0,1,4)
Rysuj_geometrie(Tablica1, Tablica2, Wezly+1)
Liczba_wezlow = Wezly + 1
print('Liczba wezlow: ', Liczba_wezlow)
print('Tablica wezlow: ', Tablica1)
print('Tablica elementow: ', Tablica2)







