# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 22:45:53 2022

@author: fx_66
"""


fiboRecur = lambda n: n if (n<2) else (fiboRecur(n-1)+fiboRecur(n-2))   


for i in range (10):   
    print (fiboRecur(i))
    
    