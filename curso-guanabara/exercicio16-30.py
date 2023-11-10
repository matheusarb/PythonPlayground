import os
import random
import math

os.system('cls' if os.name == 'nt' else 'clear'); # limpar console


# 16. recebe um numero real pelo usuário e mostra sua porção inteira no console
def converterRealInteiro():
  numReal = float(input('Digite um nº real: '))
  print(f'A porção inteira é {math.floor(numReal)}')
# converterRealInteiro();

# 17. Calcular o comprimento da hipotenusa
def calcularHipotenusa():
  catetoOposto = int(input('digite o comprimento oposto: '))
  catetoAdjacente = int(input('digite o comprimento adjacente: ')) 
  quadradoHipotenusa = catetoOposto **2 + catetoAdjacente**2
  comprimentoHipotenusa = math.sqrt(quadradoHipotenusa)
  print(f'O comprimento da hipotenusa: {comprimentoHipotenusa}')
calcularHipotenusa()