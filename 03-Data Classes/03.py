from dataclasses import dataclass

@dataclass
class Person:
    name:str
    age:int
    
p1 = Person('mahmoud',25)

p2 = Person('ali',20)

p3 = Person('mahmoud',25)

print(p1 == p2)
print(p1 == p3)