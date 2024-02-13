clientes = []
motoristas = []
corridas = []

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