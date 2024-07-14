class Node:
    def __init__(self, name, cost):
        self.name = name
        self.children = []
        self.cost = cost

    def addChild(self, c):
        for i in c:
            self.children.append(i)


def comp(x: Node):
    return x.cost


def gbfs(start: Node, end: Node):
    explored = []
    queue = [start]
    while len(queue) != 0:
        top = queue.pop(0)
        explored.append(top)

        if top.name == end.name:
            return explored
        lst = []
        for i in top.children:
            if i not in (queue and explored):
                lst.append(i)
        lst.sort(key=comp,reverse=True)
        for i in lst:
            queue.insert(0, i)
    return explored


if __name__ == "__main__":
    NodeA = Node("A", 40)
    NodeB = Node("B", 32)
    NodeC = Node("C", 25)
    NodeD = Node('D', 35)
    NodeE = Node('E', 19)
    NodeF = Node('F', 17)
    NodeG = Node('G', 0)
    NodeH = Node('H', 10)
    NodeA.addChild([NodeD, NodeC, NodeB])
    NodeD.addChild([NodeA, NodeF])
    NodeB.addChild([NodeA, NodeE])
    NodeC.addChild([NodeF, NodeE, NodeA])
    NodeE.addChild([NodeH, NodeC, NodeB])
    NodeF.addChild([NodeG, NodeC, NodeD])
    NodeG.addChild([NodeH, NodeF])
    print("Duong di tu {0} toi {1}".format('A', 'G'))
    path = gbfs(NodeA, NodeG)
    for i in path:
        print(i.name+"->")
