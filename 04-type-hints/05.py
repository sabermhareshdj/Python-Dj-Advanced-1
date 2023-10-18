
#def add_employee(name:str,age:int=0):  
#   if not age :
#       print(f' my name is {name}')
# else:
#    print(f'my name is {name} - age {age}')        
#add_employee('ahmad', 25)
#add_employee('ali')
    
from typing import Optional
def add_employee(name:str,age:Optional[int]=None) -> str:
    if not age :
       print(f' my name is {name}')
    else:
      print(f'my name is {name} - age {age}')        
add_employee('ahmad', 25)
add_employee('ali','ali')