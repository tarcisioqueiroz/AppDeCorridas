from controller import *
from menu import *

def main():

    listaClientes = 'appdecorridas/clientes.txt'

    if not arquivoExiste(listaClientes):
        criarArquivo(listaClientes)

    cadastraCliente(listaClientes)

consultaClientes()




