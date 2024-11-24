from A1_1 import Grafo
import sys


class ConjuntoDisjunto:
    def __init__(self, tamanho):
        self.pai = [i for i in range(tamanho)]
        self.rank = [0] * tamanho

    def find(self, u):
        if self.pai[u] != u:
            self.pai[u] = self.find(self.pai[u])  # Compressão de caminho
        return self.pai[u]

    def union(self, u, v):
        raiz_u = self.find(u)
        raiz_v = self.find(v)
        if raiz_u == raiz_v:
            return False  # Já estão no mesmo conjunto
        if self.rank[raiz_u] < self.rank[raiz_v]:
            self.pai[raiz_u] = raiz_v
        else:
            self.pai[raiz_v] = raiz_u
            if self.rank[raiz_u] == self.rank[raiz_v]:
                self.rank[raiz_u] += 1
        return True

def kruskal(grafo: Grafo):
    # Obter todas as arestas do grafo
    arestas = []
    for v1 in range(grafo.qtdVertices()):
        for v2 in range(v1 + 1, grafo.qtdVertices()):
            if grafo.haAresta(v1 + 1, v2 + 1):
                peso = grafo.grafo[v1].relacoes[v2]
                if peso != None:
                    arestas.append((peso, v1, v2))

    # Ordenar as arestas pelo peso
    arestas.sort()

    uf = ConjuntoDisjunto(grafo.qtdVertices())

    agm_peso_total = 0.0
    agm_arestas = []
    for peso, u, v in arestas:
        if uf.union(u, v):
            agm_peso_total += peso
            agm_arestas.append(f"{u + 1}-{v + 1}")

    print(f"{agm_peso_total}")
    print(", ".join(agm_arestas))


if __name__ == '__main__':
    grafo = Grafo(sys.argv[1])
    kruskal(grafo)
