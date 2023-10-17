#annotaion   
import typer
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def add():
    pass


@app.command()
def delete(username , confirm:Annotated[bool,typer.Option(prompt="are your sure ? ")]):
    if confirm:
        print(f'deleteing user : {username}')
        
    else:
        print('operation canceld')    

if __name__ == "__main__":
    app()
