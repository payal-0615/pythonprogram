class Test:
    def __init__(self, x=0, y=0):   
        self.x = x
        self.y = y
t1 = Test()         
t2 = Test(15, 6)     
print(t1.x, t1.y)
print(t2.x, t2.y)