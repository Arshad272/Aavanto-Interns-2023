# inheritance 
class parent:
    def parent_display(self):
        print('parent class')

class child(parent):
    def child_display(self):
        print('child class')

class grandchild(child):
    def grandchild_display(self):
        print('grandchild class')

# print('parent class object')
# obj = parent()
# obj.parent_display()

# print('child class object')
# obj1 = child()
# obj1.child_display()
# obj1.parent_display()

print('grandchild class object')
obj2 = grandchild()
obj2.parent_display()
obj2.child_display()
obj2.grandchild_display()

