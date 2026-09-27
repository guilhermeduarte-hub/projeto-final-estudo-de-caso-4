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

    opcao = input('\nEscolha uma opção: ')

    if opcao == '0':
        break

    elif opcao == '1':
        id = input('Digite o identificador da carta: ')
        
        existe = False
        for carta in informacoes:
            if carta[0] == id:
                existe = True
                break
                
        if existe:
            print('Erro: Este identificador já está cadastrado!')
        else:
            titulo = input('Digite o título da carta: ')
            quantidade_estoque = int(input('Digite a quantidade em estoque: '))
            
            if quantidade_estoque < 0:
                print('Erro: A quantidade em estoque não pode ser negativa!')
            else:
                informacoes.append([id, titulo, quantidade_estoque])
                print('Carta cadastrada com sucesso!')

    elif opcao == '2':
        print('\n========== ESTOQUE ==========\n')
        if len(informacoes) == 0:
            print('Não há cartas cadastradas no estoque.\n')
        else:
            for carta in informacoes:
                print(f'ID: {carta[0]}')
                print(f'Carta: {carta[1]}')
                print(f'Quantidade: {carta[2]}\n')

    elif opcao == '3':
        id = input('Digite o identificador da carta: ')
        encontrada = False

        for carta in informacoes:
            if carta[0] == id:
                print('\n========== CARTA ==========\n')
                print(f'ID: {carta[0]}')
                print(f'Título: {carta[1]}')
                print(f'Quantidade em estoque: {carta[2]}\n')
                encontrada = True
                break
                
        if not encontrada:
            print('Carta não encontrada.\n')

    elif opcao == '4':
        id = input('Digite o identificador da carta: ')
        encontrada = False

        for carta in informacoes:
            if carta[0] == id:
                encontrada = True
                quantidade_recebida = int(input('Digite a quantidade recebida: '))
                
                if quantidade_recebida <= 0:
                    print('\nErro: A quantidade recebida deve ser maior que zero.\n')
                else:
                    carta[2] += quantidade_recebida
                    print('\nEntrada registrada com sucesso!')
                    print('O estoque agora será:\n')
                    print(f'ID: {carta[0]}')
                    print(f'Carta: {carta[1]}')
                    print(f'Quantidade: {carta[2]}\n')
                break
                
        if not encontrada:
            print('Carta não encontrada.\n')

    elif opcao == '5':
        id = input('Digite o identificador da carta: ')
        encontrada = False

        for carta in informacoes:
            if carta[0] == id:
                encontrada = True
                quantidade_retirada = int(input('Digite a quantidade retirada: '))
                
                if quantidade_retirada <= 0:
                    print('\nErro: A quantidade retirada deve ser maior que zero.\n')
                elif quantidade_retirada > carta[2]:
                    print('\nErro: Quantidade indisponível em estoque.\n')
                else:
                    carta[2] -= quantidade_retirada
                    print('\nSaída registrada com sucesso!')
                    print('O estoque passa a ser:\n')
                    print(f'ID: {carta[0]}')
                    print(f'Carta: {carta[1]}')
                    print(f'Quantidade: {carta[2]}\n')
                break
                
        if not encontrada:
            print('Carta não encontrada.\n')

    elif opcao == '6':
        print('\n====== CARTAS SEM ESTOQUE ======\n')
        if len(informacoes) == 0:
            print('Não há cartas cadastradas.\n')
        else:
            contador_zeradas = 0
            for carta in informacoes:
                if carta[2] == 0:
                    print(f'ID: {carta[0]}')
                    print(f'Título: {carta[1]}')
                    print(f'Quantidade: {carta[2]}\n')
                    contador_zeradas += 1
            
            if contador_zeradas == 0:
                print('Nenhuma carta sem estoque encontrada.\n')

    else:
        print('\nOpção inválida! Tente novamente.\n')

    input('Pressione ENTER para continuar...')