class MyClass():
    counter = 0
    def __init__(self):
        type(self).counter += 1

    @classmethod
    def count(cls):
        print("Total objects: ", cls.counter)
        
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

print(MyClass.count())

'''
Really strange task. We need to count copy of class obj
But there is poor description of test, so i can't pass it) 
itresume solution: 
    counter = 0
    def __init__(self):
        MyClass.counter += 1
        
    @classmethod
    def count(cls):
        return cls.counter
'''