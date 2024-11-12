def funcao1(n):
    for i in range(n):
        print(i)

def funcao2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

def funcao3(n):
    if n <= 1:
        return n
    return funcao3(n-1) + funcao3(n - 2)


#Questão 2
#https://www.geeksforgeeks.org/python-program-for-quicksort/
def ordena_quick(arr):
    if len(arr) <= 1:
        return arr
    pi = arr[len(arr) // 2]  
    esquerda = [x for x in arr if x < pi]
    meio = [x for x in arr if x == pi]
    direita = [x for x in arr if x > pi]
    return ordena_quick(esquerda) + meio + ordena_quick(direita)


arr = [32, 17, 73, 9, 3, 99, 11]
arr_ordenado = ordena_quick(arr)
print(arr_ordenado)

#Questão 4
def ordenar_pilha(pilha):
    pilha_temp = []
    while pilha:
        nota_atual = pilha.pop()

        while pilha_temp and pilha_temp[-1] > nota_atual:
            pilha.append(pilha_temp.pop())
        pilha_temp.append(nota_atual)
    
    while pilha_temp:
        pilha.append(pilha_temp.pop())

pilha_notas = [25, 50, 10, 15, 14, 88]
print("Pilha priomaria:", pilha_notas)
ordenar_pilha(pilha_notas)

#Questão 5
def tarefa_no_topo(pilha_de_tarefas):
    if pilha_de_tarefas:
        return pilha_de_tarefas[-1]  
    else:
        return None  

pilha_de_tarefas = ['Fazer questão 1', 'Fazer questão 2', 'Fazer questão 3']
print("última tarefa na pilha", tarefa_no_topo(pilha_de_tarefas))  


#Questão 6
def contar_impares(pilha_pedidos):
    contador_impares = 0
    
    for pedido in pilha_pedidos:
        if pedido % 2 != 0:
            contador_impares += 1
    
    return contador_impares

pilha_pedidos = [511, 522, 533, 514, 555, 516, 756]
print("ímpar", contar_impares(pilha_pedidos))


#Questão 7
def contar_pares(pilha_pedidos):
    contador_pares = 0
    
    for pedido in pilha_pedidos:
        if pedido % 2 == 0:
            contador_pares += 1
    
    return contador_pares

pilha_pedidos = [511, 522, 533, 514, 555, 516, 756]
print("par", contar_pares(pilha_pedidos))

#Questão 9
def ordenar_fila(lista):
    n = len(lista)
    for i in range(n):
        menor = i
        for j in range(i+1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista
lista = [64, 34, 25, 12, 22, 11, 90]
print(ordenar_fila(lista))

#Questão 10
def contar_livros_impares(fila_de_livros):
    contador_impares = 0
    for livro in fila_de_livros:
        if livro % 2 != 0:
            contador_impares += 1
    return contador_impares
fila_de_livros = [101, 102, 103, 104, 105, 106, 107]
print(contar_livros_impares(fila_de_livros))
