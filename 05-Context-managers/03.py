

from contextlib import contextmanager

@contextmanager
def MyFileManager(filename,mode):
    file = open(filename,mode)
    try:
        yield file
    finally:
        file.close()
        
with MyFileManager('file.txt','r') as file:
    data = file.read()
    print(data)