"""
Created on May 24 2021
@author: Leonardo
"""

import math

grafoLido = []
matrix = []
item = []

# Lê o arquivo txt contendo a matriz de adjacências
file = open('A_pesos_1s2021.txt', 'r')
data = file.readlines()

# Percorre a matriz de strings lida e separa cada elemento da string
for i in data:
    matrix.append(i.split())
# Percorre cada elemento obtido transformando os pesos em inteiro
for j in matrix:
    for k in j:
        if k == "inf":
            item.append(k)
        else:
            item.append(int(k))
# Monta a matriz de adjacências
    grafoLido.append(item)
    item = []
file.close()




class HeapMin:

    def __init__(self):
        self.nos = 0
        self.heap = []

    def adiciona_no(self, u, indice):
        # Adiciona os nós na lista da árvore. Lembrete: listaArvore = [pai,filhoEsquerda, filhoDireita, ...]
        self.heap.append([u, indice])
        # conta o número de nós
        self.nos += 1
        # Passa a posição do último elemento da listaArvore para o f
        f = self.nos
        while True:
            # se estiver na raiz sai do while e não troca posições na árvore
            if f == 1:
                break
            p = f // 2
            # se o pai for menor que o filho sai do while e não troca posições na árvore
            if self.heap[p - 1][0] <= self.heap[f - 1][0]:
                break
            else:
                # se o pai for maior que o flho troca as posições na árvore
                self.heap[p - 1], self.heap[f - 1] = self.heap[f - 1], self.heap[p - 1]
                # Atualiza a posição do f para ser comparado ao próximo pai
                f = p

    def mostra_heap(self):
        print('A estrutura heap é a seguinte:')
        nivel = int(math.log(self.nos, 2))
        a = 0
        for i in range(nivel):
            for j in range(2 ** i):
                print(f'{self.heap[a]}', end='  ')
                a += 1
            print('')
        for i in range(self.nos - a):
            print(f'{self.heap[a]}', end='  ')
            a += 1
        print('')

    def remove_no(self):
        # Armazena a primeira posição da árvore
        x = self.heap[0]
        # Passa o valor do primeiro nó para a primeira posição da árvore
        self.heap[0] = self.heap[self.nos - 1]
        # Exclui o valor da última posição da árvore
        self.heap.pop()
        # Subtrai um nó do número de nós
        self.nos -= 1
        # Posição considerada do primeiro elemento na árvore (sistemicamente ela é 0)
        p = 1
        while True:
            # Para pegar a posição do filho à esquerda
            f = 2 * p
            # Testa se a posição do filho esquerdo existe na árvore senão saí do while
            if f > self.nos:
                break
            # Testa se a posição do filho à direita existe na árvore
            if f + 1 <= self.nos:
                # compara se o filho da direita( f + 1(-1 por conta do python começar em 0) = f) é maior do que o filho da esquerda (f-1)
                if self.heap[f][0] < self.heap[f - 1][0]:
                    # se sim trabalharemos com o filho da direita
                    f += 1
            # Testa se o Pai já é menor do que o filho se sim, não precisa trocar de posição
            if self.heap[p - 1][0] <= self.heap[f - 1][0]:
                break
            else:
                # Se o pai não é menor que o filho troca a posição na árvore
                self.heap[p - 1], self.heap[f - 1] = self.heap[f - 1], self.heap[p - 1]
                p = f
        return x

    def tamanho(self):
        return self.nos


class Grafo:

# Inicia um construtor
    def __init__(self, grafo):
        self.grafo = grafoLido
        self.vertices = len(self.grafo)

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(len(self.grafo)):
            print(self.grafo[i])
        print(self.vertices)

    def dijkstra(self, origem):
        # Configura uma lista com uma sublista para cada vértice. Cada sublista contém uma configuração inicial para: [peso, pos do nó]
        custo_vem = [[-1, 0] for i in range(self.vertices)]
        # Configura o primeiro nó como origem
        custo_vem[origem - 1] = [0, origem]
        h = HeapMin()
        h.adiciona_no(0, origem)
        while h.tamanho() > 0:
            dist, v = h.remove_no()
            for i in range(self.vertices):
                if self.grafo[v - 1][i] != 'inf':
                    if custo_vem[i][0] == -1 or custo_vem[i][0] > dist + self.grafo[v - 1][i]:
                        custo_vem[i] = [dist + self.grafo[v - 1][i], v]
                        h.adiciona_no(dist + self.grafo[v - 1][i], i + 1)
        return custo_vem

# Instancia a classe grafo
g = Grafo(grafoLido)

'''g.mostra_matriz()'''

resultado_dijkstra = g.dijkstra(1)
for i in range (len(resultado_dijkstra)):
    print("Vértice", int(i+1))
    print(resultado_dijkstra[i][0])
