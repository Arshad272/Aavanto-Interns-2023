class mammal:

    #class variable 
    species = 'mammal'
    
    #privatevariable
    __x = 'private'

    #contructor function or method
    def __init__(self,name=None):
        #instance variable
        self.name = name

    def display(self):
        print('name: ',self.name)
        print('species: ',self.species)
        print(self.__x)


    def __str__(self):
        return self.name


obj1 = mammal()
obj1.display()
print('outside the class')
print(obj1.species)
print(obj1.name)
print(obj1.__x)


#abstraction 