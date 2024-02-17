from pathlib import Path
import random

clientes = []
motoristas = []
corridasEmAndamento = []
corridasFinalizadas = []

def criaPastaArquivos():
    caminho_do_arquivo = Path(__file__).resolve().parent
    pastaarquivos = 'src'

    caminhoPastaArquivos = caminho_do_arquivo / pastaarquivos

    if not caminhoPastaArquivos.exists():
        caminhoPastaArquivos.mkdir()
        print(f'Pasta {pastaarquivos} criada com sucesso!')

    return caminhoPastaArquivos

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!');

def cadastraCliente(arquivo):
    global clientes
    atualizaBase(arquivo)
    with open(arquivo, 'a') as a:
        cliente = {}
        cliente['nome'] = input(str('digite seu nome e sobrenome: '))
        cliente['cpf'] = input(str('digite o número do CPF: '))
        cliente['contato'] = input(str('digite seu email ou telefone: '))
        
        cliente_existe = any(c['cpf'] == cliente['cpf'] for c in clientes)

        if cliente_existe:
            print('Cliente já cadastrado!')
        else:
            a.write(str(cliente) + '\n')
            print('Cliente cadastrado com sucesso!')
        
    atualizaBase(arquivo)
        
def consultaClientes():
    atualizaBase('appdecorridas/clientes.txt')
    global clientes
    elementoBusca = input(str('Digite o cpf do cliente: '))
        
    for cliente in clientes:
        if elementoBusca == cliente['cpf']:
            print(f'o cliente {cliente["nome"]} foi encontrado!')
            return
        
    print('Cliente não encontrado!')

def listaClientes():
    atualizaBase('appdecorridas/clientes.txt')
    global clientes
    for cliente in clientes:
        print(cliente['nome'])
                
def atualizaBase(arquivo):
    global clientes
    with open(arquivo, 'r') as a:
        for linha in a:
            cliente = eval(linha.strip())
            if cliente not in clientes:
                clientes.append(cliente)

#motoristas
        
def cadastraMotorista(arquivo):
    global motoristas
    atualizaBaseMotorista(arquivo)
    with open(arquivo, 'a') as a:
        motorista = {}
        motorista['nome'] = input(str('digite seu nome e sobrenome: '))
        motorista['cpf'] = input(str('digite o número do CPF: '))
        motorista['contato'] = input(str('digite seu email ou telefone: '))
        motorista['placa'] = input(str('digite a placa do seu carro: '))
        motorista['carro'] = input(str('digite o modelo do carro: '))
        motorista['disp'] = True
        
        motorista_existe = any(c['cpf'] == motorista['cpf'] for c in motoristas)

        if motorista_existe:
            print('Motorista já cadastrado!')
        else:
            a.write(str(motorista) + '\n')
            print('Motorista cadastrado com sucesso!')
        
    atualizaBaseMotorista(arquivo)

def consultaMotoristas(arquivo):
    atualizaBaseMotorista(arquivo)
    global motoristas
    elementoBusca = input(str('Digite o cpf do motorista: \n'))
        
    for motorista in motoristas:
        if elementoBusca == motorista['cpf']:
            print(f'o motorista {motorista["nome"]} foi encontrado!')
            return
    
    print('Motorista não encontrado!')

def consultaPlacas(arquivo):
    atualizaBaseMotorista(arquivo)
    global motoristas
    elementoBusca = input(str('Digite a placa do carro: '))
        
    for motorista in motoristas:
        if elementoBusca == motorista['placa']:
            print(f'a placa {motorista["placa"]} foi encontrada e pertence ao {motorista["nome"]}!')
            return
    
    print('Placa não encontrada!')

def listaMotoristas(arquivo):
    atualizaBaseMotorista(arquivo)
    global motoristas
    for motorista in motoristas:
        print(motorista['nome'])

def atualizaBaseMotorista(arquivo):
    global motoristas
    with open(arquivo, 'r') as a:
        for linha in a:
            motorista = eval(linha.strip())
            if motorista not in motoristas:
                motoristas.append(motorista)

#corridas

def cod_corrida(corrida):
    while True:
        chaveAleatoria = random.randint(100000, 999999)
        corrida['COD'] = chaveAleatoria
        cod_existe = any(c['COD'] == corrida['COD'] for c in corridasEmAndamento)

        if cod_existe:
            continue

        else:
            corrida['COD'] = chaveAleatoria
            break

def cadastraCorrida(arquivoC, arquivoM, arquivoCEA):
    atualizaBase(arquivoC)
    atualizaBaseMotorista(arquivoM)
    atualizaCorridasAtivas(arquivoCEA)

    global corridasEmAndamento
    global clientes
    global motoristas

    with open (arquivoCEA,'a') as a:
        corrida = {}

        while True:
            cod_corrida(corrida)
            while True:
                cpfCliente = input(str('Digite o cpf do cliente:\n'))
                corrida['CPFcliente'] = cpfCliente
                validaClienteCorrida = any(c['CPFcliente'] == corrida['CPFcliente'] for c in corridasEmAndamento)
                clientexiste = any(c['cpf'] == corrida['CPFcliente'] for c in clientes)

                if clientexiste:
                    if validaClienteCorrida:
                        print('este cliente já se encontra em uma corrida')
                        op_cliente = input(str('deseja realizar um novo cadastro:\n1 - sim\n2 - não\n'))
                        if op_cliente == '1':
                            continue
                        else:
                            return
                    else:
                        for cliente in clientes:
                            if cliente['cpf'] == corrida['CPFcliente']:
                                corrida['nomeCliente'] = cliente['nome']
                                corrida['contatoCliente'] = cliente['contato']
                            
                        break
                else:
                    print('cliente não encontrado na base')
                    op_cliente = input(str('deseja cadastrar um novo cliente:\n1 - sim\n2 - não\n'))
                    if op_cliente == '1':
                        cadastraCliente(arquivoC)
                        print('\nInsira novamente os dados do cliente para cadastrar a corrida\n')
                        continue
                    else:
                        return
                    
            while True:
                for motorista in motoristas:
                    if motorista['disp'] == True:
                        motoristaAtual= motorista
                        corrida['CPFmotorista'] = motorista['cpf']
                        corrida['nomeMotorista'] = motorista['nome']
                        motorista['disp'] = False
                        motoristas[motoristas.index(motorista)] = motoristaAtual
                        
                        with open (arquivoM, 'w') as b:
                            for motorista in motoristas:
                                b.write(str(motorista) + '\n')

                        break
                    else:
                        print('Nenhum motorista disponível no momento, tente novamente mais tarde')

                break

            a.write(str(corrida) + '\n')
            atualizaBaseMotorista(arquivoM)
            break


def atualizaCorridasAtivas(arquivo):
    global corridasEmAndamento
    with open(arquivo, 'r') as a:
        for linha in a:
            corrida = eval(linha.strip())
            if corrida not in corridasEmAndamento:
                corridasEmAndamento.append(corrida)