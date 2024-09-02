from A1_1 import Graph

def solve(filePath: str, s_index: int):
    graph = Graph(filePath)
    vertex_info = {}
    
    for i in range(graph.qtdVertices()):
        vertex_info[i+1] = [False, float('inf'), None, i+1]
    
    vertex_info[s_index][0] = True
    vertex_info[s_index][1] = 0

    queue = [vertex_info[s_index]]

    while len(queue) != 0:
        u = queue.pop()
        for neighbor in graph.vizinhos(u[3]):
            if vertex_info[neighbor][0] == False:
                vertex_info[neighbor][0] = True
                vertex_info[neighbor][1] = u[1] + 1
                vertex_info[neighbor][2] = u
                queue.append(vertex_info[neighbor])
    
    d = [[] for i in range(graph.qtdVertices())]
    for info in vertex_info.values():
        d[info[1]].append(info[3])
    
    for i in range(len(d)):
        if d[i]:
            print(f"{i}: {', '.join(map(str, d[i]))}")

def main():
    solve('arquivo.txt', 1)    

if __name__ == '__main__':
    main()