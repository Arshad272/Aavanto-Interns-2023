class car:
    #class variables
    wheels = 4
    #contructor function
    def __init__(self,name,model):
        #instance variables
        self.name = name
        self.model = model


obj1 = car('benz','sclass')
obj2 = car('audi','r8')

print(obj1.wheels)
print(obj2.wheels)