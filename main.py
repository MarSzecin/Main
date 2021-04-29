# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 12:36:08 2021

@author: marci
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spint
from GeometriaDefinicja import GeometriaDefinicja
from AutomatycznyGeneratorGeometrii import AutomatycznyGeneratorGeometrii
from RysujGeometrie import RysujGeometrie
from Alokacja import Alokacja
from FunkcjeBazowe import FunkcjeBazowe
from Aij import Aij





if __name__ == '__main__':
    
    #Preprocesing
    
    
    
    #Parametry sterujace
    c=0;
    f=lambda x: 1 #Wymuszenie
    
    #Geomatria - Definicja
    WEZLY,ELEMENTY,WB = GeometriaDefinicja()
    n = np.shape(WEZLY)[0]
    
    
    # #Automatyczne wygenerowanie geometrii
    
    # x_a=0
    # x_b=1
    # n=5
    
    
    # WEZLY, ELEMENTY = AutomatycznyGeneratorGeometrii(x_a, x_b, n)
    
    
    # #Warunki brzegowe
    # WB = [{"Index": 1, "TYP":'D', "Wartosc":0},
    #      {"Index": n, "TYP":'D', "Wartosc":1},]
    
    RysujGeometrie(WEZLY,ELEMENTY,WB)
    
    print(WEZLY)
    
    
    
    
    
    #Processing
    
    [A,b]= Alokacja(n)
    stop_funkcji = 1
    phi, dphi = FunkcjeBazowe(stop_funkcji)
    
    # x2 = np.linspace(-1,1,101)
    # plt.plot(x2, phi[0](x2),'r')
    # plt.plot(x2, phi[1](x2),'g')
    # plt.plot(x2, dphi[0](x2),'b')
    # plt.plot(x2, dphi[1](x2),'y')

    
    
    
    #PROCESSING
    
    for k in np.arange(0,np.shape(ELEMENTY)[0]):
        
        elemIndRow = k
        elemGlobalInd = ELEMENTY[k,0]
        elemWezel1= ELEMENTY[k,1]
        elemWezel2 = ELEMENTY[k,2]
        
        x_a=WEZLY[elemWezel1-1,1]
        x_b=WEZLY[elemWezel2-1,1]
        
        temp = np.zeros([stop_funkcji+1, stop_funkcji+1])

        J = (x_b-x_a)/2
        
        n=0; m=0;
        temp[n,m] = J*spint.quad(Aij(dphi[n],dphi[m],c,phi[n]),phi[m], -1, 1)
        n=0; m=1;
        temp[n,m] = J*spint.quad(Aij(dphi[n],dphi[m],c,phi[n]),phi[m], -1, 1)
        n=1; m=0;
        temp[n,m] = J*spint.quad(Aij(dphi[n],dphi[m],c,phi[n]),phi[m], -1, 1)
        n=1; m=1;
        temp[n,m] = J*spint.quad(Aij(dphi[n],dphi[m],c,phi[n]),phi[m], -1, 1)


        
        

   



















































# wezly = np.array([0, 1, 0.5, 0.75 ])

# elementy = np.array([[1, 3],
#                      [4, 2],
#                      [3, 4]])

# twb_L = 'D'
# twb_R = 'D'
# wwb_L = 0
# wwb_R = 1

# #Parametry sterujące
# c=0
# f = lambda x: 0 #wymuszenie

# n = 100


# def GenerujTabliceGeometrii(x_0,x_p,n):
    
#     val = (x_p-x_0)/(n-1)
#     tablica1 = np.array([x_0])
    
#     for indeks_tab1 in range(1,n,1):
#         tablica1 = np.block([tablica1, indeks_tab1 * val + x_0])
    
#     tablica2 = np.zeros((n-1,2))
        
#     for indeks_tab2 in range(0, n-1, 1):
#         tablica2[indeks_tab2][0] = indeks_tab2+1
#         tablica2[indeks_tab2][1] = indeks_tab2+2

    
#     return indeks_tab1,tablica1,tablica2


# def Rysuj_geometrie(tablica1,tablica2, n):
#     tab=np.zeros((n))
#     l1 = plt.plot(tablica1,tab)
#     for i in range(0,n,1):
#         plt.text(tablica1[i], -0.01, str(i+1))
#         plt.text(tablica1[i], 0, "|")
#         plt.text(tablica1[i+1]/2+tablica1[i]/2, 0.005 ,str(i+1))
    
    
    

# Wezly, Tablica1, Tablica2 = GenerujTabliceGeometrii(0,1,4)
# Rysuj_geometrie(Tablica1, Tablica2, Wezly+1)
# Liczba_wezlow = Wezly + 1

# print('Liczba wezlow: ', Liczba_wezlow)
# print('Tablica wezlow: ', Tablica1)
# print('Tablica elementow: ', Tablica2)




# """ Processing """


# #Alokacja
# A = np.zeros((Liczba_wezlow,Liczba_wezlow))
# b = np.zeros((Liczba_wezlow,1))
# print(A)


# #Częsć głowna
# for ee in np.arange(0,)


