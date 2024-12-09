import sys
from A1_1 import Grafo

def eh_conjunto_estavel(grafo: Grafo, subconjunto: int) -> bool:
    # Verifica se o subconjunto representado por 'subconjunto' (bitmask)
    # é um conjunto independente, ou seja, não há aresta entre quaisquer dois vértices nele.
    vertices = []
    n = grafo.qtdVertices()
    for v in range(n):
        if (subconjunto & (1 << v)) != 0:
            vertices.append(v+1)  # +1 porque o grafo é indexado a partir de 1
    # Verificação de arestas
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            if grafo.haAresta(vertices[i], vertices[j]):
                return False
    return True

def lawler_coloring(grafo: Grafo):
    n = grafo.qtdVertices()
    # dp[S] = número mínimo de cores para colorir os vértices no subconjunto S
    # choice[S] = subconjunto independente que gera a solução ótima
    tamanho = 1 << n
    dp = [float('inf')] * tamanho
    choice = [-1] * tamanho
    dp[0] = 0

    # Pré-cálculo: gerar todos subconjuntos estáveis
    # Para otimizar um pouco, vamos guardar todos os subconjuntos estáveis
    conjuntos_estaveis = []
    for S in range(tamanho):
        if eh_conjunto_estavel(grafo, S):
            conjuntos_estaveis.append(S)
        else:
            conjuntos_estaveis.append(-1)  # marca não-estável

    for S in range(1, tamanho):
        # Encontra o dp[S]
        # dp[S] = 1 + min_{I estavel em S} dp[S \ I]
        # Testa todos subconjuntos estáveis I contidos em S
        # Em vez de iterar sobre todos sub-subconjuntos, iteramos pelos pré-calculados
        # e verificamos se I está contido em S.
        for I in range(tamanho):
            if conjuntos_estaveis[I] != -1:  # I é estável
                I_estavel = I
                # Verifica se I_estavel está contido em S: (S & I_estavel) == I_estavel
                if I_estavel != -1 and (I_estavel & S) == I_estavel:
                    resto = S ^ I_estavel
                    if dp[resto] + 1 < dp[S]:
                        dp[S] = dp[resto] + 1
                        choice[S] = I_estavel
    
    # dp[(1<<n)-1] guarda o número mínimo de cores
    # Agora reconstruir a solução
    cor_atribuida = [0]*n
    S = (1 << n) - 1
    cor_atual = dp[S]

    # A cada passo choice[S] nos dá o conjunto independente que usamos
    # Esses vértices receberão a cor cor_atual
    while S != 0:
        I = choice[S]
        # Atribuir cor cor_atual aos vértices em I
        for v in range(n):
            if (I & (1 << v)) != 0:
                cor_atribuida[v] = cor_atual
        S = S ^ I
        cor_atual -= 1

    return dp[(1<<n)-1], cor_atribuida

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 programa.py <caminho_arquivo>")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]
    grafo = Grafo(caminho_arquivo)
    num_cores, atribuicoes = lawler_coloring(grafo)

    # Imprime o número de cores
    print(num_cores)
    # Imprime as cores dos vértices na ordem (1...n)
    # As cores estão atribuídas no array "atribuicoes" (0-based), mas já corretas
    print(", ".join(map(str, atribuicoes)))