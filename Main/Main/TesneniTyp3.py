from math import *
from PrirubaSKuzelovymKrkem import *
from Soucast import *

class TesneniTyp3(Tesneni):
    """description of class"""

    b_Ge = 0

    def calcb_Gifirst(self): 
        """(72)-prvni aproximace"""
        self.b_Gi = self.b_Ge

    def calcb_Gi(self, F_G0):
        """(72)"""
        self.b_Gi = self.b_Ge

    def calcd_Ge(self):
        """(73)"""
        self.d_Ge = self.d_Gt
