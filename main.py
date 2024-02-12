from controller import *
from menu import *

def main():

    arquivoClientes = 'appdecorridas/clientes.txt'

    if not arquivoExiste(arquivoClientes):
        criarArquivo(arquivoClientes)

    cadastraCliente(arquivoClientes)

listaTodosClientes()




