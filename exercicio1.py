# Printar olá mundo
def hw():
  p = print('olá, mundo')
  p;
# hw();

# Saudar usuário
def saudacao():
  input = string('Digite o seu nome: ');
  print(f'Olá, {input}, muito prazer!');
saudacao();

# 1. ler um nº inteiro e mostrar na tela seu antecessor e sucessor 
def exerc1():
  n = int(input('escreva um nº: \n'));
  print(f'o antecessor de {n} é {n - 1} e o seu sucessor é {n + 1}')
# exec1();

# 2. Dobro, triplo e raiz quadrada
def exerc2():
  n = int(input('digite um nº '));
  print(f'o dobro de {n} é {n*2}')
  print(f'o triplo de {n} é {n*3}')
  print(f'a raiz quadrada de {n} é {n ** (1/2):.2f}')
  print(f'a raiz quadrada de {n} é {pow(n, (1/2)):.2f}')
# exerc2()

# 3.  