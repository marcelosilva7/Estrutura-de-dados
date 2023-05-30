# lista_selecao = [51, 61, 91, 41, 1, 57, 85, 90, 31, 10]
# # menor pro maior complexidade 0 de n
# tamanho = len(lista_selecao)
# for m in range(tamanho -1):
#     menor_numero = m
#     for c in range(m + 1, tamanho):
#         if lista_selecao[c] < lista_selecao[menor_numero]:
#             menor_numero  = c
#     if menor_numero != m:
#         lista_selecao[m], lista_selecao[menor_numero] = lista_selecao[menor_numero], lista_selecao[m]
# print(lista_selecao)
#
#
#
# lista_insercao = [20, 10, 31, 57, 61, 52, 87, 91, 25, 30]
# # menor pro maior
# tamanho1 = len(lista_insercao)
# for i in range(1, tamanho1):
#     valor = lista_insercao[i]
#     p = i - 1
#     while p >= 0 and lista_insercao[p] > valor:
#         lista_insercao[p + 1] = lista_insercao[p]
#         p -= 1
#     lista_insercao[p + 1] = valor
#
# print(lista_insercao)

lista_shell = [12, 15, 81, 21, 61, 91, 51, 1]
tamanho_shell = len(lista_shell)
gaps = [4, 2, 1]

for gap in gaps:
    for i in range(gap, tamanho_shell):
        temp = lista_shell[i]
        j = i

        while j >= gap and lista_shell[j - gap] > temp:
            lista_shell[j] = lista_shell[j - gap]
            j -= gap

        lista_shell[j] = temp

print(lista_shell)
#
# def merge_sort(lista):
#     tamanho = len(lista)
#     if tamanho <= 1:
#         return lista
#
#     meio = tamanho // 2
#     lista_esquerda = lista[:meio]
#     lista_direita = lista[meio:]
#
#     esquerda_separada = merge_sort(lista_esquerda)
#     direita_separada = merge_sort(lista_direita)
#
#     merged = merge(esquerda_separada, direita_separada)
#     return merged
#
#
# def merge(esquerda, direita):
#     merged = []
#     i = j = 0
#
#     tamanho_esquerda = len(esquerda)
#     tamanho_direita = len(direita)
#     while i < tamanho_esquerda and j < tamanho_direita:
#         if esquerda[i] <= direita[j]:
#             merged.append(esquerda[i])
#             i += 1
#         else:
#             merged.append(direita[j])
#             j += 1
#
#     merged.extend(esquerda[i:])
#     merged.extend(direita[j:])
#
#     return merged
#
#
# lista = [4, 7, 1, 9, 3, 5, 2, 8, 6, 8, 6, 10, 18, 4]
# lista_organizada = merge_sort(lista)
# print(lista_organizada)


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#
#     pivot = arr[len(arr) // 2]
#
#
#     smaller = [x for x in arr if x < pivot]
#     equal = [x for x in arr if x == pivot]
#     larger = [x for x in arr if x > pivot]
#
#
#     sorted_smaller = quick_sort(smaller)
#     sorted_larger = quick_sort(larger)
#
#
#     sorted_arr = sorted_smaller + equal + sorted_larger
#     return sorted_arr


# Exemplo de uso
# arr = [4, 7, 1, 9, 3, 5, 2, 8, 6]
# sorted_arr = quick_sort(arr)
# print(sorted_arr)
#
#
# def partition(lista, incio=0, fim=None):
#     if fim is None:
#         fim = len(lista)-1
#     pivot = lista[fim]  # escolhendo o pivô como o último elemento
#     smaller_idx = incio - 1  # índice do último elemento menor que o pivô
#
#     for i in range(incio, fim):
#         if lista[i] <= pivot:
#             smaller_idx += 1
#             lista[i], lista[smaller_idx] = lista[smaller_idx], lista[i]
#
#     lista[smaller_idx + 1], lista[fim] = lista[fim], lista[smaller_idx + 1]
#     return smaller_idx + 1
#
# def quick_sort(lista, incio, fim):
#     if incio < fim:
#         pivot_idx = partition(lista, incio, fim)
#
#         quick_sort(lista, incio, pivot_idx - 1)  # ordenando a sublista à esquerda do pivô
#         quick_sort(lista, pivot_idx + 1, fim)  # ordenando a sublista à direita do pivô
def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p-1)
        quicksort(lista, p+1, fim)


def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for m in range(inicio, fim):
        if lista[m] <= pivot:
            lista[m], lista[i] = lista[i], lista[m]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i


# Exemplo de uso
lista = [4, 7, 1, 9, 3, 5, 2, 8, 6]
tamanho = len(lista)
quick_sort(lista, 0)
print(lista)











