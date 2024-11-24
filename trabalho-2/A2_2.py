from A1_1 import Grafo
import sys
from collections import deque

def ordenacao_topologica(grafo: Grafo):
    # Calcula o grau de entrada de cada vértice
    grau_entrada = [0] * grafo.qtdVertices()
    for v in range(grafo.qtdVertices()):
        for vizinho in grafo.vizinhos(v + 1):
            grau_entrada[vizinho - 1] += 1

    # Fila para processar os vértices com grau de entrada zero
    fila = deque([v + 1 for v in range(grafo.qtdVertices()) if grau_entrada[v] == 0])
    ordem_topologica = []

    while fila:
        v = fila.popleft()
        ordem_topologica.append(grafo.rotulo(v))

        for vizinho in grafo.vizinhos(v):
            grau_entrada[vizinho - 1] -= 1
            if grau_entrada[vizinho - 1] == 0:
                fila.append(vizinho)

    if len(ordem_topologica) != grafo.qtdVertices():
        raise ValueError("O grafo possui um ciclo e, portanto, não pode ser ordenado topologicamente.")

    return ordem_topologica

def main():
    if len(sys.argv) != 2:
        print("Uso: python A2_1.py <caminho_para_arquivo_de_grafo>")
        return

    caminho_arquivo = sys.argv[1]
    grafo = Grafo(caminho_arquivo)
    ordem_topologica = ordenacao_topologica(grafo)
    print("→".join(ordem_topologica))

if __name__ == "__main__":
    main()
