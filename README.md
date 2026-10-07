# Loja de Cartas Pokémon - Gestão de Estoque (Versão 2.0)

## Integrantes da Equipe
- Alice Esther
- Guilherme Duarte
- Luiz Guilherme

## Estudo de Caso
Estudo de Caso 6 — Loja de Cartas Pokémon

## Descrição Resumida
Sistema interativo desenvolvido em Python para execução em terminal, destinado ao gerenciamento de estoque de uma loja de cartas Pokémon. O sistema utiliza uma estrutura de dados baseada em **lista de dicionários** e organiza suas funcionalidades por meio de **submenus temáticos**.

## Estrutura do Menu e Funcionalidades

### Menu Principal
- **1 - Cadastros**
  - **1.1 - Cadastrar carta:** Permite cadastrar uma nova carta registrando seu identificador (ID), título e quantidade inicial em estoque, contando com validação de ID único e bloqueio de quantidades negativas.
- **2 - Consultas**
  - **2.1 - Listar cartas:** Exibe todas as cartas atualmente cadastradas no sistema.
  - **2.2 - Consultar carta:** Localiza e exibe os detalhes de uma carta específica através do seu ID.
  - **2.3 - Listar cartas sem estoque:** Exibe um relatório filtrado contendo apenas as cartas que possuem quantidade em estoque igual a 0.
- **3 - Estoque**
  - **3.1 - Registrar entrada:** Adiciona novas unidades ao estoque de uma carta já existente (valida entradas maiores que zero).
  - **3.2 - Registrar saída:** Dá baixa em unidades do estoque de uma carta (valida saldo disponível para evitar estoque negativo).
- **0 - Sair:** Encerra a execução do sistema.

## Estrutura de Dados Utilizada
Os dados são armazenados em uma lista principal chamada `informacoes`, na qual cada item é um dicionário com a seguinte estrutura:

```python
{
    'id': 'PK001',
    'titulo': 'Pikachu',
    'estoque': 10
}
