#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:35:27 2023

@author: belen
"""

#familia
import random

integrante = ""

numero_aleatorio = random.randint(1, 6)
if numero_aleatorio ==1:
    integrante = "Chistian"
elif numero_aleatorio ==2:
    integrante = "Mabel"
elif numero_aleatorio==3:
    integrante="Belén"
elif numero_aleatorio==4:
    integrante="Guz"
elif numero_aleatorio==5:
    integrante="Lola"
elif numero_aleatorio==6:
    integrante="Chatrán"

print(integrante)