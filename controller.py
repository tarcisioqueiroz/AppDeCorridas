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
        
