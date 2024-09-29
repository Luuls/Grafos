from dataclasses import dataclass

@dataclass
class Aresta:
    v1: int
    v2: int
    peso: float

class Vertice:
    def __init__(self, rotulo: str, grau: int, relacoes: list[float]):
        self.rotulo = rotulo
        self.grau = grau
        self.relacoes = relacoes
        self.list_vizinhos: list[list[int]] = []
        self.arestas: list[Aresta]

    def __str__(self) -> str:
        return str(self.relacoes)

    def __repr__(self) -> str:
        return self.__str__()

class Grafo:

    nao_existe = float('inf')

    def __init__(self, caminho_arquivo: str) -> None:
        self.grafo: list[Vertice] = []
        self.qtd_arestas: int
        self.lista_vizinhos: list[list[int]]
        self.arestas: list[Aresta] = []
        self.__ler_arquivo(caminho_arquivo)

    def qtdVertices(self) -> int:
        return len(self.grafo)

    def qtdArestas(self) -> int:
        return self.qtd_arestas

    def grau(self, vertice: int) -> int:
        return self.grafo[vertice - 1].grau

    def rotulo(self, vertice: int) -> str:
        return self.grafo[vertice - 1].rotulo

    def vizinhos(self, vertice: int) -> list[int]:
        return self.lista_vizinhos[vertice - 1]

    def peso(self, v1: int, v2: int) -> float:
        return self.grafo[v1].relacoes[v2]

    def haAresta(self, v1: int, v2: int) -> bool:
        return self.grafo[v1 - 1].relacoes[v2 - 1] != Grafo.nao_existe

    def __ler_arquivo(self, caminho_arquivo: str) -> None:
        with open(caminho_arquivo, 'r') as arquivo:
            tag = ""
            numero_de_vertices = 0
            rotulos: list[str] = []
            for linha in arquivo:
                if "*vertices" in linha:
                    tag = "vertices"
                    numero_de_vertices = int(linha.split()[1])
                    rotulos = ['' for _ in range(numero_de_vertices)]
                    self.lista_vizinhos = [
                        [] for _ in range(numero_de_vertices)
                    ]

                elif "*edges" in linha:
                    tag = "edges"

                elif tag == "vertices":
                    indice, rotulo = linha.split()
                    indice = int(indice)
                    rotulos[indice - 1] = rotulo

                elif tag == "edges":
                    vertice1, vertice2, peso = linha.split()
                    vertice1 = int(vertice1)
                    vertice2 = int(vertice2)
                    peso = float(peso)
                    self.arestas.append(Aresta(vertice1 - 1, vertice2 - 1, peso))

            for i in range(numero_de_vertices):
                self.grafo.append(
                    Vertice(
                        rotulos[i],
                        0,
                        [Grafo.nao_existe for _ in range(numero_de_vertices)]
                    )
                )
            for aresta in self.arestas:
                # opera simetricamente, pois o grafo é não-dirigido
                self.grafo[aresta.v1] \
                    .relacoes[aresta.v2] = aresta.peso
                self.grafo[aresta.v2] \
                    .relacoes[aresta.v1] = aresta.peso

                self.lista_vizinhos[aresta.v1].append(aresta.v2 + 1)
                self.lista_vizinhos[aresta.v2].append(aresta.v1 + 1)

            self.qtd_arestas = len(self.arestas)

    def obterArestasSemRepeticao(self):
        # Retorna todas as arestas do grafo, considerando que (3,4) é igual a (4,3)
        arestas = []
        for l, vertice in enumerate(self.grafo):  # `vertice` é um objeto `Vertice`
            for c, peso in enumerate(vertice.relacoes):  # Acessa as relações (pesos)
                # Verifica se existe uma aresta entre l e c (peso != infinito)
                if self.haAresta(l + 1, c + 1) and (c + 1, l + 1) not in arestas:
                    arestas.append((l + 1, c + 1))
        return arestas[:]


"""
grafo = Grafo('arquivo.txt')
print(grafo.obterArestasSemRepeticao())
print(grafo.qtdVertices())
print(grafo.qtdArestas())
print(grafo.grau(1))
print(grafo.vizinhos(1))
print(grafo.peso(1,2))
print(grafo.haAresta(1, 2))
print(grafo.haAresta(2, 3))
print(grafo.haAresta(3, 1))
print(grafo.grafo)
for i in range(grafo.qtdVertices()):
    print(grafo.rotulo(i + 1))
"""