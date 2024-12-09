from collections import deque
import sys
import re
from A1_1 import Grafo

def hopcroft_karp(grafo: Grafo):
    n = grafo.qtdVertices()
    meio = n // 2

    pair_u = [0] * (meio + 1)        # Índices: 1...meio
    pair_v = [0] * (n - meio + 1)    # Índices: 1...(n-meio)
    dist = [0] * (meio + 1)

    def bfs():
        fila = deque()
        for u in range(1, meio + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                fila.append(u)
            else:
                dist[u] = Grafo.nao_existe
        dist[0] = Grafo.nao_existe

        while fila:
            u = fila.popleft()
            if dist[u] < dist[0]:
                for viz in grafo.vizinhos(u):
                    if viz > meio:
                        v_indice = viz - meio
                        if dist[pair_v[v_indice]] == Grafo.nao_existe:
                            dist[pair_v[v_indice]] = dist[u] + 1
                            fila.append(pair_v[v_indice])
        return dist[0] != Grafo.nao_existe

    def dfs(u):
        if u != 0:
            for viz in grafo.vizinhos(u):
                if viz > meio:
                    v_indice = viz - meio
                    if dist[pair_v[v_indice]] == dist[u] + 1:
                        if dfs(pair_v[v_indice]):
                            pair_v[v_indice] = u
                            pair_u[u] = viz
                            return True
            dist[u] = Grafo.nao_existe
            return False
        return True

    matching = 0
    while bfs():
        for u in range(1, meio + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1

    emparelhamento = []
    for u in range(1, meio + 1):
        if pair_u[u] != 0:
            emparelhamento.append(f"{u}-{pair_u[u]}")

    return matching, emparelhamento

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 programa.py <caminho_arquivo>")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]
    grafo = Grafo(caminho_arquivo)
    matching, emparelhamento = hopcroft_karp(grafo)
    print(matching)
    print(", ".join(emparelhamento))
