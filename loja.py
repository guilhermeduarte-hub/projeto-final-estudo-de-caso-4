"""
Estudo de Caso 6 - Loja de Cartas Pokémon

Componentes:
   - Alice Esther
   - Guilherme Duarte
   - Luiz Guilherme
"""

informacoes = []

while True:
    print('\n=================================')
    print('      LOJA DE CARTAS POKÉMON')
    print('=================================\n')
    print('1 - Cadastros')
    print('2 - Consultas')
    print('3 - Estoque')
    print('0 - Sair')

    opcao = int(input('\nEscolha uma opção: '))

    if opcao == 0:
        break

    elif opcao == 1:
        while True: 
            print('\n========== CADASTROS ==========')
            print('1 - Cadastrar carta')
            print('0 - Voltar')

            opcao_sub = int(input('\nEscolha uma opção: '))

            if opcao_sub == 0:
                break
            elif opcao_sub == 1:
                id_carta = input('\nDigite o identificador da carta: ')

                existe = False
                for carta in informacoes:
                    if carta['id'] == id_carta:
                        existe = True
                        break

                if existe:
                    print('\nErro: Este identificador já está cadastrado!')
                else:
                    titulo = input('Digite o título da carta: ')
                    quantidade_estoque = int(input('Digite a quantidade em estoque: '))

                    if quantidade_estoque < 0:
                        print('\nErro: A quantidade em estoque não pode ser negativa!')
                    else:
                        informacoes.append({
                            'id': id_carta,
                            'titulo': titulo, 
                            'estoque': quantidade_estoque
                        })
                        print('\nCarta cadastrada com sucesso!')

    elif opcao == 2:
        while True:
            print('\n========== CONSULTAS ==========')
            print('1 - Listar cartas')
            print('2 - Consultar carta')
            print('3 - Listar cartas sem estoque')
            print('0 - Voltar')

            opcao_sub = int(input('\nEscolha uma opção: '))

            if opcao_sub == 0:
                break
            elif opcao_sub == 1:
                print('\n========== ESTOQUE ==========')
                if len(informacoes) == 0:
                    print('\nNão há cartas cadastradas no estoque.')
                else:
                    for carta in informacoes:
                        print(f"\nID: {carta['id']}")
                        print(f"Carta: {carta['titulo']}")
                        print(f"Quantidade: {carta['estoque']}")
            elif opcao_sub == 2:
                id_carta = input('\nDigite o identificador da carta: ')
                encontrada = False

                for carta in informacoes:
                    if carta['id'] == id_carta:
                        print('\n========== CARTA ==========')
                        print(f"\nID: {carta['id']}")
                        print(f"Título: {carta['titulo']}")
                        print(f"Quantidade em estoque: {carta['estoque']}")
                        encontrada = True
                        break
                if not encontrada:
                    print('\nCarta não encontrada.')
            elif opcao_sub == 3:
                print('\n====== CARTAS SEM ESTOQUE ======')
                if len(informacoes) == 0:
                    print('\nNão há cartas cadastradas.')
                else:
                    contador_zeradas = 0
                    for carta in informacoes:
                        if carta['estoque'] == 0:
                            print(f"\nID: {carta['id']}")
                            print(f"Título: {carta['titulo']}")
                            print(f"Quantidade: {carta['estoque']}\n")
                            contador_zeradas += 1

                    if contador_zeradas == 0:
                        print('\nNenhuma carta sem estoque encontrada.')

    elif opcao == 3:
        while True:
            print('\n========== ESTOQUE ==========')
            print('1 - Registrar entrada')
            print('2 - Registrar saída')
            print('0 - Voltar')

            opcao_sub = int(input('\nEscolha uma opção: '))

            if opcao_sub == 0:
                break
            elif opcao_sub == 1:
                id_carta = input('\nDigite o identificador da carta: ')
                encontrada = False

                for carta in informacoes:
                    if carta['id'] == id_carta:
                        encontrada = True
                        quantidade_recebida = int(input('Digite a quantidade recebida: '))

                        if quantidade_recebida <= 0:
                            print('\nErro: A quantidade recebida deve ser maior que zero.')
                        else:
                            carta['estoque'] += quantidade_recebida
                            print('\nEntrada registrada com sucesso!')
                            print('\nO estoque agora será:')
                            print(f"\nID: {carta['id']}")
                            print(f"Carta: {carta['titulo']}")
                            print(f"Quantidade: {carta['estoque']}\n")
                        break

                if not encontrada:
                    print('\nCarta não encontrada.')
            elif opcao_sub == 2:
                id_carta = input('\nDigite o identificador da carta: ')
                encontrada = False

                for carta in informacoes:
                    if carta['id'] == id_carta:
                        encontrada = True
                        quantidade_retirada = int(input('Digite a quantidade retirada: '))

                        if quantidade_retirada <= 0:
                            print('\nErro: A quantidade retirada deve ser maior que zero.')
                        elif quantidade_retirada > carta['estoque']:
                            print('\nErro: Quantidade indisponível em estoque.')
                        else:
                            carta['estoque'] -= quantidade_retirada
                            print('\nSaída registrada com sucesso!')
                            print('\nO estoque passa a ser:')
                            print(f"\nID: {carta['id']}")
                            print(f"Carta: {carta['titulo']}")
                            print(f"Quantidade: {carta['estoque']}\n")
                        break

                if not encontrada:
                    print('\nCarta não encontrada.')

    else:
        print('\nOpção inválida! Tente novamente.')
