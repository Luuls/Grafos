from dataclasses import dataclass


class Vertice:
    def __init__(self, rotulo: str, grau: int, relacoes: list[float]):
        self.rotulo = rotulo
        self.grau = grau
        self.relacoes = relacoes

    def __str__(self) -> str:
        return str(self.relacoes)

    def __repr__(self) -> str:
        return self.__str__()


class Grafo:

    nao_existe = float('inf')

    def __init__(self, caminho_arquivo: str) -> None:
        self.grafo: list[Vertice] = []
        self.qtd_arestas: int
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
        vizinhos: list[int] = []
        for vizinho, peso in enumerate(self.grafo[vertice - 1].relacoes):
            if peso != Grafo.nao_existe:
                vizinhos.append(vizinho)

        return vizinhos

    def peso(self, v1: int, v2: int) -> float:
        return self.grafo[v1].relacoes[v2]

    def __ler_arquivo(self, caminho_arquivo: str) -> None:
        # para melhorar legibilidade
        @dataclass
        class Aresta:
            vertice1: int
            vertice2: int
            peso: float

        with open(caminho_arquivo, 'r') as arquivo:
            tag = ""
            numero_de_vertices = 0
            arestas: list[Aresta] = []
            rotulos: list[str] = []
            for linha in arquivo:
                if "*vertices" in linha:
                    tag = "vertices"
                    numero_de_vertices = int(linha.split()[1])
                    rotulos = ['' for _ in range(numero_de_vertices)]

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
                    arestas.append(Aresta(vertice1 - 1, vertice2 - 1, peso))

            for i in range(numero_de_vertices):
                self.grafo.append(
                    Vertice(
                        rotulos[i],
                        0,
                        [Grafo.nao_existe for _ in range(numero_de_vertices)]
                    )
                )

            for aresta in arestas:
                self.grafo[aresta.vertice1].relacoes[aresta.vertice2] = aresta.peso

            self.qtd_arestas = len(arestas)

grafo = Grafo('arquivo.txt')

print(grafo.qtdVertices())
print(grafo.qtdArestas())
print(grafo.grau(1))
print(grafo.vizinhos(3))
print(grafo.peso(1,2))
print(grafo.grafo)

for i in range(grafo.qtdVertices()):
    print(grafo.rotulo(i + 1))
