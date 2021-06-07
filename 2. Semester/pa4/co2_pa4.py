class Set:
    def __init__(self, V: list ):
        self._elements = sorted(V)

    def Elements(self):
        return self._elements

    def __str__(self):
        return str(self._elements)

class Partition:
    def __init__(self, V):
        self.Sets = []
        V.sort()
        for i in range(1, len(V)):
            if V[i] == V[i-1]:
                raise Exception("invalid operation")

        for el in V:
            self.Sets.append(Set([el]))

    def __str__(self):
        s = "["
        for set in self.Sets:
            s += str(set) + ','
        return s[:-1] + ']'

    def MakeSet(self, n):
        for s in self.Sets:
            if n in s._elements:
                raise Exception("invalid operation")
        self.Sets.append(Set([n]))

    def FindSet(self, n):
        for set in self.Sets:
            if n in set._elements:
                return set.Elements()[0]
        raise Exception("invalid operation")

    def Union(self, a, b):
        s1 = self.find(a)
        s2 = self.find(b)
        self.Sets.append(Set(s1._elements + s2._elements))

    def find(self, a):
        if a != self.FindSet(a):
            raise Exception("invalid operation")
        for s in self.Sets:
            if a in s._elements:
                return self.Sets.pop(self.Sets.index(s))



if __name__ == "__main__":
    S =  Partition( [ ( 0 , 3 )  , ( 0 , 1 )  , ( 1 , 3 )  , ( 1 , 0 ) ] )
    print(S)
    S.Union((1, 3), (0, 1))
    print(S)
    S.Union((0, 3), (0, 1))
    print(S)

    print()
    print(S.FindSet((1,3)))
    S.MakeSet((300,1))
    S.Union((300,1), (0,1))
    print(S)

    print()
    print(S.FindSet((300,1)))
    print()

    S.MakeSet((0,0))
    S.Union((0,0), (0,1))
    print(S.FindSet((300,1)))
    print(S)
