from grafo import Grafo
import random

def buscarSubcicloEuleriano(grafo: Grafo, v: int, arestas: list) -> list:
        
    # define o vertice inicial
    t = v
    ciclo = [t]
    while True:
        # pega todas arestas que estão ligadas a v
        arestas_vizinhas_de_v = list(filter(lambda aresta: aresta[0] == v or aresta[1] == v, arestas))

        # se nao existir nenhuma aresta ligada a v, então não ha caminho de volta para t
        # ou seja, nao se tem um ciclo euleriano
        if not len(arestas_vizinhas_de_v):
            return None

        # escolhe arbitrariamente uma aresta de v e a remove das arestas
        aresta_escolhida = random.choice(arestas_vizinhas_de_v)
        arestas.remove(aresta_escolhida)
        
        # pega o proximo vertice do ciclo
        v = aresta_escolhida[0] if v == aresta_escolhida[1] else aresta_escolhida[1]
        ciclo.append(v)
        # Se o proximo vertice for o inicial, fechamos um ciclo euleriano
        if v == t:
            break

    # Aqui se faz a busca por subciclos
    novo_ciclo = ciclo[:]
    for i, vertice_ciclo in enumerate(ciclo):
        for origem, _ in arestas:
            # Se ha alguma aresta não visistada ligada ao ciclo, entao se faz a busca por um subciclo
            if origem == vertice_ciclo:
                subciclo = buscarSubcicloEuleriano(grafo, origem, arestas)
                if not subciclo:
                    return None
                # insere o subciclo no meio do ciclo
                novo_ciclo = novo_ciclo[:i] + subciclo + novo_ciclo[i + 1:]

    return novo_ciclo
    

def hierholzer(grafo: Grafo):
    # obtêm todas arestas sem repeticao ((1,2) == (2,1)),
    # pois quando se visita a aresta (1,2) não é possível
    # voltar pela (2,1) (vide definição de um ciclo euleriano)
    arestas = grafo.obterArestasSemRepeticao()
    v = random.choice(arestas)[0]

    ciclo = buscarSubcicloEuleriano(grafo, v, arestas)
    if not ciclo:
        return None
    
    # vai excluindo as arestas da lista o algoritmo e se sobrar isso indica que tem aresta não visitada o que não deveria acontecer
    if len(arestas):
        return None
            
    return ciclo


grafo = Grafo("arquivo.txt")
ciclo_euleriano = hierholzer(grafo)

if ciclo_euleriano:
    print(f"1\n{', '.join(str(vertice) for vertice in ciclo_euleriano)}")
else:
    print("0")
