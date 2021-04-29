# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:31:56 2021

@author: marci
"""

import numpy as np


def GeometriaDefinicja():
    
    nodes = np.array([[1,0],
              [2,1],
              [3,0.5],
              [4,0.75]] )
    
    elem = np.array([[1,1,3],
                     [2,4,2],
                     [3,3,4]] )
    
    WB = [{"Index": 1, "TYP":'D', "Wartosc":1},
          {"Index": 2, "TYP":'D', "Wartosc":2},]
    
    
    return nodes, elem, WB
    