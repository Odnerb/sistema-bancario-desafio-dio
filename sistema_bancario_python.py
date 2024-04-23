# Como funções não guardam valor, utilizei variáveis globais para poder guardar
# os valores de cada respectivo cliente em determinada conta bancária
usuarios, dados_bancarios, conta, saldo_conta, saque, saques, op_saldo, total_saque, LIMITE_SAQUE, AGENCIA, historico = [], [], 0, 0, 0, 0, 0, 0, 0, '0001', "Não foram realizadas movimentações"


def menu():
    print(f"""\n-----------------------------
------- BANCO BRAZUCA ------- 
-----------------------------
Seleciona a operação desejada:

[1] - Cadastrar usuário
[2] - Abrir conta corrente
[3] - Depósito
[4] - Saque
[5] - Visualizar extrato
[6] - Listar contas
[0] - Sair

""")


# Caso o usuário escolha a opção 1 - O programa irá pedir para o cliente fornecer seus dados
def cadastro_usuario(nome, data_nascimento, cpf, endereco):
    global usuarios
    usuarios.append([{
        'Nome': nome,
        'Data Nascimento': data_nascimento,
        'Cpf': cpf,
        'Endereço': endereco,
    }])
    print('----------------Usuário Cadastrado com Sucesso----------------\n')


# A função cria uma conta bancária para o cliente, onde o número da agência é fixo
# sendo argumento nomeado e recebe o valor de '0001', os dados de conta corrente
# serão adicionados, sempre +1 ao valor de conta a cada abertura.
def criar_conta_corrente(usuario):
    global dados_bancarios, conta, AGENCIA
    conta += 1
    dados_bancarios.append([{
        'Agencia': AGENCIA,
        'Conta corrente': conta,
        'Usuário': usuario
    }])
    print('----------------Usuário Cadastrado com Sucesso----------------\n')

# A função depositar recebe parâmetros de saldo e o valor a ser depositado, em
# seguida o sistema fornece o extrato mostrando quanto foi depositado na conta.
def depositar(saldo, valor, extrato, /):
    # Para atualizar os valores das funções, estou atualizando os dados das variáveis globais, já que funções não irão armazenar os valores no seu final
    global saldo_conta
    saldo += valor
    # Atualizando o saldo_conta da variável global
    saldo_conta += saldo
    if valor < 0:
        # Caso o usuário digite números negativos, o programa irá informar a mensagem padrão contida em extrato
        saldo, valor = 0, 0
        return extrato, valor
    elif valor > 0:
        extrato = f'-------------------------\nUltimo depósito: R$ {valor}\nSaldo da conta: R$ {saldo_conta}'
        return extrato

# Sacar recebe argumentos posicionais "saldo_atual" e "valor_saque", argumentos nomeados "extrato" e "numeros_saques"
# valor_saque irá pegar o valor que o cliente deseja retirar do banco, sendo assim atualizando globalmente a variável saldo_conta
# de onde será descontado o valor.
def sacar(saldo_atual, valor_saque, /, *, extrato, numero_saques):
    global LIMITE_SAQUE, saldo_conta, historico, total_saque, usuarios
    
    if valor_saque >= 1 and valor_saque < 501 and saldo_atual >= valor_saque and LIMITE_SAQUE >= 0 and LIMITE_SAQUE < 3:
        numero_saques += 1
        saldo_atual -= valor_saque
        total_saque += valor_saque
        saldo_conta = saldo_atual
        extrato = f'-------------------------\nValor sacado: R$ {valor_saque}\nSaldo da conta: R$ {saldo_atual}'
        LIMITE_SAQUE += numero_saques
        historico = extrato
        return extrato
        
    elif saldo_atual < valor_saque:
        print(f'Inserir valor menor ou igual a R$ {saldo_atual}')

    elif valor_saque > 500:
        print(f'Limite de saque de até R$ 500,00\n')
    
    elif LIMITE_SAQUE >= 3:
        print(f'\nLimite de saque atingido')
        extrato = f'-------"BANCO BRAZUCA"-------\nSaldo atual: R$ {saldo_conta}\nValor de saque: R$ {total_saque}\n'+'-'*28
        historico = extrato
        return extrato


# Histórico irá fornecer os dados de saldo atual da conta
def visualizar_historico(saldo, comprovante):
    print(comprovante)
    print(f'\nSaldo atual: R${saldo}')


# Função mostra o quantitativo de contas criadas por determinado usuário.
def contas_criadas(dados):
    for chave, dado in enumerate(dados):
        for conta in dado:
            print('------------Contas-----------')
            print(f'Agencia: ', conta['Agencia'])
            print(f'C/c: ', conta['Conta corrente'])
            print(f'Usuário: ', conta['Usuário'])
    

# Enquanto o usuário estiver realizando as operações no sistema, o programa fica em execução
# até que o cliente deseja encerrar suas consultas.
while True:
    menu()
    operacao = int(input('Operação: '))

    if operacao == 1:
        # Na operação 1 - Resolvi deixar inicialmente, para evitar que os usuários realizem a tentativa de criar usuários diferentes com o mesmo CPF
        saldo_conta, dados_bancarios = 0, []

        nome_usuario = input('Nome completo: ')
        nascimento = input('Data nascimento - (Ex: 15/05/1999): ')
        cpf_usuario = int(input('Cpf: '))
        # Valida se o CPF recebido pelo sistema é único.
        for chave, valor in enumerate(usuarios):
            for itens in valor:
                if cpf_usuario == itens['Cpf']:
                    print('\nCpf inválido!\nPor favor insira o cpf correto...')
                    cpf_usuario = int(input('Cpf: '))

        endereco_usuario = input('Endereço - (Ex: Rua Petrolina, Bairro Dom Quixote, 3500 - Porto Velho/RO): ')
        cadastro_usuario(**{'nome':nome_usuario, 'data_nascimento':nascimento, 'cpf':cpf_usuario, 'endereco':endereco_usuario})
        
    elif operacao == 2:
        criar_conta_corrente(cpf_usuario)
        
    elif operacao == 3:
        deposito = float(input('Valor do depósito:\nR$ '))
        print(depositar(op_saldo, deposito, historico))
        
    elif operacao == 4:
        saque = float(input('Valor de saque:\nR$ '))
        op_saldo = saldo_conta
        print(sacar(op_saldo, saque, extrato=historico, numero_saques=saques))
        
    elif operacao == 5:
        visualizar_historico(saldo_conta, comprovante=historico)
    
    elif operacao == 6:
        contas_criadas(dados_bancarios)

    else:
        print('O Banco Brazuca, Agradece sua visita!')
        break

for chave, usuario in enumerate(usuarios):
    print(usuario)
