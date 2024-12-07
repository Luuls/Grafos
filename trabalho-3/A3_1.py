from A1_1 import Grafo

def edmonds_karp(grafo, source, sink):
    from collections import deque

    n = grafo.qtdVertices()
    parent = [-1] * n
    max_flow = 0

    def bfs(s, t):
        visited = [False] * n
        queue = deque()
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.popleft()
            for v in range(n):
                if not visited[v] and grafo.grafo[u].relacoes[v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
        return False

    while bfs(source, sink):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, grafo.grafo[parent[s]].relacoes[s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            grafo.grafo[u].relacoes[v] -= path_flow
            grafo.grafo[v].relacoes[u] += path_flow
            v = parent[v]
    return max_flow

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print(f"Uso: python {sys.argv[0]} <arquivo_grafo> <vertice_origem> <vertice_destino>")
        sys.exit(1)

    arquivo_grafo = sys.argv[1]
    vertice_origem = int(sys.argv[2]) - 1
    vertice_destino = int(sys.argv[3]) - 1

    grafo = Grafo(arquivo_grafo)
    max_flow = edmonds_karp(grafo, vertice_origem, vertice_destino)
    if max_flow == float('inf'):
        print("O fluxo máximo é infinito.")
    else:
        print(int(max_flow))