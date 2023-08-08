saldo = 0
numero_saque = 0
extrato = []

menu = \
'''
----------Sistema Bancário----------
Selecione a opção desejada:
(1) - Depósito
(2) - Saque
(3) - Extrato
(4) - Finalizar
------------------------------------
'''
while True:
    entrada = int(input(menu))

    if entrada == 1:
        valor_deposito = float(input('Digite o valor desejado: '))
        if valor_deposito < 0:
            print('Operação inválida!')
        else:
            saldo += valor_deposito
            extrato.append(f'Depósito: R$ {valor_deposito:.2f}')

    if entrada == 2:
        valor_saque = float(input('Digite o valor desejado: '))
        if valor_saque < 0  or valor_saque > 500 or valor_saque > saldo or numero_saque >= 3:
            print('Operação inválida!')
        else:
            saldo -= valor_saque
            numero_saque += 1
            extrato.append(f'Saque: R$ {valor_saque:.2f}')
    
    if entrada == 3:
        print('---------------Extrato--------------')
        for i in range(0, len(extrato)):
            print(extrato[i])
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('------------------------------------')
    
    if entrada == 4:
        break