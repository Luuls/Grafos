from collections import deque
from A1_1 import Grafo
import sys

# Supondo que a classe Grafo esteja definida conforme fornecido anteriormente

def edmond_karp(grafo: Grafo, s: int, t: int) -> float:
    # Número de vértices
    n = grafo.qtdVertices()
    
    # Cria o grafo residual a partir das capacidades do grafo original
    # Se não houver aresta (valor = infinito no grafo original), capacidade = 0
    capacidade_residual = [[0] * n for _ in range(n)]
    for u in range(n):
        for v in range(n):
            peso = grafo.grafo[u].relacoes[v]
            if peso != float('inf'):
                capacidade_residual[u][v] = peso
    
    fluxo_maximo = 0.0

    while True:
        # Busca em Largura (BFS) para encontrar um caminho aumentante no grafo residual
        # parent[u] irá guardar o antecessor de u no caminho encontrado pela BFS
        parent = [-1] * n
        parent[s - 1] = -2  # Marca o vértice fonte (s) como visitado
        fila = deque()
        fila.append((s - 1, Grafo.nao_existe))  # (vértice, fluxo disponível até esse vértice)

        caminho_encontrado = False
        while fila:
            u, fluxo_atual = fila.popleft()
            for v in range(n):
                # Se a capacidade residual é > 0 e o vértice ainda não foi visitado
                if capacidade_residual[u][v] > 0 and parent[v] == -1:
                    parent[v] = u
                    # O fluxo até v será o mínimo entre o fluxo atual e a capacidade residual da aresta u->v
                    novo_fluxo = min(fluxo_atual, capacidade_residual[u][v])
                    if v == t - 1:
                        # Chegamos em t, atualizamos fluxo_maximo
                        fluxo_maximo += novo_fluxo
                        # Atualiza as capacidades residuais ao longo do caminho
                        w = v
                        while w != s - 1:
                            u_pai = parent[w]
                            capacidade_residual[u_pai][w] -= novo_fluxo
                            capacidade_residual[w][u_pai] += novo_fluxo
                            w = u_pai
                        caminho_encontrado = True
                        break
                    fila.append((v, novo_fluxo))
            if caminho_encontrado:
                break
        
        if not caminho_encontrado:
            # Não há mais caminho aumentante
            break

    return fluxo_maximo


if __name__ == "__main__":
    # Exemplo de execução
    # Suponhamos que o caminho do arquivo seja passado como argumento na linha de comando
    # e s e t também.
    # Ex: python3 programa.py caminho_do_arquivo_grafo.txt 1 4
    if len(sys.argv) < 4:
        print("Uso: python3 programa.py <caminho_arquivo> <s> <t>")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]
    s = int(sys.argv[2])
    t = int(sys.argv[3])

    grafo = Grafo(caminho_arquivo)
    resultado = edmond_karp(grafo, s, t)
    print(int(resultado))  # Imprime o fluxo máximo encontrado

