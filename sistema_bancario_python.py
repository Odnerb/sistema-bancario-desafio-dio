deposito = 0
saque = 0
saldo = 0
total_operacoes = 0
total_saque = 0
LIMITE_SAQUE_DIARIO = 0
extrato = "Não foram realizadas movimentações"

def menu():
    print(f"""------- BANCO BRAZUCA ------- 
-----------------------------
Seleciona a operação desejada:
[1] - Depósito
[2] - Saque
[3] - Visualizar extrato
[0] - Sair

""")
    
while True:
    menu()
    operacao = int(input('Operação: '))

    if operacao == 1 and deposito >= 0:
        deposito = float(input('Valor do depósito:\nR$ '))
        saldo += deposito
        total_operacoes += 1
        if deposito < 0:
            saldo, deposito,total_operacoes = 0, 0, 0
            print(f'Valor inválido! Insira valores acima de R$0,00\n')

    elif operacao == 2:
        saque = float(input('Valor de saque:\nR$ '))
        print()
        if saque >= 1 and saque < 501 and saldo >= saque and LIMITE_SAQUE_DIARIO >= 0 and LIMITE_SAQUE_DIARIO < 3:
            total_saque += saque
            saldo -= saque
            LIMITE_SAQUE_DIARIO += 1
            total_operacoes += 1
        
        elif saldo < saque:
            print(f'Valor de saque maior que o saldo atual de R${saldo}\n')

        elif LIMITE_SAQUE_DIARIO > 3:
            print(f'Limite de saque atingido\n')

        else:
            print('Limite de saque de até R$500,00\n')

    elif operacao == 3:
        if total_operacoes > 0:
            extrato = f'-------"BANCO BRAZUCA"-------\nSaldo atual: R$ {saldo}\n\nDepósito de: R$ {deposito}\nValor de saque: R$ {total_saque}\nOperações realizadas: {total_operacoes}x\n'+'-'*28
            print(extrato)
            break

        else:
            print(extrato)
            break

    else:
        print('O Banco Brazuca, Agradece sua visita!')
        break

