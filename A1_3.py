from grafo import Grafo

def buscar_subciclo_euleriano(grafo: Grafo, vertice: int, arestas_visitadas: dict):
    ciclo: list[int] = vertice
    vertice_tmp: int = vertice
    vizinhos_vertice: list[int] = grafo.vizinhos(vertice)
    while True:
        qtd_arestas_visitadas: int = 0
        for vizinho in vizinhos_vertice:
            try:
                if arestas_visitadas[(vertice, vizinho)] == True:
                    qtd_arestas_visitadas += 1
            except:
                if arestas_visitadas[(vizinho, vertice)] == True:
                    qtd_arestas_visitadas += 1
            if qtd_arestas_visitadas == len(arestas_visitadas):
                return False, None
    
        if vertice == vertice_tmp:
            break

def buscar_ciclo_euleriano(caminho_arquivo: str):
    grafo = Grafo(caminho_arquivo)
    arestas_visitadas: dict = {}
    for aresta in grafo.arestas:
        arestas_visitadas[(aresta.v1, aresta.v2)] = False

    # Talvez alterar para selecionar aleatoriamente
    vertice = grafo.arestas[0].v1



buscar_ciclo_euleriano("arquivo.txt")