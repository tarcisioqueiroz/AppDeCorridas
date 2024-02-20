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
        print('Digite a opção desejada:')
        op = input(str('>>> '))

        if op == '1':
            menuCliente()
            print('Digite a opção desejada: ')
            op_cliente = input(str('>>> '))

            if op_cliente == '1':
                cadastraCliente(arquivoClientes)

            elif op_cliente == '2':
                consultaClientes(arquivoClientes)

            elif op_cliente == '3':
                listaClientes(arquivoClientes)

            elif op_cliente == '0':
                print('Saindo do MENU cliente...\n')

            else:
                print('Opção Inválida')

        elif op == '2':
            menuMotorista()
            print("Digite a opção desejada: ")
            op_motorista = input(str('>>> '))

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

            menuCorrida()
            print("Digite a opção desejada: ")
            op_corrida = input(str('>>> '))

            if op_corrida == '1':
                cadastraCorrida(arquivoClientes, arquivoMotoristas, arquivoCorridasEmAndamento)

            elif op_corrida == '2':
                finalizaCorrida(arquivoCorridasEmAndamento, arquivoCorridasFinalizadas, arquivoMotoristas)
            
            elif op_corrida == '3':
                consultaMotoristasON(arquivoMotoristas)

            elif op_corrida == '4':
                consultaCorridaMotorista(arquivoMotoristas, arquivoCorridasEmAndamento)

            elif op_corrida == '5':
                consultaCorridaCliente(arquivoClientes, arquivoCorridasEmAndamento)

            elif op_corrida == '6':
                listaCorridas(arquivoCorridasEmAndamento, arquivoCorridasFinalizadas)
        
            elif op_corrida == '7':
                print('Saindo do MENU corrida...\n')

            else:
                print('Opção inválida')
               
        elif op == '4':
            break

main()