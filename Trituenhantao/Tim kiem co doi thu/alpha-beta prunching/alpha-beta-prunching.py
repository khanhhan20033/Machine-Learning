class Node:
    def __init__(self, name, value=0):
        self.name = name
        self.cost = value
        self.children = []

    def setValue(self, value):
        self.cost = value

    def getValue(self):
        return self.cost

    def addChild(self, child):
        for c in child:
            self.children.append(c)


def alpha_beta(node: Node, alpha, beta, maximizing):
    if len(node.children) == 0:
        return node
    if maximizing:
        node.cost = -100000
        for i in node.children:
            temp = alpha_beta(i, alpha, beta, False)
            if temp.cost > node.cost:
                node.cost = temp.cost
            if beta <= node.cost:
                return node
            if alpha < node.cost:
                alpha = node.cost
        return node
    else:
        node.cost = 100000
        for i in node.children:
            temp = alpha_beta(i, alpha, beta, True)
            if temp.cost < node.cost:
                node.cost = temp.cost
            if alpha >= node.cost:
                return node
            if beta > node.cost:
                beta = node.cost
        return node


if __name__ == '__main__':
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    F = Node('F')
    G = Node('G')
    H = Node('H')
    I = Node('I')
    J = Node('J')
    K = Node('K')
    M = Node('M')
    N = Node('N')
    L = Node('L')
    Z = Node('Z')
    A.addChild([B, C])
    B.addChild([D, E])
    C.addChild([F, G])
    D.addChild([H, I])
    E.addChild([J, K])
    F.addChild([M, N])
    G.addChild([L, Z])
    H.setValue(2)
    I.setValue(9)
    J.setValue(7)
    K.setValue(4)
    M.setValue(8)
    N.setValue(9)
    L.setValue(3)
    Z.setValue(5)
    print(f'A:{alpha_beta(A, -1000000, 1000000, True).getValue()}')
