from controller import *
from menu import *

def main():

    criaPastaArquivos()
    diretoriaAtual = criaPastaArquivos()

    nomeArquivoClientes = 'clientes.txt'
    arquivoClientes = diretoriaAtual / nomeArquivoClientes
    if not arquivoExiste(arquivoClientes):
        criarArquivo(arquivoClientes)

    nomeArquivoMotoristas = 'motoristas.txt'
    arquivoMotoristas = diretoriaAtual / nomeArquivoMotoristas
    if not arquivoExiste(arquivoMotoristas):
        criarArquivo(arquivoMotoristas)

    nomearquivoCorridasEmAndamento = 'corridasEmAndamento.txt'
    arquivoCorridasEmAndamento = diretoriaAtual / nomearquivoCorridasEmAndamento
    if not arquivoExiste(arquivoCorridasEmAndamento):
        criarArquivo(arquivoCorridasEmAndamento)

    nomeArquivoCorridasFlinalizadas = 'corridasFinalizadas.txt'
    arquivoCorridasFinalizadas = diretoriaAtual / nomeArquivoCorridasFlinalizadas
    if not arquivoExiste(arquivoCorridasFinalizadas):
        criarArquivo(arquivoCorridasFinalizadas)

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
                print('Saindo do MENU cliente...\n')

            else:
                print('Opção Inválida')

        elif op == '2':
            menuMotorista()
            op_motorista = input(str("Digite a opção desejada: "))

            if op_motorista == '1':
                cadastraMotorista(arquivoMotoristas)
            
            elif op_motorista == '2':
                consultaMotoristas(arquivoMotoristas)

            elif op_motorista == '3':
                consultaPlacas(arquivoMotoristas)
           
            elif op_motorista == '4':
                listaMotoristas(arquivoMotoristas)

            elif op_motorista == '5':
                print('Saindo do MENU motorista...\n')
            
            else:
                print("Opção inválida")

        elif op == '3':
            menuMotorista()
            op_motorista = input(str("Digite a opção desejada: "))

#        if op_motorista == '1':
#                cadastraCorrida(arquivoClientes, arquivoMotoristas, arquivoCorridasEmAndamento)
            

        elif op == '4':
            break

main()