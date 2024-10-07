from A1_1 import Grafo
import random
import sys

def buscarSubcicloEuleriano(grafo: Grafo, v: int, arestas: list) -> list:        
    t = v
    ciclo = [t]
    while True:
        # Filtra arestas que estão conectadas ao vértice atual
        arestas_vizinhas_de_v = list(filter(lambda aresta: aresta[0] == v or aresta[1] == v, arestas))

        # Se não houver mais arestas vizinhas, retorna None
        if not arestas_vizinhas_de_v:
            return None

        # Escolhe uma aresta e a remove da lista de arestas
        aresta_escolhida = arestas_vizinhas_de_v[0]  # Removendo o uso de random
        arestas.remove(aresta_escolhida)

        # Atualiza o vértice atual
        v = aresta_escolhida[0] if v == aresta_escolhida[1] else aresta_escolhida[1]
        ciclo.append(v)

        if v == t:
            break

    novo_ciclo = ciclo[:]
    for i, vertice_ciclo in enumerate(ciclo):
        while any(aresta[0] == vertice_ciclo or aresta[1] == vertice_ciclo for aresta in arestas):
            subciclo = buscarSubcicloEuleriano(grafo, vertice_ciclo, arestas)
            if not subciclo:
                return None
            novo_ciclo = novo_ciclo[:i] + subciclo + novo_ciclo[i+1:]

    return novo_ciclo

def hierholzer(grafo: Grafo):
    def obterArestasSemRepeticao(grafo):
        arestas = []
        for l, vertice in enumerate(grafo.grafo):  
            for c, peso in enumerate(vertice.relacoes):  
                if grafo.haAresta(l + 1, c + 1) and (c + 1, l + 1) not in arestas:
                    arestas.append((l + 1, c + 1))
        return arestas[:]

    arestas = obterArestasSemRepeticao(grafo)
    
    if not arestas:
        return None  # Se não há arestas, não há ciclo euleriano

    v = arestas[0][0]
    
    ciclo = buscarSubcicloEuleriano(grafo, v, arestas)

    if not ciclo or arestas:
        return None
            
    return ciclo

def main():
    grafo = Grafo(sys.argv[1])
    ciclo_euleriano = hierholzer(grafo)
    
    if ciclo_euleriano:
        print(f"1\n{', '.join(str(vertice) for vertice in ciclo_euleriano)}")
    else:
        print("0")

main()