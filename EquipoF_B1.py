#imports
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import os
#-------------------------------------------------------------------------
#creacion de variables

a = int(input("a"))     #Numero de datos de A

aNombre = input("Introduce el nombre del Primer Factor ") 

b = int(input("b"))     #Numero de datos de B

bNombre = input("Introduce el nombre del Segundo factor ")

replicas = int(input("replicas"))    #Numero de replicas 

sumas = [b]

sumasTotales = [a]

sumaTotal = 0

anova = np.zeros(shape=(5,4))

os.system('cls')
#--------------------------------------------------------------------------------
#creacion de root window y dirección de documento

root = tk.Tk()
root.title("Calculator")
root.withdraw()

filePath = filedialog.askopenfilename()         
                 
#----------------------------------------------------------------------------------------------------------
#Lectura de archivos y creación de matriz

datos = pd.read_csv(filePath, header = 0) #lee el csv

temp = (a*replicas)-1

prueba = np.matrix(datos.loc[0:temp])

print(prueba)
