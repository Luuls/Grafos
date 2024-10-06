from A1_1 import Grafo


def floyd_warshall(grafo: Grafo):
    # Número de vértices
    n = grafo.qtdVertices()
    
    # Inicializa a matriz de distâncias com os pesos do grafo ou Grafo.nao_existe para arestas inexistentes
    distancias = [[Grafo.nao_existe] * n for _ in range(n)]
    
    # Preenche a matriz de distâncias com os pesos das arestas
    for i in range(n):
        distancias[i][i] = 0  # Distância para si mesmo é sempre 0
        for j in range(n):
            if grafo.haAresta(i + 1, j + 1):
                distancias[i][j] = grafo.peso(i, j)
    
    # Algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distancias[i][j] > distancias[i][k] + distancias[k][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]

    return distancias

def imprimir_matriz_distancias(distancias):
    n = len(distancias)
    for i in range(n):
        linha = f"{i+1}:"
        linha += ",".join(str(int(dist)) if dist != Grafo.nao_existe else "inf" for dist in distancias[i])
        print(linha)

# Exemplo de uso
# Assumindo que o arquivo do grafo esteja no caminho "grafo.txt"
grafo = Grafo("grafo.txt")
distancias = floyd_warshall(grafo)
imprimir_matriz_distancias(distancias)
