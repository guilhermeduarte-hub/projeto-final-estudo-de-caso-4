# ============================================================
# DADOS E CONTADORES
# ============================================================

informacoes = []
proximo_id_carta = 1
erros = []


# ============================================================
# GERENCIAMENTO DE CARTAS
# ============================================================

def adicionar_carta(titulo, estoque):
    global proximo_id_carta

    erros_locais = []

    if not titulo.strip():
        erros_locais.append("Erro: O título da carta não pode ser vazio!")

    if estoque < 0:
        erros_locais.append("Erro: A quantidade em estoque não pode ser negativa!")

    if erros_locais:
        for erro in erros_locais:
            registrar_erro(erro)
        return None, "\n".join(erros_locais)

    carta = {
        "id": proximo_id_carta,
        "titulo": titulo.strip(),
        "estoque": estoque
    }

    informacoes.append(carta)
    proximo_id_carta += 1

    return carta, "Carta cadastrada com sucesso!"


def listar_cartas():
    return informacoes


def consultar_carta(id_carta):
    for carta in informacoes:
        if carta["id"] == id_carta:
            return carta

    return None


def buscar_cartas_por_titulo(titulo):
    resultado = []
    titulo = titulo.strip().lower()

    if not titulo:
        return resultado

    for carta in informacoes:
        if titulo in carta["titulo"].lower():
            resultado.append(carta)

    return resultado


def obter_cartas_sem_estoque():
    resultado = []

    for carta in informacoes:
        if carta["estoque"] == 0:
            resultado.append(carta)

    return resultado


def adicionar_estoque(id_carta, quantidade):
    carta = consultar_carta(id_carta)

    if carta is None:
        registrar_erro(f"Erro: Carta com ID {id_carta} não encontrada!")
        return False, "Erro: Carta não encontrada!"

    if quantidade <= 0:
        registrar_erro("Erro: A quantidade deve ser maior que zero!")
        return False, "Erro: A quantidade deve ser maior que zero!"

    carta["estoque"] += quantidade

    return True, "Estoque atualizado com sucesso!"


def remover_estoque(id_carta, quantidade):
    carta = consultar_carta(id_carta)

    if carta is None:
        registrar_erro(f"Erro: Carta com ID {id_carta} não encontrada!")
        return False, "Erro: Carta não encontrada!"

    if quantidade <= 0:
        registrar_erro("Erro: A quantidade deve ser maior que zero!")
        return False, "Erro: A quantidade deve ser maior que zero!"

    if quantidade > carta["estoque"]:
        registrar_erro(f"Erro: Quantidade indisponível! Estoque atual: {carta['estoque']}")
        return False, f"Erro: Quantidade indisponível! Estoque atual: {carta['estoque']}"

    carta["estoque"] -= quantidade

    return True, "Saída de estoque registrada com sucesso!"


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            registrar_erro("Erro: Entrada inválida! Digite apenas números inteiros.")
            print("\nErro: Digite apenas números inteiros!")


def exibir_resultado(sucesso, mensagem):
    if sucesso:
        print(f"\n{mensagem}")
    else:
        print(f"\n{mensagem}")


def imprimir_tabela(lista_cartas):
    if not lista_cartas:
        print("\nNenhuma carta encontrada.")
        return

    largura_id = max(
        max(len(str(carta["id"])) for carta in lista_cartas),
        len("ID")
    )

    largura_titulo = max(
        max(len(carta["titulo"]) for carta in lista_cartas),
        len("TÍTULO")
    )

    largura_estoque = max(
        max(len(str(carta["estoque"])) for carta in lista_cartas),
        len("ESTOQUE")
    )

    print(
        f"\n{'ID':<{largura_id}}   "
        f"{'TÍTULO':<{largura_titulo}}   "
        f"{'ESTOQUE':<{largura_estoque}}"
    )

    print("-" * (largura_id + largura_titulo + largura_estoque + 6))

    for carta in lista_cartas:
        print(
            f"{carta['id']:<{largura_id}}   "
            f"{carta['titulo']:<{largura_titulo}}   "
            f"{carta['estoque']:<{largura_estoque}}"
        )


def exibir_carta(carta):
    print("\n========== CARTA ==========")
    print(f"ID: {carta['id']}")
    print(f"Título: {carta['titulo']}")
    print(f"Quantidade em estoque: {carta['estoque']}")


def registrar_erro(mensagem):
    erros.append(mensagem)


def exibir_erros():
    if not erros:
        print("\nNenhum erro registrado.")
    else:
        print("\n========== ERROS REGISTRADOS ==========")
        for i, erro in enumerate(erros, start=1):
            print(f"{i}. {erro}")


# ============================================================
# MENU DE CADASTROS
# ============================================================

def menu_cadastros():
    while True:
        print("\n========== CADASTROS ==========")
        print("1 - Cadastrar carta")
        print("0 - Voltar")

        opcao = ler_inteiro("\nEscolha uma opção: ")

        if opcao == 0:
            break

        elif opcao == 1:
            titulo = input("\nDigite o título da carta: ").strip()
            quantidade = ler_inteiro("Digite a quantidade em estoque: ")

            carta, mensagem = adicionar_carta(titulo, quantidade)

            if carta is not None:
                print(f"\n{mensagem}")
                print(f"ID gerado automaticamente: {carta['id']}")
            else:
                print(f"\n{mensagem}")

        else:
            print("\nOpção inválida! Tente novamente.")


# ============================================================
# MENU DE CONSULTAS
# ============================================================

def menu_consultas():
    while True:
        print("\n========== CONSULTAS ==========")
        print("1 - Listar cartas")
        print("2 - Consultar carta por ID")
        print("3 - Listar cartas sem estoque")
        print("4 - Buscar carta por título")
        print("5 - Exibir erros registrados")
        print("0 - Voltar")

        opcao = ler_inteiro("\nEscolha uma opção: ")

        if opcao == 0:
            break

        elif opcao == 1:
            lista = listar_cartas()
            imprimir_tabela(lista)

        elif opcao == 2:
            id_carta = ler_inteiro("\nDigite o ID da carta: ")

            carta = consultar_carta(id_carta)

            if carta is None:
                print("\nCarta não encontrada.")
            else:
                exibir_carta(carta)

        elif opcao == 3:
            lista = obter_cartas_sem_estoque()

            print("\n====== CARTAS SEM ESTOQUE ======")
            imprimir_tabela(lista)

        elif opcao == 4:
            titulo = input("\nDigite o título ou parte dele: ").strip()

            if not titulo:
                print("\nErro: O título da pesquisa não pode ser vazio!")
            else:
                lista = buscar_cartas_por_titulo(titulo)
                imprimir_tabela(lista)

        elif opcao == 5:
            exibir_erros()

        else:
            print("\nOpção inválida! Tente novamente.")


# ============================================================
# MENU DE ESTOQUE
# ============================================================

def menu_estoque():
    while True:
        print("\n========== ESTOQUE ==========")
        print("1 - Registrar entrada")
        print("2 - Registrar saída")
        print("0 - Voltar")

        opcao = ler_inteiro("\nEscolha uma opção: ")

        if opcao == 0:
            break

        elif opcao == 1:
            id_carta = ler_inteiro("\nDigite o ID da carta: ")
            quantidade = ler_inteiro("Digite a quantidade recebida: ")

            sucesso, mensagem = adicionar_estoque(id_carta, quantidade)
            exibir_resultado(sucesso, mensagem)

        elif opcao == 2:
            id_carta = ler_inteiro("\nDigite o ID da carta: ")
            quantidade = ler_inteiro("Digite a quantidade retirada: ")

            sucesso, mensagem = remover_estoque(id_carta, quantidade)
            exibir_resultado(sucesso, mensagem)

        else:
            print("\nOpção inválida! Tente novamente.")


# ============================================================
# MENU PRINCIPAL
# ============================================================

def menu_principal():
    while True:
        print("\n=================================")
        print("       LOJA DE CARTAS POKÉMON")
        print("=================================")
        print("1 - Cadastros")
        print("2 - Consultas")
        print("3 - Estoque")
        print("0 - Sair")

        opcao = ler_inteiro("\nEscolha uma opção: ")

        if opcao == 0:
            print("\nSaindo do sistema... Até logo!")
            break

        elif opcao == 1:
            menu_cadastros()

        elif opcao == 2:
            menu_consultas()

        elif opcao == 3:
            menu_estoque()

        else:
            print("\nOpção inválida! Tente novamente.")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

menu_principal()
