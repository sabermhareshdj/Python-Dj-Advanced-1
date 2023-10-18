from typing import List,Dict


def myfunction(person:Dict[str,str]) -> str:
    fname = person.get('fname')
    lname = person.get('lname') 
    return f"{fname} - {lname}"   

print(myfunction({'fname': 'mahmoud' , 'lname': 'saber'}))