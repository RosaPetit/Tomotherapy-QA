#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
#import matplotlib.pyplot as plt

import pandas as pd


 
G33L=pd.read_csv('AllG33L.csv', header=0)
df1=pd.DataFrame(G33L)
G32G=pd.read_csv('AllG32G.csv', header=0)
df2=pd.DataFrame(G32G)
DIFFD=pd.read_csv('AllDIFF.csv',header=0)
df3=pd.DataFrame(DIFFD)


#Constants 
beta=6


print("This is a program to calculate the TOLERANCE AND ACTION LIMITS for the Tomotherapy machine for the abdominal, breast+SVC, head and neck and prostate treatments \n") 

selection=input("Calculate for the Gamma index (G) and/or the difference in dose? (D)\n")

print("Wait the program is processing the previus data you entered \n")

if selection == "G":
  selection2=input("What actions and toletence limit do you want to know Gamma 3% 3mm (G33L) or Gamma 3% 2mm(G32G)? \n")
  if selection2 == "G33L": 
            T=0
            for i in range (1,len(df1)+1): #lee la fila AG33L y para el calculo hasta donde existen valores
              df1['diffa']=df1['AG33L'].diff(1) #diferencia 
              df1['diffa']=df1['diffa'].abs() #valor absoluto
              Suma1=df1['diffa'].sum() #Sumatoria
              
              break
            Mean1=df1['AG33L'].mean()
            st1=df1['AG33L'].std()
            ALA=beta*np.sqrt((st1**2)+((Mean1-T)**2))
            ALA2=ALA/2
            print(Mean1)
            ALATOTAL=(1-ALA2)
            print("The percentaje action limit for abdominal treatmens is",ALATOTAL)
            NG33LA=166
            NG33LB=165
            NG33LHN=115
            NG33LP=281
            #CentLA=(1/NG33LA)*G33LA166
            



  elif selection2 == "G32G":
            T=0
            print ("Numero positivo")
            NG32GA=71
            NG32GB=79
            NG32GHN=62
            NG32GP=131

elif selection == "D":
            T=1 
            print ("Igual a 0")
            NG32GA=71
            NG32GB=79
            NG32GHN=62
            NG32GP=131


        









  
