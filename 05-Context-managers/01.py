# open --> close ----> context manager : with [open : auto close]

with open('file.txt','r') as file:
    data = file.read()
    print(data)
    
# auto close