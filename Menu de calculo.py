n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
escolha = 0
while escolha != 5:
    escolha = int(input('''===================\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS
[5] SAIR\n>>Qual é a sua opção? '''))
    if escolha == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    if escolha == 2:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, multiplicacao))
    if escolha == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        else:
            print('O maior número é {}.'.format(n1))
    if escolha == 4:
        print('==Insira novos números==')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
print('FIM')