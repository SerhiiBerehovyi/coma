class IntVektor:
    """
        given class
    """
    def __init__(self, x, y, z):
        if type(x) != type(0) or type(y) != type(0) or type(z) != type(0):
           raise TypeError("Vektoreintrag keine ganze Zahl.")
        self.x=x
        self.y=y
        self.z=z

    def __str__(self):
        return '({0:n},{1:n},{2:n})'.format(self.x,self.y,self.z)

    def __getitem__(self,i):
        if type(i) != type(0):
           raise TypeError("Index keine ganze Zahl.")
        if i<0 or i>2:
           raise IndexError("Index nicht im zul. Bereich.")
        elif i==0:
           return self.x
        elif i==1:
           return self.y
        elif i==2:
           return self.z

    def __add__(self, other):
        if isinstance(other, IntVektor):
           return IntVektor(self.x+other.x,self.y+other.y,self.z+other.z)
        else:
           raise TypeError("Formate passen nicht.")

    def __mul__(self, other):
        if isinstance(other, IntVektor):
           return self.x * other.x + self.y * other.y + self.z * other.z
        elif type(other) == type(0):
           return IntVektor(self.x * other, self.y * other, self.z * other)
        else:
           raise TypeError("Formate passen nicht.")

    def __rmul__(self,other):
        if isinstance(other,IntVektor):
           return self.x * other.x + self.y * other.y + self.z * other.z
        elif type(other) == type(0):
           return IntVektor(self.x * other, self.y * other, self.z * other)
        else:
           raise TypeError("Formate passen nicht.")

    def copy(self):
        return IntVektor(self.x,self.y,self.z)


class Teilgitter(IntVektor):
    """
        class represents the partial grid G of IntVector.
        G = {k1*b1 + k2*b2 : k1,k2 \in Z}
        b1 = IntVektor(2,1,1)
        b2 = IntVektor(1,0,5)

        has additional attributes: Koordinate_1, Koordinate_2 (look at the assignment)
    """
    def __init__(self, x, y, z):
    """
        constructor of the class. input: coordinates of new vector
        :x: x-coordinate
        :y: y-coordinate
        :z: z-coordinate
    """
        self.Koordinate_1, self.Koordinate_2 = self.find_coordinates(x, y, z)
        super().__init__(x, y, z)

    def find_coordinates(self, x, y, z):
    """
        checks if given vector is an partitial grid of b1 and b2, throws an Exception if it's not
        :x: x-coordinate
        :y: y-coordinate
        :z: z-coordinate
    """
        k1 = y
        k2 = x - 2*k1
        if k1 + 5*k2 != z:
            raise Exception("Vektor liegt nicht im Teilgitter.")
        return k1, k2

    def __str__(self):
        return super().__str__() + "; Koordinate 1: {0:n}, Koordinate 2: {1:n}"\
            .format(self.Koordinate_1, self.Koordinate_2)

    def __add__(self, other):
        i = super().__add__(other)
        return Teilgitter(i.x, i.y, i.z)

    def __mul__(self, other):
        if isinstance(other, Teilgitter):
            return super().__mul__(other)
        elif isinstance(other, int):
            i = super().__mul__(other)
            return Teilgitter(i.x, i.y, i.z)

    def __rmul__(self, other):
        if isinstance(other, Teilgitter):
            return super().__rmul__(other)
        elif isinstance(other, int):
            i = super().__rmul__(other)
            return Teilgitter(i.x, i.y, i.z)

    def copy(self):
        return Teilgitter(self.x, self.y, self.z)


# simply tests
if __name__ == '__main__':
    a = Teilgitter(10, 3, 23)
    print(a)
    b = Teilgitter(14,4,34)
    print(b)
    print(a+b)
    print(3*a)
    print(-3*a)
    print(b*7)
    print(a*b)
    print(a.copy())
    print(Teilgitter(9, 5, 0))
