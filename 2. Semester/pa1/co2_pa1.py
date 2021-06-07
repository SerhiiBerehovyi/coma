class Node:
    """
        this class is a binary three with 3 instance variables:
            two children and key.

        @key is a key-value of Node.
             in case of PA it is an integer.
        @leftChild 	is a pointer on another Node.
                    it can be also None.
        @rightChild is also a pointer on None or None.
    """
    def __init__(self, key, leftChild, rightChild):
        """
            Constructor, that initializes instance variables of
            Node.
        """
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild

    def keys(self):
        """
            an recursive method, produce an array with
            all keys in a binary three.
            if left or right child is existing, calls
            a key()-method of this child.
            uses an extend()-method of an Array to add
            all keys of by children returned Arrays
        """
        res = [self.key]
        if self.leftChild is not None:
            res.extend(self.leftChild.keys())
        if self.rightChild is not None:
            res.extend(self.rightChild.keys())
        return res

    def height(self):
        """
            an recursive method. recursive iterates hight of
            children and returns a maximal of this both.
            if there is any child, adds 1 to returned child.hight()
            value.
        """
        heightLeft = 0
        heightRight = 0
        if self.leftChild is not None:
            heightLeft += self.leftChild.height() + 1
        if self.rightChild is not None:
            heightRight += self.rightChild.height() + 1
        return max(heightRight, heightLeft)

    def leaves(self):
        """
            an recursive method. checks if Node has any another children
            if it has, calls leaves() method by it's child or returns
            self.key, if it hasn't.
        """
        res = []
        if self.leftChild is None and self.rightChild is None:
            return [self.key]
        if self.leftChild is not None:
            res.extend(self.leftChild.leaves())
        if self.rightChild is not None:
            res.extend(self.rightChild.leaves())
        return res
