class Node:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value
        self.children = []

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def addChild(self, child):
        for c in child:
            self.children.append(c)


def compare(n: Node):
    return n.value


def maxvalues(max: Node):
    if len(max.children) == 0:
        return max
    lst = []
    for i in max.children:
        lst.append(minvalues(i))
    lst.sort(key=compare, reverse=True)
    max.setValue(lst[0].getValue())
    return max


def minvalues(max: Node):
    if len(max.children) == 0:
        return max
    lst = []
    for i in max.children:
        lst.append(maxvalues(i))
    lst.sort(key=compare, reverse=False)
    max.setValue(lst[0].getValue())
    return max


if __name__ == "__main__":
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
    print(f'A:{maxvalues(A).getValue()}')
    
