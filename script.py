informacoes = []

while True:
    print("""=================================
       LOJA DE CARTAS POKÉMON
=================================

1 - Cadastrar carta
2 - Listar estoque
3 - Consultar carta
4 - Registrar entrada
5 - Registrar saída
6 - Listar cartas sem estoque
0 - Sair""")
    
    opcao = int(input('\nEscolha uma opção: '))

    if opcao == 0:
        break

    elif opcao == 1:
        id = input('Digite o identificador da carta: ')
        titulo = input('Digite o título da carta: ')
        quantidade_estoque = int(input('Digite a quantidade em estoque: '))
        
        informacoes.append([id, titulo, quantidade_estoque])

        print('Carta cadastrada com sucesso!')
    elif opcao == 2:
        print('\n========== ESTOQUE ==========\n')
        for carta in informacoes:
            print(f'ID: {carta[0]}')
            print(f'Carta: {carta[1]}')
            print(f'Quantidade: {carta[2]}\n')

    elif opcao == 3:
        id = input('Digite o identificador da carta: ')

        for carta in informacoes:
            if carta[0] == id:
                print('\n========== CARTA ==========\n')
                print(f'ID: {carta[0]}')
                print(f'Carta: {carta[1]}')
                print(f'Quantidade: {carta[2]}\n')
    
    elif opcao == 4:
        id = input('Digite o identificador da carta: ')
        quantidade_recebida = int(input('Digite a quantidade recebida: '))

        for carta in informacoes:
            if carta[0] == id:
                carta[2] += quantidade_recebida
        
        print('Entrada registrada com sucesso!')

    elif opcao == 5:
        id = input('Digite o identificador da carta: ')
        quantidade_retirada = int(input('Digite a quantidade retirada: '))

        for carta in informacoes:
            if carta[0] == id:
                carta[2] -= quantidade_retirada
        
        print('Saída registrada com sucesso!\n')
    
    elif opcao == 6:
        print('\n====== CARTAS SEM ESTOQUE ======\n')

        for carta in informacoes:
            if carta[2] == 0:
                print(f'ID: {carta[0]}')
                print(f'Carta: {carta[1]}')
                print(f'Quantidade: {carta[2]}\n')