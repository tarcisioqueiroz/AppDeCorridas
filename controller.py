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

def cadastraCliente(arquivoC):
    global clientes
    atualizaBase(arquivoC)
    with open(arquivoC, 'a') as a:
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
        
    atualizaBase(arquivoC)
        
def consultaClientes(arquivoC):
    atualizaBase(arquivoC)
    global clientes
    elementoBusca = input(str('Digite o cpf do cliente: '))
        
    for cliente in clientes:
        if elementoBusca == cliente['cpf']:
            print(f'o cliente {cliente["nome"]} foi encontrado!')
            return
        
    print('Cliente não encontrado!')

def listaClientes(arquivoC):
    atualizaBase(arquivoC)
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
        
def cadastraMotorista(arquivo):
    global motoristas
    atualizaBaseMotorista(arquivo)
    with open(arquivo, 'a') as a:
        motorista = {}
        motorista['nome'] = input(str('digite seu nome e sobrenome: '))
        motorista['cpf'] = input(str('digite o número do CPF: '))
        motorista['contato'] = input(str('digite seu email ou telefone: '))
        tamanhoplacas = 7
        motorista['placa'] = input(str('digite a placa do seu carro, nos modelos\nABC1D23 ou ABC1234: '))
        while len(motorista['placa']) != tamanhoplacas:
            print('A placa na está em um padrão válido, digite novamente')
            motorista['placa'] = input(str('digite a placa do seu carro: '))
        motorista['carro'] = input(str('digite o modelo do carro: '))
        motorista['disp'] = True
        
        motorista_existe = any(c['cpf'] == motorista['cpf'] for c in motoristas)

        if motorista_existe:
            print('Motorista já cadastrado!')
        else:
            placaexistente = any(c['placa'] == motorista['placa'] for c in motoristas)
            if placaexistente:
                print('Placa já cadastrada!')
                opplaca = input(str('deseja recadastrar o motorista com outra placa?\n1 - sim\n2 - não\n'))
                if opplaca == '1':
                    cadastraMotorista(arquivo)
                else:
                    return
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

def cod_corrida(corrida):
    while True:
        chaveAleatoria = str(random.randint(100000, 999999))
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

                        print(f'Corrida cadastrada com sucesso!\nCódigo da corrida: {corrida["COD"]}')
                        a.write(str(corrida) + '\n')
                        atualizaBaseMotorista(arquivoM)

                        break
                else:
                    print('Nenhum motorista disponível no momento, tente novamente mais tarde')
                    continue
                break
            break

def finalizaCorrida(arquivoCEA, arquivoCF, arquivoM):
    atualizaCorridasAtivas(arquivoCEA)
    atualizaBaseMotorista(arquivoM)
    global motoristas
    global corridasEmAndamento
    global corridasFinalizadas
    corridaFinalizada = {}

    while True:
        cod = input(str('Digite o código da corrida: '))

        validaCodCorrida = any(c['COD'] == cod for c in corridasEmAndamento)

        if validaCodCorrida:
            for corrida in corridasEmAndamento:
                if corrida['COD'] == cod:
                    corridaFinalizada = corrida
                    corridasEmAndamento.remove(corrida)
                    corridasFinalizadas.append(corridaFinalizada)

                    for motorista in motoristas:
                        if motorista['cpf'] == corridaFinalizada['CPFmotorista']:
                            motoristaAtual = motorista
                            motorista['disp'] = True
                            motoristas[motoristas.index(motorista)] = motoristaAtual

                            with open(arquivoCEA, 'w') as a:
                                for corrida in corridasEmAndamento:
                                    a.write(str(corrida) + '\n')
                            with open(arquivoCF, 'a') as a:
                                a.write(str(corridaFinalizada) + '\n')
                            with open(arquivoM, 'w') as b:
                                for motorista in motoristas:
                                    b.write(str(motorista) + '\n')
                            print('Corrida finalizada com sucesso!')
                            return
        else:
            print('Código de corrida não encontrado!')
            op = input(str('deseja tentar novamente?\n1 - sim\n2 - não\n'))
            if op == '1':
                continue
            else:
                break

def consultaMotoristasON(arquivo2):
    atualizaBaseMotorista(arquivo2)
    global motoristas

    if any(motorista['disp'] for motorista in motoristas):
        print('Motoristas disponíveis para alugueis: ')
        
        for motorista in motoristas:
            if motorista['disp'] == True:
                print(f'- {motorista["nome"]}.')
    else:
        print('\nNão há motoristas disponíveis no momento...')
        print('Tente novamente mais tarde.')

def consultaCorridaMotorista(arquivoM, arquivoCEA):
    atualizaBaseMotorista(arquivoM)
    atualizaCorridasAtivas(arquivoCEA)
    global motoristas
    global corridasEmAndamento

    cpfMotorista = input(str('Digite o cpf do motorista: '))
    validaMotorista = any(m['cpf'] == cpfMotorista for m in motoristas)
    if validaMotorista:
        for motorista in motoristas:
            if motorista['cpf'] == cpfMotorista:
                for corrida in corridasEmAndamento:
                    if corrida['CPFmotorista'] == motorista['cpf']:
                        print(f'O motorista {motorista["nome"]} está em uma corrida com o código {corrida["COD"]}')
                        return
                print(f'O motorista {motorista["nome"]} não está em corrida no momento')
                return
    else:
        print('Motorista não encontrado na base')

def consultaCorridaCliente(arquivoC, arquivoCEA):
    atualizaBase(arquivoC)
    atualizaCorridasAtivas(arquivoCEA)
    global clientes
    global corridasEmAndamento

    cpfCliente = input(str('Digite o cpf do motorista: '))
    validaMotorista = any(m['cpf'] == cpfCliente for m in clientes)

    if validaMotorista:
        for cliente in clientes:
            if cliente['cpf'] == cpfCliente:
                for corrida in corridasEmAndamento:
                    if corrida['CPFcliente'] == cliente['cpf']:
                        print(f'O cliente {cliente["nome"]} está em uma corrida com o código {corrida["COD"]}')
                        return
                print(f'O cliente {cliente["nome"]} não está em corrida no momento')
                return
    else:
        print('Cliente não encontrado na base')

def listaCorridas(arquivoCEA, arquivoCF):
    atualizaCorridasAtivas(arquivoCEA)
    atualizaCorridasFinalizadas(arquivoCF)
    global corridasEmAndamento
    global corridasFinalizadas

    print('Corridas em andamento: \n')
    for corrida in corridasEmAndamento:
        print(f'Corrida {corrida["COD"]} - Cliente: {corrida["nomeCliente"]} - Motorista: {corrida["nomeMotorista"]}')

    print('\nCorridas finalizadas: \n')
    for corrida in corridasFinalizadas:
        print(f'Corrida {corrida["COD"]} - Cliente: {corrida["nomeCliente"]} - Motorista: {corrida["nomeMotorista"]}')

def atualizaCorridasAtivas(arquivo):
    global corridasEmAndamento
    with open(arquivo, 'r') as a:
        for linha in a:
            corrida = eval(linha.strip())
            if corrida not in corridasEmAndamento:
                corridasEmAndamento.append(corrida)

def atualizaCorridasFinalizadas(arquivoCF):
    global corridasFinalizadas
    with open(arquivoCF, 'r') as a:
        for linha in a:
            corrida = eval(linha.strip())
            if corrida not in corridasFinalizadas:
                corridasFinalizadas.append(corrida)