class Graph:
    def __init__(self, filePath: str) -> None:
        # decidir a estrutura de dados da implementação (matriz, hash table...)
        self._graph = []
        self._vertex_index = {}         
        self.ler_arquivo(filePath)

    def qtdVertices(self) -> int:
        return len(self._graph)

    def qtdArestas(self) -> int:
        qtd_arestas = 0
        arestas_verificadas = []
        for i in range(self.qtdVertices()):
            for j in range(self.qtdVertices()):
                if self._graph[i][j] != float('inf') and (i,j) not in arestas_verificadas:
                    qtd_arestas += 1
                    arestas_verificadas.append((j, i))
        return qtd_arestas

    # TODO: `tipodovertice` a definir
    def grau(self, vertice: int) -> int:
        index = self._vertex_index[vertice] - 1
        grau = 0
        for j in range(self.qtdVertices()):
            if self._graph[index][j] != float('inf'):
                grau += 1
        return grau

    def rotulo(self, vertice: int) -> str:
        return self._vertex_index[vertice]

    def vizinhos(self, vertice: int) -> list[int]:
        index = self._vertex_index[vertice] - 1
        neighborhood = []
        for j in range(self.qtdVertices()):
            if self._graph[index][j] != float('inf'):
                for v, i in self._vertex_index.items():
                    if i - 1 == j:
                        neighborhood.append(v)
        return neighborhood

    def peso(self, v1: int, v2: int) -> int:
        return self._graph[self._vertex_index[v1]-1][self._vertex_index[v2]-1]

    def ler_arquivo(self, filePath: str) -> None:
        with open(filePath, 'r') as file:
            tag = ""
            number_of_vertex = 0
            edges = []
            for line in file:
                if "*vertices" in line:
                    tag = "vertices"
                    number_of_vertex = int(line[-2])
                elif "*edges" in line:
                    tag = "edges"

                elif tag == "vertices":
                    index = int(line[0: line.find(" ")])
                    vertice = int(line[12: line.find("\n")])
                    self._vertex_index[vertice] = index     
    
                elif tag == "edges":
                    vertex1 = int(line[0: line.find(" ")])
                    substring = line[2:]
                    vertex2 = int(substring[0:substring.find(" ")])
                    substring = line[4:]
                    value = int(line[4:])
                    edges.append((vertex1, vertex2, value))

            for i in range(number_of_vertex):
                line = []
                for j in range(number_of_vertex):
                    line.append(float('inf'))
                self._graph.append(line)
                
            for i in range(number_of_vertex):
                for j in range(number_of_vertex):
                    for edge in edges:
                        if (edge[0] == i + 1 and edge[1] == j + 1) or (edge[1] == i + 1 and edge[0] == j + 1):
                            self._graph[i][j] = edge[2]

               
grafo = Graph('arquivo.txt')

print(grafo.qtdVertices())
print(grafo.qtdArestas())
print(grafo.grau(1))
print(grafo.vizinhos(3))
print(grafo.peso(1,2))
print(grafo._graph)
