# -*- coding: utf-8 -*-
# Samet BELLUR

from os import system as sys

uil= list(range(4))#User İnformation List
titles= ["First Name: ","Last Name: ","Age: ","Birth Date (Year): "]

for i in range (4):
    uil[i]= input(titles[i])

sys ("cls")

for i in range (4):
    print("\n"+titles[i]+uil[i])

if int(uil[2])<18:
    print ("You can't go out. Because it's too dangerous")
elif int(uil[2])>=18:
    print ("\nYou can go out to the street")

sys ("pause")