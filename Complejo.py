import unittest
import math
import numpy as np

class Complejo():
    
    def __init__(self, real, imaginario):

        self.real = real
        self.imaginario = imaginario
        self.norma = np.sqrt(self.imaginario**2+self.real**2)
        
        
    def conjugado(self):
        
        self.imaginario = -self.imaginario
    
    def calcula_norma(self):
        
        self.norma = np.sqrt(self.imaginario**2+self.real**2)
        
    def pow(self, n):
        
        return self.imaginario**n
    
        
        