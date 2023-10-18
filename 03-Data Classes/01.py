#no data classess

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def __str__(self):
        return (f"name : {self.name} - age: {self.age}")

p1 = Person('mahmoud',25)
print(p1.name)
print(p1.age)
print(p1)

