from grafo import Grafo
import heapq

def dijkstra(grafo: Grafo, inicio: int):
    # Inicializações
    distancias = {v: Grafo.nao_existe for v in range(1, grafo.qtdVertices() + 1)}
    distancias[inicio] = 0
    antecessores = {v: None for v in range(1, grafo.qtdVertices() + 1)}

    fila_prioridade = [(0, inicio)]  # Fila de prioridade inicializada com o nó de início

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[vertice_atual]:
            continue

        for vizinho in grafo.vizinhos(vertice_atual):
            distancia = distancia_atual + grafo.peso(vertice_atual - 1, vizinho - 1)

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                antecessores[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    return distancias, antecessores

def construir_caminho(antecessores, vertice):
    caminho = []
    while vertice is not None:
        caminho.append(vertice)
        vertice = antecessores[vertice]
    return caminho[::-1]  # Inverte o caminho para mostrar do início ao destino

def imprimir_caminhos_e_distancias(grafo: Grafo, distancias, antecessores, inicio):
    for vertice in range(1, grafo.qtdVertices() + 1):
        if distancias[vertice] == Grafo.nao_existe:
            print(f"{grafo.rotulo(vertice)}: Sem caminho")
        else:
            caminho = construir_caminho(antecessores, vertice)
            caminho_str = ",".join(grafo.rotulo(v) for v in caminho)
            print(f"{grafo.rotulo(vertice)}: {caminho_str}; d={distancias[vertice]}")

# Exemplo de uso
# Assumindo que o arquivo do grafo esteja no caminho "grafo.txt"
grafo = Grafo("arquivo.txt")
vertice_inicial = 2  # Escolha o vértice de início

distancias, antecessores = dijkstra(grafo, vertice_inicial)
imprimir_caminhos_e_distancias(grafo, distancias, antecessores, vertice_inicial)
