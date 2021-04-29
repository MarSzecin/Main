# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 12:58:59 2021

@author: marci
"""

def FunkcjeBazowe(n):
    '''
    

    Returns
    -------
    None.

    '''
    
    if n==0:
        f=lambda x: 0*x +1
        df=lambda x: 0*x
    elif n==1:
            f = (lambda x: -1/2*x + 1/2, lambda x: 1/2*x + 1/2)
            df = (lambda x: -1/2 + 0*x, lambda x: 1/2 + 0*x)
  # elif n==2:
  #     f =
  #     df =
    else:
        raise Exception("Błąd w funkcjach bazowych")
            
    
    
    
    return f,df