def initialize(V, E):
    dct = {}
    for i in V:
        if i not in dct.keys():
            dct[i] = []
    for i in E:
        dct[i[0]].append(i[1])
        dct[i[1]].append(i[0])
    return dct


V = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'S']
E = [('A', 'S'), ('S', 'B'), ('A', 'B'), ('A', 'D'), ('C', 'S'), ('C', 'B'), ('B', 'D'), ('B', 'F'), ('B', 'G'),
     ('F', 'E'), ('F', 'H'), ('H', 'G'), ('C', 'F'), ('D', 'E'), ('G', 'E')]
graph = initialize(V, E)
print("Do thi:")
print(graph)


def DFS(V, S, G, graph):
    lst_vertex = []
    queue = [S]

    visited = {}
    for i in V:
        visited[i] = False

    while len(queue) != 0:
        top = queue.pop(0)
        lst_vertex.append(top)
        visited[top] = True
        find = G in lst_vertex
        if top == G:
            return lst_vertex, find
        for i in graph[top]:
            if not visited[i] and i not in queue:
                queue.insert(0, i)
    # find = G in queue
    return lst_vertex, False


visited = {}
for i in V:
    visited[i] = False


def DFS_dequy(S, G, graph):
    queue = [S]
    lst_vertex = []

    while len(queue) != 0:
        top = queue.pop(0)
        lst_vertex.append(top)
        visited[top] = True
        if top == G:
            return lst_vertex
        for i in graph[top]:
            if not visited[i] and i not in queue:
                queue.extend(DFS_dequy(i, G, graph))
    return lst_vertex


print("Duong di:")
''''
path, tim = DFS(V, 'A', 'N', graph)
if tim:
    print(path)
else:
    print("khong tim thay duong di")
'''
path = DFS_dequy('S', 'G', graph)
if 'G' in path:
    print(path)
else:
    print("khong tim thay duong di")
