class reactangle:
    def __init__(self,L,B):
        self.L=L
        self.B=B
    def show(self):
        print("length=",self.L)
        print("breadth=",self.B)
    def area(self):
        return self.L*self.B
    def perimeter(self):
        print("perimeter=",2*(self.L*self.B))
r=reactangle(3,5)
r.show()
print("area of reactangle=",r.area())
print("perimeter=",r.perimeter())