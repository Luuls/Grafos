from A1_1 import Grafo
import random

def buscarSubcicloEuleriano(grafo: Grafo, v: int, arestas: list) -> list:        
    t = v
    ciclo = [t]
    while True:
        arestas_vizinhas_de_v = list(filter(lambda aresta: aresta[0] == v or aresta[1] == v, arestas))

        if not len(arestas_vizinhas_de_v):
            return None

        aresta_escolhida = random.choice(arestas_vizinhas_de_v)
        arestas.remove(aresta_escolhida)
        
        v = aresta_escolhida[0] if v == aresta_escolhida[1] else aresta_escolhida[1]
        ciclo.append(v)
        if v == t:
            break

    novo_ciclo = ciclo[:]
    for i, vertice_ciclo in enumerate(ciclo):
        counter = 0
        for vertice1, vertice2 in arestas:
            counter += 1
            if vertice1 == vertice_ciclo or vertice2 == vertice_ciclo:
                if vertice1 == vertice_ciclo:
                    subciclo = buscarSubcicloEuleriano(grafo, vertice1, arestas)
                else:
                    subciclo = buscarSubcicloEuleriano(grafo, vertice2, arestas)
                if not subciclo:
                    return None
                novo_ciclo = novo_ciclo[:i] + subciclo + novo_ciclo[i + 1:]

    return novo_ciclo
    
def hierholzer(grafo: Grafo):
    def obterArestasSemRepeticao(grafo):
        # Retorna todas as arestas do grafo, considerando que (3,4) é igual a (4,3)
        arestas = []
        for l, vertice in enumerate(grafo.grafo):  
            for c, peso in enumerate(vertice.relacoes):  
                if grafo.haAresta(l + 1, c + 1) and (c + 1, l + 1) not in arestas:
                    arestas.append((l + 1, c + 1))
        return arestas[:]
    arestas = obterArestasSemRepeticao(grafo)
    v = random.choice(arestas)[0]
    ciclo = buscarSubcicloEuleriano(grafo, v, arestas)

    if not ciclo:
        return None
    if len(arestas):
        return None
            
    return ciclo

grafo = Grafo("arquivo.txt")
ciclo_euleriano = hierholzer(grafo)

if ciclo_euleriano:
    print(f"1\n{', '.join(str(vertice) for vertice in ciclo_euleriano)}")
else:
    print("0")
