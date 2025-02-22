from dataclasses import dataclass
import re

class Vertice:
    def __init__(self, rotulo: str, grau: int, relacoes: list):
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
        self.grafo: list = []
        self.qtd_arestas: int
        self.lista_vizinhos: list
        self.dirigido: bool = False
        self.__ler_arquivo(caminho_arquivo)

    def qtdVertices(self) -> int:
        return len(self.grafo)

    def qtdArestas(self) -> int:
        return self.qtd_arestas

    def grau(self, vertice: int) -> int:
        return self.grafo[vertice - 1].grau

    def rotulo(self, vertice: int) -> str:
        return self.grafo[vertice - 1].rotulo

    def vizinhos(self, vertice: int) -> list:
        return self.lista_vizinhos[vertice - 1]

    def peso(self, v1: int, v2: int) -> float:
        return self.grafo[v1].relacoes[v2]

    def haAresta(self, v1: int, v2: int) -> bool:
        return self.grafo[v1 - 1].relacoes[v2 - 1] != Grafo.nao_existe

    def transpor(self):
        grafo_transposto = [[] for _ in range(self.qtdVertices())]
        for v in range(self.qtdVertices()):
            for vizinho in self.vizinhos(v + 1):
                grafo_transposto[vizinho - 1].append(v + 1)
        self.lista_vizinhos = grafo_transposto

    def vizinhos_transposto(self, vertice: int) -> list:
        return self.lista_vizinhos[vertice - 1]

    def __ler_arquivo(self, caminho_arquivo: str) -> None:
        # para melhorar legibilidade
        @dataclass
        class Aresta:
            v1: int
            v2: int
            peso: float

        with open(caminho_arquivo, 'r') as arquivo:
            tag = ""
            numero_de_vertices = 0
            arestas: list = []
            rotulos: list = []
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
                    self.dirigido = False

                elif "*arcs" in linha:
                    tag = "arcs"
                    self.dirigido = True

                elif tag == "vertices":
                    # Verifica se a linha contém um rótulo entre aspas
                    if '"' in linha:
                        # Usamos uma expressão regular para separar o índice e o rótulo entre aspas
                        match = re.match(r'(\d+)\s+"(.*)"', linha)
                        if match:
                            indice = int(match.group(1))
                            rotulo = match.group(2)
                            rotulos[indice - 1] = rotulo
                    else:
                        # Caso contrário, considera o segundo valor como o rótulo numérico
                        indice, rotulo = linha.split()
                        rotulos[int(indice) - 1] = rotulo

                elif tag in ["edges", "arcs"]:
                    try:
                        vertice1, vertice2, peso = linha.split()
                        vertice1 = int(vertice1)
                        vertice2 = int(vertice2)
                        peso = float(peso)
                        arestas.append(Aresta(vertice1 - 1, vertice2 - 1, peso))
                    except:
                        pass

            for i in range(numero_de_vertices):
                self.grafo.append(
                    Vertice(
                        rotulos[i],
                        0,
                        [Grafo.nao_existe for _ in range(numero_de_vertices)]
                    )
                )

            for aresta in arestas:
                self.grafo[aresta.v1].relacoes[aresta.v2] = aresta.peso
                self.lista_vizinhos[aresta.v1].append(aresta.v2 + 1)
                if not self.dirigido:
                    self.grafo[aresta.v2].relacoes[aresta.v1] = aresta.peso
                    self.lista_vizinhos[aresta.v2].append(aresta.v1 + 1)

            self.qtd_arestas = len(arestas)
