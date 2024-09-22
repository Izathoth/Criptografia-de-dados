# Criptografia de Dados com Python

## Descrição

Este projeto é uma aplicação de criptografia de dados desenvolvida em Python, utilizando a biblioteca `Tkinter` para a interface gráfica e `cryptography` para os algoritmos de criptografia. O objetivo principal é fornecer uma maneira fácil e segura de criptografar e descriptografar mensagens e arquivos, além de registrar operações realizadas pelo usuário.

## Funcionalidades

- **Criptografia e Descriptografias de Mensagens**: Insira uma mensagem e utilize a aplicação para criptografá-la ou descriptografá-la facilmente.
- **Criptografia e Descriptografias de Arquivos**: Selecione arquivos do seu sistema e criptografe-os ou descriptografe-os, armazenando os resultados em pastas dedicadas.
- **Registro de Operações**: Todas as operações realizadas (criptografias e descriptografias) são registradas em um arquivo de log para consulta futura.
- **Interface Gráfica Intuitiva**: A aplicação apresenta uma interface limpa e organizada, facilitando a interação do usuário.

## Estrutura do Projeto

- `secret.key`: Arquivo gerado que contém a chave de criptografia.
- `Arquivos_Criptografados/`: Pasta onde os arquivos criptografados são armazenados.
- `Arquivos_Descriptografados/`: Pasta onde os arquivos descriptografados são armazenados.
- `Registro/operacoes.log`: Arquivo que registra todas as operações realizadas na aplicação.

## Dependências

- Python 3.x
- `cryptography`
- `tkinter`

## Como Usar

1. Clone o repositório para o seu sistema.
2. Instale as dependências necessárias com `pip install cryptography`.
3. Execute o script principal.
4. Utilize a interface gráfica para criptografar ou descriptografar mensagens e arquivos.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
