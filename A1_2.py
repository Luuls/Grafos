from grafo import Grafo

def busca_em_largura(caminho_arquivo: str, vertice_s: int):
    grafo = Grafo(caminho_arquivo)
    vertice_info = {}
    
    for i in range(grafo.qtdVertices()):
        vertice_info[i+1] = [False, float('inf'), None, i+1]
    
    vertice_info[vertice_s][0] = True
    vertice_info[vertice_s][1] = 0

    fila = [vertice_info[vertice_s]]

    while len(fila) != 0:
        u = fila.pop()
        for neighbor in grafo.vizinhos(u[3]):
            if vertice_info[neighbor][0] == False:
                vertice_info[neighbor][0] = True
                vertice_info[neighbor][1] = u[1] + 1
                vertice_info[neighbor][2] = u
                fila.append(vertice_info[neighbor])
    
    d = [[] for i in range(grafo.qtdVertices())]
    for info in vertice_info.values():
        d[info[1]].append(info[3])
    
    for i in range(len(d)):
        if d[i]:
            print(f"{i}: {', '.join(map(str, d[i]))}")

busca_em_largura('arquivo.txt', 1)
