class MyClass:
    def hi(self):
        print("hello")

    def sum(self,x,y):
        self.x = x
        self.y = x

a1 = MyClass()#this is constructor
print(a1)
a1.sum(2,3)
print(a1.x)
