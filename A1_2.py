from collections import deque
from A1_1 import Grafo
import sys

def busca_em_largura(grafo, vertice_inicial) -> None:
    # Lista para marcar os vértices visitados
    visitado = [False] * grafo.qtdVertices()
    
    # Fila para processar os vértices
    fila = deque([vertice_inicial])
    
    # Inicialmente, o vértice inicial foi visitado
    visitado[vertice_inicial - 1] = True
    
    # Nível atual
    nivel_atual = 0
    
    # Dicionário para armazenar os vértices por nível
    niveis = {nivel_atual: [vertice_inicial]}

    while fila:
        # Número de vértices no nível atual
        num_vertices_nivel = len(fila)
        
        # Lista para armazenar os vértices do próximo nível
        proximos_vertices = []

        # Processa todos os vértices do nível atual
        for _ in range(num_vertices_nivel):
            vertice = fila.popleft()
            
            # Percorre os vizinhos do vértice atual
            for vizinho in grafo.vizinhos(vertice):
                if not visitado[vizinho - 1]:
                    visitado[vizinho - 1] = True
                    fila.append(vizinho)
                    proximos_vertices.append(vizinho)

        # Incrementa o nível se houver novos vértices para processar
        if proximos_vertices:
            nivel_atual += 1
            niveis[nivel_atual] = proximos_vertices
    
    # Impressão dos níveis e seus vértices
    for nivel, vertices in niveis.items():
        print(f"{nivel}: {','.join(map(str, vertices))}")

def main():
    busca_em_largura(Grafo(sys.argv[1]), int(sys.argv[2]))

main()