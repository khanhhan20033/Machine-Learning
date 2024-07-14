class Node:
    def __init__(self, name, g, h):
        self.name = name
        self.g = g
        self.h = h
        self.children = []

    def update_g(self, j):
        self.g = self.g + j

    def addChild(self, child):
        for c in child:
            self.children.append(c)

    def cost(self):
        return self.h + self.g


def compare(a: Node):
    return a.cost()


def A_star(start: Node, end: Node):
    queue = [start]
    explored = []
    while len(queue) != 0:
        queue.sort(key=compare, reverse=False)
        top = queue.pop(0)
        explored.append(top.name)
        if top.h == 0:
            return explored
        for i in top.children:
            i.update_g(top.g)
            queue.append(i)
    return explored


if __name__ == "__main__":
    NodeA = Node("A", 0, 6)
    NodeB = Node('B', 2, 3)
    NodeC = Node('C', 1, 4)
    NodeD = Node('D', 3, 5)
    NodeE = Node('E', 5, 3)
    NodeF = Node('F', 4, 1)

    NodeG = Node('G', 6, 6)

    NodeH = Node('H', 3, 2)

    NodeI = Node('I', 2, 5)

    NodeJ = Node('J', 4, 4)
    NodeK = Node('K', 2, 2)
    NodeL = Node('L', 1, 0)
    NodeM = Node('M', 4, 4)
    NodeN = Node('N', 2, 0)
    NodeO = Node('O', 4, 4)
    NodeA.addChild([NodeB, NodeC, NodeD])
    NodeB.addChild([NodeE, NodeF])
    NodeC.addChild([NodeG, NodeH])
    NodeD.addChild([NodeI, NodeJ])
    NodeF.addChild([NodeK, NodeL, NodeM])
    NodeH.addChild([NodeN, NodeO])
    print("Duong di tu {0} toi {1} ".format('A', 'N'))
    path = A_star(NodeA, NodeN)
    for i in range(len(path)):
        print("explored:")
        print(path[0:i+1])
