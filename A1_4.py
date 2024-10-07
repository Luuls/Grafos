import heapq
from A1_1 import Grafo 
import sys

def dijkstra(grafo: Grafo, origem: int):
    distancias = [Grafo.nao_existe] * grafo.qtdVertices()
    caminhos = [[] for _ in range(grafo.qtdVertices())]
    
    distancias[origem - 1] = 0
    caminhos[origem - 1] = [origem]
    
    fila_prioridade = [(0, origem - 1)]  
    
    while fila_prioridade:
        dist_atual, vertice_atual = heapq.heappop(fila_prioridade)
        
        for vizinho in grafo.vizinhos(vertice_atual + 1):
            peso = grafo.peso(vertice_atual, vizinho - 1)
            nova_dist = dist_atual + peso
            
            if nova_dist < distancias[vizinho - 1]:
                distancias[vizinho - 1] = nova_dist
                caminhos[vizinho - 1] = caminhos[vertice_atual] + [vizinho]
                heapq.heappush(fila_prioridade, (nova_dist, vizinho - 1))
    
    for i in range(grafo.qtdVertices()):
        if distancias[i] == Grafo.nao_existe:
            print(f"{i + 1}: Não alcançável")
        else:
            caminho_str = ",".join(map(str, caminhos[i]))
            print(f"{i + 1}: {caminho_str}; d={distancias[i]}")
    

def main():
    grafo = Grafo(sys.argv[1])
    vertice_inicial = int(sys.argv[2])
    dijkstra(grafo, vertice_inicial)

main()