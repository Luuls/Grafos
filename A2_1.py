from A1_1 import Grafo
import sys

def cfc(grafo: Grafo):
    def busca_em_largura(v, visitado, pilha):
        visitado[v] = True
        for vizinho in grafo.vizinhos(v + 1):
            if not visitado[vizinho - 1]:
                busca_em_largura(vizinho - 1, visitado, pilha)
        pilha.append(v)

    def busca_em_largura_transposto(v, visitado, componente):
        visitado[v] = True
        componente.append(v + 1)
        for vizinho in grafo.vizinhos_transposto(v + 1):
            if not visitado[vizinho - 1]:
                busca_em_largura_transposto(vizinho - 1, visitado, componente)

    pilha = []
    visitado = [False] * grafo.qtdVertices()

    for i in range(grafo.qtdVertices()):
        if not visitado[i]:
            busca_em_largura(i, visitado, pilha)

    grafo.transpor()

    visitado = [False] * grafo.qtdVertices()
    componentes = []

    while pilha:
        v = pilha.pop()
        if not visitado[v]:
            componente = []
            busca_em_largura_transposto(v, visitado, componente)
            componentes.append(componente)

    return componentes

if __name__ == "__main__":
    grafo = Grafo(sys.argv[1])
    componentes = cfc(grafo)
    for componente in reversed(componentes):
        print(*componente, sep=',')
    
