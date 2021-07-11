import click
from .contexto import compilador


@click.command()
@click.option("-o","--opção", help="Compile ou Execute")
@click.option("-e","--entrada", prompt="Arquivo a ser compilado",help="Nome do arquivo que sera compilado ou executado")
@click.option("-s","--saida", default="arquivoCompilado.py", help="Nome do arquivo compilado (padrão é arquivoCompilado.py) ")

def main(opção, entrada, saida):

    scriptFile = open(entrada, "r")
    lines = scriptFile.readlines()
    newScript = compilador( lines )

    if opção == "execute":
        exec(newScript)
    elif opção == "compile":
        with open(saida, "w") as f:
            f.write(newScript)
    else:
        print("Opção invalida")

if __name__ == "__main__":
    main()