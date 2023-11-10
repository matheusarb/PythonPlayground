import os
os.system('cls' if os.name == 'nt' else 'clear'); # limpar console

import random
from math import sqrt, floor, ceil

# num = int(input('Escreva um nº inteiro: '))
# raiz = sqrt(num)
# print(f'A raiz quadrada de {num} é {ceil(raiz)}')

numReal = random.random()
numInt = random.randint(2, 400)
print(numReal)
print(numInt)