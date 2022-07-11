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

#Datensatz als Liste
#data = [21, 23, 18, 20, 30, 25, 21, 21, 23, 23]

def mittel(data):
    n = len(data)
    summe = 0
    for i in data:
        summe += i
    return summe / n

def median(data):
    n = len(data)
    data = sorted(data)
    if n%2 == 0:
        #Anzahl der Elemente in Liste ist gerade
        return 0.5 * (data[n//2] + data[n//2-1])
    else:
        #Anzahl der Elemente in Liste ist ungerade
        return data[n//2]
    
#Benötigt Laufzeitoptimierung
def modal(data):
    modalwerte = []
    vorkommen = []
    max_anzahl = 0
    #Zähle wie oft das Element in Liste vorkommt
    for i in data:
        anzahl = data.count(i)
        #Prüft ob das aktuelle Element das häufigste ist
        if anzahl > max_anzahl:
            max_anzahl = anzahl
        vorkommen.append((anzahl,i))
    for j in vorkommen:
        #Prüft welche Werte am häufigsten vorkommen
        if j[0] == max_anzahl:
            modalwerte.append(j[1])
    return set(modalwerte) #Set eleminiert Duplikate

def varianz(data):
    return 0, 0**2 #hoch zwei


print(f'Der Mittelwert ist {mittel(data)}')
print(f'Der Median ist {median(data)}')
print(f'Der Modus ist {modal(data)}')