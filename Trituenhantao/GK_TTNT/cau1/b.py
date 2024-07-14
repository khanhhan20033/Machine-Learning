import networkx as nx
import matplotlib.pyplot as plt


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


def BFS(V, S, G, graph):
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
                queue.append(i)
    # find = G in queue
    return lst_vertex, False


path, tim = BFS(V, 'S', 'G', graph)
if tim:
    # print("Duong di:")
    for i in range(1, len(path) + 1):
        print("explored")
        print(path[0:i])
    # print(path)
else:
    print("khong tim thay duong di")


def visualize_search(V, E, path):
    G = nx.Graph()
    G.add_nodes_from(V)
    G.add_edges_from(E)

    pos = nx.spring_layout(G)  # Positions for all nodes

    plt.figure(figsize=(8, 6))

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=12)

    # Draw explored edges
    for i in range(1, len(path)):
        nx.draw_networkx_edges(G, pos, edgelist=[(path[i - 1], path[i])], width=2.0, alpha=1, edge_color='red')

    plt.title('BFS Search Visualization')
    plt.show()


# Call the visualization function
visualize_search(V, E, path)
