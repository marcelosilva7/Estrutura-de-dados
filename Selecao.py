lista_selecao = [51, 61, 91, 41, 1, 57, 85, 90, 31, 10]
# menor pro maior complexidade 0 de n
tamanho = len(lista_selecao)
for m in range(tamanho -1):
    menor_numero = m
    for c in range(m + 1, tamanho):
        if lista_selecao[c] < lista_selecao[menor_numero]:
            menor_numero = c
    if menor_numero != m:
        lista_selecao[m], lista_selecao[menor_numero] = lista_selecao[menor_numero], lista_selecao[m]
print(lista_selecao)



lista_insercao = [20, 10, 31, 57, 61, 52, 87, 91, 25, 30]
# menor pro maior
tamanho1 = len(lista_insercao)
for i in range(1, tamanho1):
    valor = lista_insercao[i]
    p = i - 1
    while p >= 0 and lista_insercao[p] > valor:
        lista_insercao[p + 1] = lista_insercao[p]
        p -= 1
    lista_insercao[p + 1] = valor

print(lista_insercao)

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







