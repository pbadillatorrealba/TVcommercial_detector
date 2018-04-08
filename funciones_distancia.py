# ----------------------------------------------------------------------------------------------
# ----------------------------------- Funciones de Distancia -----------------------------------
# ----------------------------------------------------------------------------------------------
import numpy as np
import cv2

MIN_FLOAT =  np.finfo(float).min

def distancia_manhattan(u,v): 
    return np.sum(np.abs(u - v))

def distancia_chebychev(u,v):
    return np.max(np.abs(u - v))

def ditancia_hamming(u,v):
    return (np.array(u) == np.array(v)).sum

def distancia_euclideana(u,v):
    return np.linalg.norm(u-v)



