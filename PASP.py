# -*- coding: utf-8 -*-
"""
PASP - Pete's Awesome Statistics Program

Created on Tue Jun 21 23:28:05 2022

@author: Tristan
"""

import pandas as pd #Exceldatensatz einlesen

#Excel zu Liste
data = pd.read_excel('Mappe1.xlsx')
data = data['Alter'].to_list()

#Ersatz Datensatz als Liste
#data = [21, 23, 18, 20, 30, 25, 21, 21, 23, 23]

def mittelwert(data):
    n = len(data)
    summe = 0
    for i in data:
        summe += i
    return summe / n

def median(data):
    n = len(data)
    data = sorted(data)
    if n%2 == 0:    #Anzahl der Elemente in Liste ist gerade
        return 0.5 * (data[n//2] + data[n//2-1])
    else:   #Anzahl der Elemente in Liste ist ungerade
        return data[n//2]
    
def modalwert(data):
    modalwerte = []
    vorkommen = []
    max_anzahl = 0
    for i in data:  #Zähle wie oft das Element in Liste vorkommt
        anzahl = data.count(i)
        if anzahl > max_anzahl: #Prüft ob das aktuelle Element das häufigste ist
            max_anzahl = anzahl
        vorkommen.append((anzahl,i))
    for j in vorkommen:  #Prüft welche Werte am häufigsten vorkommen
        if j[0] == max_anzahl:
            modalwerte.append(j[1])
    return set(modalwerte) #Set eleminiert Duplikate

def summe(data):
    sum = 0
    for i in data:
        sum += i
    return sum

def minimum(data):
    min = sorted(data)
    return min[0]

def maximum(data):
    max = sorted(data)
    return max[-1]

def spannweite(data):
    a = sorted(data)
    return a[-1] - a[0]

def varianz(data):
    a = 1 / len(data)
    b = 0
    for i in data:
        b += (i - mittelwert(data))**2
    return a * b

def standardabweichung(data):
    return varianz(data) ** 0.5 #Wurzel aus Varianz

print(f'Mittelwert = {mittelwert(data)}')
print(f'Median = {median(data)}')
print(f'Modalwert = {modalwert(data)}')
print(f'Summe = {summe(data)}')
print(f'Min = {minimum(data)}')
print(f'Max = {max(data)}')
print(f'Spannweite = {spannweite(data)}')
print(f'Varianz = {varianz(data)}')
print(f'Standardabweichung = {standardabweichung(data)}')