# 🧮 Calculadora Científica em Python — Desafio 02

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)
![Alura](https://img.shields.io/badge/Imers%C3%A3o-Alura-blue)

## 📌 Sobre o projeto

Este projeto foi desenvolvido durante a **Imersão Engenharia de Software: Dev na Era da IA**, da Alura em parceria com o Google.

O segundo desafio consiste na evolução de uma calculadora desenvolvida em Python, ampliando suas funcionalidades para realizar operações matemáticas mais avançadas, gerar representações gráficas de funções e manter um histórico dos cálculos realizados.

O objetivo é aplicar conhecimentos de lógica de programação, organização de código, tratamento de erros e utilização de bibliotecas externas.

## 🚀 Funcionalidades

A calculadora oferece:

### Operações básicas
- Adição
- Subtração
- Multiplicação
- Divisão

### Operações avançadas
- Raiz quadrada
- Raiz cúbica
- Porcentagem
- Exponenciação

### Gráficos de funções
- Trabalha com funções matemáticas.
- Gera representações gráficas utilizando recursos de Python.
- Permite obter uma imagem do gráfico gerado.

### Histórico de operações
- Registra os cálculos realizados.
- Permite consultar operações anteriores.
- Armazena o histórico para consultas posteriores.

## 🛠️ Tecnologias

- **Python:** linguagem principal do projeto.
- **Terminal:** interface de execução e interação.
- **Biblioteca gráfica:** utilizada para geração de gráficos e imagens.
- **Armazenamento local:** utilizado para registrar o histórico de cálculos.

## 📋 Pré-requisitos

Antes de iniciar, tenha instalado:

1. Python 3, em uma versão compatível com as dependências do projeto.
2. Git (opcional, para clonar o repositório).
3. Um terminal, como PowerShell, Prompt de Comando ou terminal do VS Code.

### Verificar a instalação do Python

Abra o terminal e execute:

```bash
python --version
```

Se o comando não funcionar, tente:

```bash
py --version
```

Se o Python não estiver instalado, faça o download pelo site oficial:

https://www.python.org/downloads/

No Windows, configure a instalação para permitir a utilização do Python pelo terminal.

## 📥 Como baixar o projeto

### Opção 1 — Download pelo GitHub

1. Acesse o repositório:

   https://github.com/Saganski/alura-ai-software-engineering

2. Clique no botão verde **Code**.
3. Selecione **Download ZIP**.
4. Extraia o arquivo baixado.
5. Abra a pasta `desafio-02`.

### Opção 2 — Clonar usando Git

No terminal, execute:

```bash
git clone https://github.com/Saganski/alura-ai-software-engineering.git
```

Depois, acesse a pasta do projeto:

```bash
cd alura-ai-software-engineering/desafio-02
```

## ⚙️ Preparação do ambiente

É recomendado utilizar um ambiente virtual Python para manter as bibliotecas do projeto separadas das demais instalações.

### No Windows

Crie o ambiente virtual:

```powershell
python -m venv .venv
```

Ative pelo Prompt de Comando:

```cmd
.venv\Scripts\activate.bat
```

Ou pelo PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a ativação, é possível utilizar o Prompt de Comando ou executar diretamente o Python do ambiente virtual.

### No Linux ou macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 📦 Instalando as dependências

Com o ambiente virtual ativado, execute:

```bash
python -m pip install -r requirements.txt
```

Esse comando instalará as bibliotecas externas necessárias, conforme especificadas no arquivo `requirements.txt`.

### Configuração do gerador de gráficos

A funcionalidade de geração de gráficos depende da biblioteca utilizada na implementação.

Antes de executar o projeto, certifique-se de que todas as dependências de geração de gráficos estejam incluídas no arquivo `requirements.txt`.

Se houver recursos adicionais, como ferramentas externas, configurações específicas do sistema operacional ou extensões do editor, eles deverão ser instalados conforme as instruções complementares do projeto.

## ▶️ Como executar a calculadora

Com o terminal aberto dentro da pasta `desafio-02` e as dependências instaladas, execute:

```bash
python calculadora.py
```

No Windows, também pode ser utilizado:

```bash
py calculadora.py
```

A calculadora será iniciada no terminal, onde você poderá acessar as funcionalidades disponíveis.

## 📊 Utilizando os gráficos

A aplicação possui recursos para trabalhar com funções matemáticas e gerar seus respectivos gráficos.

Para utilizar:

1. Execute a calculadora pelo terminal.
2. Acesse a funcionalidade de funções ou geração de gráficos no menu.
3. Informe os valores ou a expressão solicitada.
4. Siga as instruções exibidas no programa.
5. Consulte a visualização ou a imagem gerada pela ferramenta gráfica.

**Observação:** o local de salvamento das imagens depende da configuração implementada no código.

## 🕘 Histórico de cálculos

A calculadora possui uma funcionalidade de registro de operações, permitindo recuperar informações sobre cálculos anteriores.

O armazenamento é realizado localmente, conforme a implementação do projeto.

O histórico não é sincronizado automaticamente entre diferentes computadores.

## ❗ Solução de problemas

### Python não é reconhecido

Verifique se o Python está instalado e disponível no terminal.

No Windows, tente utilizar `py` em vez de `python`.

### Erro `ModuleNotFoundError`

Esse erro geralmente indica que alguma biblioteca não foi instalada no ambiente Python em uso.

Execute novamente:

```bash
python -m pip install -r requirements.txt
```

### O gráfico não é gerado

Verifique se as dependências gráficas estão instaladas, se a expressão matemática foi informada corretamente e se o programa possui permissão para salvar arquivos no diretório utilizado.

### O histórico não está sendo salvo

Verifique as permissões de escrita da pasta e se o arquivo utilizado para armazenamento pode ser criado ou atualizado.

## 📚 Aprendizados

O desenvolvimento deste desafio contribui para a prática de:

- Lógica e programação em Python.
- Organização e evolução de projetos.
- Operações matemáticas.
- Utilização de bibliotecas externas.
- Representação gráfica de funções.
- Persistência local de dados.
- Tratamento de entradas e erros.
- Documentação de software.

## 👨‍💻 Desenvolvedor

**Miguel Saganski**

GitHub: https://github.com/Saganski

Projeto desenvolvido como parte dos desafios da Imersão Alura — Engenharia de Software: Dev na Era da IA.

---

*Este repositório registra a evolução prática dos conhecimentos adquiridos durante a imersão.*
