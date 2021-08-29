#imports
import tkinter as tk
from tkinter import Canvas, Label, Pack, filedialog, Entry, Tk, Toplevel, Text, Button
import pandas as pd
import numpy as np
import os
 
#-------------------------------------------------------------------------
#creacion de variables
global anova 
anova = np.zeros(shape=(5,4))
 
os.system('cls')
#--------------------------------------------------------------------------------
#creacion de root window y dirección de documento
 
root = tk.Tk()
root.title("HackMty")
#----------------------------------------------------------------------------------------------------------
#Creación del GUI
label=Label(root, text="Input each variable")
label.pack()
 
barratexto=Entry(root, justify="center" ,width=50)
barratexto.config(fg='grey')
barratexto.insert(0, "Input Value of Factor A")
barratexto.pack()
 
#barratexto2=Entry(root, justify="center" ,width=50)
#barratexto2.config(fg='grey')
#barratexto2.insert(0, "Input Name of Factor A")
#barratexto2.pack()
 
barratexto3=Entry(root, justify="center" ,width=50)
barratexto3.config(fg='grey')
barratexto3.insert(0, "Input Value of Factor B")
barratexto3.pack()
 
#barratexto4=Entry(root, justify="center" ,width=50)
#barratexto4.config(fg='grey')
#barratexto4.insert(0, "Input Name of Factor B")
#barratexto4.pack()
 
barratexto5=Entry(root, justify="center" ,width=50)
barratexto5.config(fg='grey')
barratexto5.insert(0, "Input Number of Replications")
barratexto5.pack()
 
#----------------------------------------------------------------------------------------------------
#funciones de gui
 
 
def saveascsv():
    np.savetxt("Anova.csv", anova, delimiter=",")
    output=Label(root, text="Your file got downloaded on your python folder")
    output.pack()
 
def Click():
    #definición de variables glovales
    global a
    global aNombre
    global b
    global bNombre
    global replicas
    a=int(barratexto.get())
    input1=Label(root, text="Variable A =" + str(a))
    input1.pack()
 
    b=int(barratexto3.get())
    input3=Label(root, text="Variable B =" + str(b))
    input3.pack()
 
 
    replicas=int(barratexto5.get())
    input5=Label(root, text="Number of Replications =" + str(replicas))
    input5.pack()
 
def Click6():
    filePath = filedialog.askopenfilename()         
                 
    #----------------------------------------------------------------------------------------------------------
    #Lectura de archivos y creación de matriz
    
    datos = pd.read_csv(filePath, header = 0) #lee el csv
    
    temp = (a*replicas)
    
    matrizD = np.matrix(datos.loc[0:temp])
    
    #--------------------------------------------------------------------------------
    #sumas iniciales
    
    matSumas = np.zeros(shape=(a,b))
    
    for i in range(0,a):
        for j in range(1,b+1):
            suma = 0
            for k in range(1,replicas+1):
                suma = suma + matrizD[k+i*replicas,j]
            matSumas[(i)][(j-1)] = suma
    
    
    sumaH = []
    for i in range(0,a): 
        suma = 0
        for j in range(0,b):
            suma = suma + matSumas[i][j]
        sumaH.append(suma) 
    
    sumaV = []
    for i in range(0,b): 
        suma = 0
        for j in range(0,a):
            suma = suma + matSumas[j][i]
        sumaV.append(suma) 
    
    sumaF = 0
    for i in range(0,a):
        sumaF = sumaF + sumaH[i]
    
    #--------------------------------------------------------------------------------
    #valores para llenar anova
    
    #SSA
    temp = 0
    for i in range(0,a): 
        temp = temp + (sumaH[i]*sumaH[i])
    
    anova[0][0] = (temp/(b*replicas))-((sumaF*sumaF)/(a*b*replicas))
    
    #SSB
    temp = 0
    for i in range(0,b): 
        temp = temp + (sumaV[i]*sumaV[i])
    
    anova[1][0] = (temp/(a*replicas))-((sumaF*sumaF)/(a*b*replicas))
    
    #SSAB
    temp = 0
    for i in range(0,a):
        for j in range(0,b):
            temp = temp + (matSumas[i][j]*matSumas[i][j])
    
    anova[2][0] = (temp/replicas) - ((sumaF*sumaF)/(a*b*replicas) + anova[0][0] + anova[1][0])
 
    #SST
    temp = 0
    for i in range(1,a*replicas+1):
        for j in range(1,b+1):
            temp = temp + (matrizD[i,j]*matrizD[i,j])
    
    anova[4][0] = temp - ((sumaF*sumaF)/(a*b*replicas))
 
    #SSE
    anova[3][0] = anova[4][0] - anova[2][0] - anova[1][0] - anova[0][0]
 
    #GL's
    anova[0][1] = a - 1
    anova[1][1] = b - 1
    anova[2][1] = (a - 1) * (b - 1)
    anova[3][1] = a * b * (replicas - 1)
    anova[4][1] = a * b * replicas - 1
 
    #DF's
    anova[0][2] = anova[0][0] / anova[0][1]
    anova[1][2] = anova[1][0] / anova[1][1]
    anova[2][2] = anova[2][0] / anova[2][1]
    anova[3][2] = anova[3][0] / anova[3][1]
 
    #F calc's
    anova[0][3] = anova[0][2] / anova[3][2]
    anova[1][3] = anova[1][2] / anova[3][2]
    anova[2][3] = anova[2][2] / anova[3][2]
 
    print(anova)
 
 
#----------------------------------------------------------------------------------------------------
#botones
 
boton1=Button(root, text="Input All Values", command=Click)
boton1.pack()
 
boton2=Button(root, text="Upload csv File", command=Click6)
boton2.pack()
 
boton3=Button(root, text="Save Analysis of Variance as cvs", command=saveascsv)
boton3.pack() 
 
root.mainloop()
#Made By Team "F"
#Diego - F
#Hugo - F
#Ardiam - F
#Miguel - F
