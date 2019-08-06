## 1. Introduction ##

l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}

print(type(l))
print(type(s))
print(type(d))

## 3. Defining a Class ##

class NewList():
    pass

## 4. Instantiating a Class ##

class NewList(DQ):
    pass

newlist_1 = NewList()
print(type(newlist_1))

## 5. Creating Methods ##

class NewList(DQ):
    def first_method():
        return "This is my first method"
    
newlist = NewList()

## 6. Understanding 'self' ##

class NewList(DQ):
    def first_method(self):
        return "This is my first method"
    
newlist = NewList()
result = newlist.first_method()

## 7. Creating a Method That Accepts an Argument ##

class NewList(DQ):
    def return_list(self,input_list):
        return input_list
    
newlist = NewList()
result = newlist.return_list([1,2,3])

## 8. Attributes and the Init Method ##

class NewList(DQ):
    def __init__(self, initial_state):
        self.data = initial_state
        
my_list = NewList([1,2,3,4,5])
print(my_list.data)

## 9. Creating an Append Method ##


class NewList(DQ):
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state):
        self.data = initial_state
        
    def list_append(self,n):
        self.data.append(n)
        
my_list = NewList([1,2,3,4,5])
print(my_list.data)
my_list.list_append(6)
print(my_list.data)