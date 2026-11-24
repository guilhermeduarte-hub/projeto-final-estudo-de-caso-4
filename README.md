# Sistema de Estoque - Loja de Cartas Pokémon

Este projeto implementa um sistema simples de gerenciamento de estoque para uma loja de cartas Pokémon, desenvolvido em Python.

---

## Funcionalidades

- Cadastro de cartas (título e quantidade em estoque) com geração automática de ID
- Listagem de todas as cartas cadastradas em formato de tabela
- Consulta de carta por ID
- Listagem de cartas sem estoque
- Busca de cartas por título (ou parte dele)
- Registro e exibição do histórico de erros
- Registro de entrada no estoque
- Registro de saída no estoque
- Menu interativo no terminal organizado em submenus (Cadastros, Consultas e Estoque)

---

## Validações

- Impede o cadastro de cartas com título vazio
- Impede o cadastro com estoque negativo
- Impede a busca por título vazio
- Impede entrada ou saída com quantidade menor ou igual a zero
- Impede saída de estoque maior que a quantidade disponível
- Verifica se o ID da carta existe antes de movimentar o estoque
- Valida entradas numéricas no menu
- Registra automaticamente os erros de validação e operação para consulta posterior

---

## Estrutura de dados

Cada carta é armazenada como um dicionário com os seguintes campos:

```python
{
    "id": 1,
    "titulo": "Pikachu",
    "estoque": 5
}
