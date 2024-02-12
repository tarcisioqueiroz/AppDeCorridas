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
    with open(arquivo, 'a') as a:
        cliente = {}
        cliente['nome'] = input(str('Nome: '))
        cliente['cpf'] = input(str('CPF: '))
        cliente['cod'] = input(str('código do cliente: '))
        
        a.write(str(cliente) + '\n')
        atualizaBase(arquivo)

def atualizaBase(arquivo):
    global clientes
    with open(arquivo, 'r') as a:
        for linha in a:
            cliente = eval(linha.strip())
            clientes.append(cliente);
        
def consultaClientes():
    atualizaBase('clientes.txt')
    global clientes
    elementoBusca = input(str('Digite o nome do cliente: '))
    
    for cliente in clientes:
        if elementoBusca in cliente['nome']:
            print(f'o cliente {cliente['nome']} foi encontrado!')
            exit()
        else:
            print('Cliente não encontrado!')
            continue

#motoristas
        
