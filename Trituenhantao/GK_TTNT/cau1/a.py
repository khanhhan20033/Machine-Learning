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