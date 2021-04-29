# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:48:20 2021

@author: marci
"""
import numpy as np
import matplotlib.pyplot as plt


def RysujGeometrie(NODES, ELEMS, WB):
    """

    Parameters
    ----------
    NODES : TYPE
        DESCRIPTION.
    ELEMS : TYPE
        DESCRIPTION.
    WB : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    fh = plt.figure()
    
    plt.plot(NODES[:,1], np.zeros((np.shape(NODES)[0],1) ), '-b')
    
    
    
    nodeNo = np.shape(NODES)[0]
    
    for i in np.arange(0,nodeNo):
        ind = NODES[i,0]
        x=NODES[i,1]
        plt.text(x, 0.01, str(int(ind)), c="b")
        plt.text(x, -0.01, str(x))
        
    elemNo=np.shape(ELEMS)[0]
    
    
    for j in np.arange(0,elemNo):
        
        wp=ELEMS[j,1]
        wk=ELEMS[j,2]
        
        x=(NODES[wp-1,1] + NODES[wk-1,1] )/2
        
        plt.text(x, 0.01, str(j+1), c="r")
        
    plt.show()
    
    return fh
        
    
        