import os
os.system('cls' if os.name == 'nt' else 'clear'); # limpar console

# Printar olá mundo
def hw():
  p = print('olá, mundo')
  p;
# hw();

# Saudar usuário
def saudacao():
  nome = input('Digite o seu nome: ');
  print(f'Olá, {nome}, muito prazer!');
# saudacao();

# Soma
def soma():
  n1 = int(input('digite o primeiro nº: '));
  n2 = int(input('digite o segundo nº: '));
  s = n1 + n2;
  print('O valor da soma de {0} + {1} é {2}'.format(n1, n2, s));
  print(f'O valor da soma de {n1} + {n2} = {n1+n2}')
# soma();

# 1. ler um nº inteiro e mostrar na tela seu antecessor e sucessor 
def exerc1():
  n = int(input('escreva um nº: \n'));
  print(f'o antecessor de {n} é {n - 1} e o seu sucessor é {n + 1}')
# exec1();

# 2. IMPORTANTE(Sintaxe pra calcular RAIZ QUADRADA) Printar na tela o dobro, triplo e raiz quadradade um nº
def exerc2():
  n = int(input('digite um nº '));
  print(f'o dobro de {n} é {n*2}')
  print(f'o triplo de {n} é {n*3}')
  print(f'a raiz quadrada de {n} é {n ** (1/2):.2f}')
  print(f'a raiz quadrada de {n} é {pow(n, (1/2)):.2f}')
# exerc2()

# 3.

# 4. Leia um input do usuário e mostre na tela o tipo primitivo e todas as infos possíveis sobre o dado
def exerc4():
  inp = input('Digite alguma coisa: ')
  print('É alfanumérico?', inp.isalnum());
  print('É um decimal?', inp.isdecimal());
  print('E um animal, ele é?', inp.isdecimal());
  print('Está em maiúscula?', inp.isupper());
# exerc4();

