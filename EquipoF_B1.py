#cosa diego.py

#imports
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import os

#creacion de variables
a = int(input("a")) #cuantos valores en a
aNombre = input("Introduce el nombre del Primer Factor ") #nombre para la a
b = int(input("b")) #cuantos valores en a
bNombre = input("Introduce el nombre del Segundo factor ") #nombre para la b
replicasVert = 0 #define cuantas replicas verticales tenemos
replicasHor = 0 #define cuantas replicas verticales tenemos
replicas = input("replicas")
temp = replicas*a
sumas = [b]
sumasTotales = [a]
sumaTotal = 0
anova = np.zeros(shape=(5,4))

os.system('cls')

#creacion de root window y asignación de valores
root = tk.Tk()
root.title("Calculator")
root.withdraw()

filePath = filedialog.askopenfilename()

print(filePath)

datos = pd.read_csv(filePath, header = 0) #lee el csv

#print(datos)



print(datos['C1'])



print(datos.loc[0:3])    #imprime los datos desde el index 0 al 3


print(datos.sort_values(by='C1', ascending= True)) #filtra los datos a partir de la columna C1

# si (datos.sort_values(by='C1', ascending = false )) #no te va a ordenar los datos de mayor a menor, sino al reves

prueba = np.matrix(datos.loc[0:4])


print(prueba)