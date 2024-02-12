from controller import *
from menu import *

def main():

    arquivoClientes = 'appdecorridas/clientes.txt'
    if not arquivoExiste(arquivoClientes):
        criarArquivo(arquivoClientes)

    while True:
        menuPrincipal()
        op = input(str('Digite a opção desejada: \n'))

        if op == '1':
            menuCliente()
            op_cliente = input(str('Digite a opção desejada: '))

            if op_cliente == '1':
                cadastraCliente(arquivoClientes)

            elif op_cliente == '2':
                consultaClientes()

            elif op_cliente == '3':
                listaClientes()

            elif op_cliente == '0':
                print('Saindo do MENU cliente...')

            else:
                print('Opção Inválida')

        elif op == '4':
            break

main()

