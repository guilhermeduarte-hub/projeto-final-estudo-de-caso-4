"""
Estudo de Caso 6 - Loja de Cartas Pokémon

Componentes:
   - Alice Esther
   - Guilherme Duarte
   - Luiz Guilherme
"""

informacoes = []

while True:
    print("""=================================
       LOJA DE CARTAS POKÉMON
=================================

1 - Cadastros
2 - Consultas
3 - Estoque
0 - Sair""")

    opcao = int(input('\nEscolha uma opção: '))

    if opcao == 0:
        break


    elif opcao == 1:
        while True: 
            print("""\n========== CADASTROS ==========

1 - Cadastrar carta
0 - Voltar""")
            
            opcao = int(input('\nEscolha uma opção: '))

            if opcao == 0:
                break
            elif opcao == 1:
                id = input('Digite o identificador da carta: ')
            
                existe = False
                for carta in informacoes:
                    if carta['id'] == id:
                        existe = True
                        break
                        
                if existe:
                    print('Erro: Este identificador já está cadastrado!\n')
                else:
                    titulo = input('Digite o título da carta: ')
                    quantidade_estoque = int(input('Digite a quantidade em estoque: '))
                    
                    if quantidade_estoque < 0:
                        print('Erro: A quantidade em estoque não pode ser negativa!\n')
                    else:
                        informacoes.append({
                            'id': id,
                            'titulo': titulo, 
                            'estoque': quantidade_estoque
                        })
                        print('Carta cadastrada com sucesso!\n')


    elif opcao == 2:
        while True:
            print("""\n========== CONSULTAS ==========

1 - Listar cartas
2 - Consultar carta
3 - Listar cartas sem estoque
0 - Voltar""")
            
            opcao = int(input('\nEscolha uma opção: '))

            if opcao == 0:
                break
            elif opcao == 1:
                print('\n========== ESTOQUE ==========\n')
                if len(informacoes) == 0:
                    print('Não há cartas cadastradas no estoque.\n')
                else:
                    for carta in informacoes:
                        print(f'ID: {carta['id']}')
                        print(f'Carta: {carta['titulo']}')
                        print(f'Quantidade: {carta['estoque']}\n')
            elif opcao == 2:
                id = input('Digite o identificador da carta: ')
                encontrada = False

                for carta in informacoes:
                    if carta['id'] == id:
                        print('\n========== CARTA ==========\n')
                        print(f'ID: {carta['id']}')
                        print(f'Título: {carta['titulo']}')
                        print(f'Quantidade em estoque: {carta['estoque']}\n')
                        encontrada = True
                        break
                    if not encontrada:
                        print('Carta não encontrada.\n')
            elif opcao == 3:
                print('\n====== CARTAS SEM ESTOQUE ======\n')
                if len(informacoes) == 0:
                    print('Não há cartas cadastradas.\n')
                else:
                    contador_zeradas = 0
                    for carta in informacoes:
                        if carta['estoque'] == 0:
                            print(f'ID: {carta['id']}')
                            print(f'Título: {carta['titulo']}')
                            print(f'Quantidade: {carta['estoque']}\n')
                            contador_zeradas += 1
                    
                    if contador_zeradas == 0:
                        print('Nenhuma carta sem estoque encontrada.\n')


    elif opcao == 3:
        while True:
            print("""\n========== ESTOQUE ==========

1 - Registrar entrada
2 - Registrar saída
0 - Voltar""")
        
            opcao = int(input('\nEscolha uma opção: '))

            if opcao == 0:
                break
            elif opcao == 1:
                id = input('Digite o identificador da carta: ')
                encontrada = False

                for carta in informacoes:
                    if carta['id'] == id:
                        encontrada = True
                        quantidade_recebida = int(input('Digite a quantidade recebida: '))
                        
                        if quantidade_recebida <= 0:
                            print('\nErro: A quantidade recebida deve ser maior que zero.\n')
                        else:
                            carta['estoque'] += quantidade_recebida
                            print('\nEntrada registrada com sucesso!')
                            print('O estoque agora será:\n')
                            print(f'ID: {carta['id']}')
                            print(f'Carta: {carta['titulo']}')
                            print(f'Quantidade: {carta['estoque']}\n')
                        break
                        
                if not encontrada:
                    print('Carta não encontrada.\n')
            elif opcao == 2:
                id = input('Digite o identificador da carta: ')
                encontrada = False

                for carta in informacoes:
                    if carta['id'] == id:
                        encontrada = True
                        quantidade_retirada = int(input('Digite a quantidade retirada: '))
                        
                        if quantidade_retirada <= 0:
                            print('\nErro: A quantidade retirada deve ser maior que zero.\n')
                        elif quantidade_retirada > carta['estoque']:
                            print('\nErro: Quantidade indisponível em estoque.\n')
                        else:
                            carta['estoque'] -= quantidade_retirada
                            print('\nSaída registrada com sucesso!')
                            print('O estoque passa a ser:\n')
                            print(f'ID: {carta['id']}')
                            print(f'Carta: {carta['titulo']}')
                            print(f'Quantidade: {carta['estoque']}\n')
                        break
                        
                if not encontrada:
                    print('Carta não encontrada.\n')

    else:
        print('\nOpção inválida! Tente novamente.\n')
