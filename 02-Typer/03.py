import typer

def toupper(name:str , uppercase:bool=False): # 
    if uppercase:
        print(name.upper())
    else:
        print(name)
    
if __name__ == "__main__":
    typer.run(toupper)