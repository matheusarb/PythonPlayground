# 1. Algoritmo de busca linear/sequencial
def busca_linear(lista, elemento):
  pos = 0
  encontrado = False

  while (pos < len(lista) and not encontrado):
    if (lista[pos] == elemento):
      encontrado = True
      break;
    else:
      pos += 1
      continue;
  return f"Encontrado = {encontrado}. O el é {elemento} na posição {pos}"

testeLista= [1,2,4, 14, 532, 42, 21, 123, 43, 2111]
# print(busca_linear(testeLista, 4))

# 2. Algoritmo de busca sequencial em vetor ordenado (ordem crescente, por ex.)
def busca_sequencial_ordenada(lista, elemento):
  pos = 0
  encontrado = False
  para = False

  while pos < len(lista) and not encontrado and not para:
    if lista[pos] == elemento:
      encontrado = True
    else:
      if lista[pos] > elemento:
        para = True
      else:
        pos += 1
  return (f"Encontrado = {encontrado}. El {elemento} na posi {pos}") 


tListaOrd = [0, 1, 3, 5, 6, 7, 10, 12, 22, 45, 65]
print(busca_sequencial_ordenada(tListaOrd, 88))

# 3. Algoritmo de busca binária
# encontra o valor do meio, se ele for menor que o valor da busca, a busca continuará na metade superior da sequência de itens, senão o contrário (até achar)

def busca_binaria(lista, elemento):
  minimo = 0
  maximo = len[lista]-1
  encontrado = False

  while minimo <= maximo and not encontrado:
    meio_lista = (minimo + maximo) // 2
    if lista[meio_lista] == elemento:
      encontrado = True
    else:
      if elemento < lista[meio_lista]:
        maximo = meio_lista - 1
      else:
        minimo = meio_lista + 1
  return encontrado

# 4. Algoritmo de ordenação por inserção
# iniciado a partir do segundo valor no vetor, pois o primeiro será uma referência pra ordenação
def insertion_sort(lista):
  # for i = 1 to 6
    

# 5. Algoritmo de Selection Sort
# 6. Bubble Sort
# 8. Quick Sort