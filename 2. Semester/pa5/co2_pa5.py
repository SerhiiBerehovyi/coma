class Node:
    def __init__(self, key: int, left=None, right=None, parent=None):
        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balance = 0

    def balancesUpdate(self):
        balanceLeft = -1
        balanceRight = -1

        if self.leftChild is not None:
            self.leftChild.balancesUpdate()
            balanceLeft = self.leftChild.hight()
        if self.rightChild is not None:
            self.rightChild.balancesUpdate()
            balanceRight = self.rightChild.hight()

        self.balance = balanceRight - balanceLeft

    def hightLeft(self):
        if self.leftChild is None:
            return -1
        return self.leftChild.hight()

    def hightRight(self):
        if self.rightChild is None:
            return -1
        return self.rightChild.hight()

    def hight(self):
        hightLeft = 0
        hightRight = 0
        if self.leftChild is not None:
            hightLeft += self.leftChild.hight() + 1
        if self.rightChild is not None:
            hightRight += self.rightChild.hight() + 1

        return max(hightLeft, hightRight)


class AVLTree:
    def __init__(self, key: int):
        self.root = Node(key)

    def insrt(self, key, node):
        if node.key > key:
            if node.leftChild is not None:
                self.insrt(key, node.leftChild)
            else:
                node.leftChild = Node(key, parent=node)
        else:
            if node.rightChild is not None:
                self.insrt(key, node.rightChild)
            else:
                node.rightChild = Node(key, parent=node)

        node.balancesUpdate()
        if abs(node.balance) > 1:
            if node.hightLeft() > node.hightRight():
                # to right
                self.rotateLeft(node)
            else:
                self.rotateRight(node)
                # to left

    def insert(self, key):
        self.insrt(key, self.root)

    def rotateRight(self, x):
        y = x.leftChild
        if x.parent is None:
            self.root = y
        elif x.parent.leftChild is x:
            x.parent.leftChild = y
        else:
            x.parent.rightChild = y

        y.parent = x.parent
        x.leftChild = y.rightChild
        if x.leftChild is not None:
            x.leftChild.parent = x

        y.rightChild = x
        x.parent = y

    def rotateLeft(self, x):
        y = x.rightChild
        if x.parent is None:
            self.root = y
        elif x.parent.leftChild is x:
            x.parent.leftChild = y
        else:
            x.parent.rightChild = y

        y.parent = x.parent
        x.rightChild = y.leftChild
        if x.rightChild is not None:
            x.rightChild.parent = x

        y.leftChild = x
        x.parent = y
