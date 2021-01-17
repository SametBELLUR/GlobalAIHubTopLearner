# -*- coding: utf-8 -*-
# Samet BELLUR

from os import system as sys

values = list(range(5))
tab= "\n" # I need that because backslash cannot useable in f-string.

for i in range(5):
    x= input ("Varriable {}: ".format(i+1))
    try:
        values[i] = int(x)
    except ValueError:
        try:
            values[i]= float(x)
        except ValueError:
            values[i]= x

sys ("cls")

for i in range(5):
    print(f'{tab}Varriable {i+1};{tab}Value: {values[i]}{tab}Type: {type(values[i])}')

sys ("pause")