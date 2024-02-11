from controller import *
from menu import *

def main():

    listaClientes = 'clientes.txt'

    if not arquivoExiste(listaClientes):
        criarArquivo(listaClientes)

    cadastraCliente(listaClientes)

consultaClientes()

    

