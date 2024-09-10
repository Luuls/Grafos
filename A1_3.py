from grafo import Grafo

def buscar_subciclo_euleriano(grafo: Grafo, vertice: int, arestas_visitadas: dict):
    
    def arestas_vizinhas_foram_visitadas(vertice: int, vizinhos: list[int]):
        # Quantidade de arestas visitadas no que diz respeito às arestas que se ligam ao vértice
        qtd_arestas_visitadas: int = 0
        for vizinho in vizinhos:
            try:
                if arestas_visitadas[(vertice, vizinho - 1)] == True:
                    qtd_arestas_visitadas += 1
            except:
                if arestas_visitadas[(vizinho - 1, vertice)] == True:
                    qtd_arestas_visitadas += 1
            if qtd_arestas_visitadas == len(vizinhos):
                return True
        return False
    
    def seleciona_aresta_nao_visitada(arestas_visitadas: dict) -> tuple:
        for aresta, visitada_bool in arestas_visitadas.items():
            if not visitada_bool:
                return aresta
    
    def vertices_do_ciclo_com_arestas_vizinhas_nao_visitadas(grafo: Grafo, ciclo: list[list[int]], arestas_visitadas: dict):
        for i in range(len(ciclo)):
            for vertice in ciclo[i]:
                for vizinho in grafo.vizinhos(vertice + 1):
                    try:
                        if arestas_visitadas[(vertice, vizinho - 1)] == False:
                            yield vertice
                    except:
                        if arestas_visitadas[(vizinho - 1, vertice)] == False:
                            yield vertice


    ciclo: list[list[int]] = [[]]
    ciclo[0].append(vertice)
    vertice_tmp: int = vertice
    
    while True:

        if arestas_vizinhas_foram_visitadas(vertice, grafo.vizinhos(vertice + 1)):
            return False, None
        
        else:
            aresta = seleciona_aresta_nao_visitada(arestas_visitadas)
            arestas_visitadas[aresta] = True
            vertice = aresta[1]
            ciclo.append([vertice])

        if vertice == vertice_tmp:
            break
    
    for vertice in vertices_do_ciclo_com_arestas_vizinhas_nao_visitadas(
        grafo, ciclo, arestas_visitadas):
        eh_ciclo_euleriano, ciclo_ = buscar_subciclo_euleriano(grafo, vertice, arestas_visitadas)
        
        if not eh_ciclo_euleriano:
            return False, None
        
        ciclo[ciclo.index([vertice])] = ciclo_

    return True, ciclo

def buscar_ciclo_euleriano(caminho_arquivo: str):
    grafo = Grafo(caminho_arquivo)
    arestas_visitadas: dict = {}
    for aresta in grafo.arestas:
        arestas_visitadas[(aresta.v1, aresta.v2)] = False

    # Talvez alterar para selecionar aleatoriamente
    vertice: int = grafo.arestas[0].v1

    eh_ciclo_euleriano, ciclo = buscar_subciclo_euleriano(grafo, vertice, arestas_visitadas)

    if eh_ciclo_euleriano:
        print(f'1\n{[", ".join(str(ciclo[i])) for i in range(len(ciclo))]}')




buscar_ciclo_euleriano("arquivo.txt")
