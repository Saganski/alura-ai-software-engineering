# 🧮 Calculadora Científica em Python

**Desafio 02 | Imersão Engenharia de Software: Dev na Era da IA — Alura + Google**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Gráficos-11557C?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-Projeto-181717?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Funcional-22C55E?style=for-the-badge)

---

## 📖 Sobre o projeto

A **Calculadora Científica em Python** foi desenvolvida como parte do segundo desafio da Imersão Engenharia de Software: Dev na Era da IA, promovida pela Alura em parceria com o Google.

O projeto representa uma evolução da calculadora básica desenvolvida no primeiro desafio, incorporando operações matemáticas avançadas, geração de gráficos de funções e armazenamento persistente do histórico de cálculos.

O desenvolvimento tem como objetivo aplicar conceitos de engenharia de software, programação orientada a objetos, tratamento de exceções, utilização de bibliotecas externas e persistência de dados.

A aplicação funciona diretamente pelo **terminal**, sem necessidade de hospedagem ou navegador.

## ✨ Funcionalidades

### 🧮 Operações matemáticas

| Operação | Exemplo de comando | Resultado |
|---|---|---|
| Adição | `15 + 7` | 22 |
| Subtração | `20 - 8` | 12 |
| Multiplicação | `6 * 7` | 42 |
| Divisão | `10 / 2` | 5 |
| Exponenciação | `2 ^ 8` | 256 |
| Raiz quadrada | `raiz 25` | 5 |
| Raiz cúbica | `27 raiz 3` | 3 |
| Raiz n-ésima | `16 raiz 4` | 2 |
| Porcentagem | `200 % 15` | 30 |
| Conversão percentual | `15 %` | 0.15 |

A calculadora também permite utilizar números decimais e possui tratamento de erros para operações inválidas.

### 📈 Gerador de gráficos científicos

A aplicação conta com integração à biblioteca **Matplotlib**, permitindo visualizar gráficos de funções matemáticas em uma janela interativa.

Entre as funcionalidades estão:

- Representação de funções matemáticas.
- Personalização do intervalo dos eixos.
- Visualização dos eixos cartesianos.
- Grade de referência e identificação da função.
- Suporte a funções trigonométricas, exponenciais e logarítmicas.

**Exemplos de funções aceitas:**

```python
x^2 - 4
2*x + 1
sin(x)
cos(x)*2
sqrt(x)
log(x)
exp(x)
abs(x)
```

> **Importante:** a implementação atual abre uma janela do Matplotlib para visualizar os gráficos. O salvamento automático em PNG ou JPG ainda não está implementado.

### 🕘 Histórico persistente

A calculadora registra automaticamente as operações realizadas com sucesso.

- Histórico armazenado localmente em JSON.
- Registro da expressão matemática, resultado e horário.
- Armazenamento das 100 operações mais recentes.
- Recuperação do histórico ao iniciar novamente a aplicação.
- Opção para consultar e limpar os registros.

O histórico é mantido no arquivo `historico_calculos.json`, criado automaticamente na pasta do projeto.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3 | Linguagem principal |
| Matplotlib | Geração e visualização de gráficos |
| JSON | Persistência do histórico |
| Math | Operações e funções matemáticas |
| Datetime | Registro dos horários |
| Git e GitHub | Versionamento e compartilhamento do projeto |

O desenvolvimento utiliza programação orientada a objetos para organizar as operações matemáticas e funcionalidades da calculadora.

---

## 📁 Estrutura do projeto

```text
desafio - 02/
│
├── calculadora.py
├── README.md
├── requirements.txt
└── .gitignore
```

Após a execução de cálculos, também poderá ser criado:

```text
historico_calculos.json
```

Esse arquivo é armazenado localmente e está configurado para ser ignorado pelo Git.

---

## 📋 Pré-requisitos

Antes de executar o projeto, é necessário ter:

- Python 3 instalado.
- Um terminal, como PowerShell, Prompt de Comando ou terminal do VS Code.
- Conexão com a internet para instalar as dependências.
- Ambiente gráfico no sistema operacional para visualizar os gráficos.

O Git é opcional caso você prefira baixar o projeto em formato ZIP.

### Verificando o Python

Abra seu terminal e execute:

```bash
python --version
```

No Windows, também pode utilizar:

```bash
py --version
```

Caso o Python não esteja instalado, acesse:

https://www.python.org/downloads/

---

## 📥 Como baixar o projeto

### Opção 1 — Download ZIP

1. Acesse o [repositório no GitHub](https://github.com/Saganski/alura-ai-software-engineering).
2. Clique no botão verde **Code**.
3. Selecione **Download ZIP**.
4. Extraia os arquivos em uma pasta do computador.
5. Entre na pasta `desafio - 02`.
6. Abra um terminal dentro dessa pasta.

### Opção 2 — Clonar com Git

Execute:

```bash
git clone https://github.com/Saganski/alura-ai-software-engineering.git
```

Depois, acesse o segundo desafio:

```bash
cd "alura-ai-software-engineering/desafio - 02"
```

> As aspas são necessárias porque o nome da pasta contém espaços.

---

## ⚙️ Configuração do ambiente

Recomenda-se criar um ambiente virtual Python para manter as dependências organizadas.

### Windows

Crie o ambiente virtual:

```powershell
python -m venv .venv
```

Ative pelo PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Ou pelo Prompt de Comando:

```cmd
.venv\Scripts\activate.bat
```

Se o PowerShell bloquear a ativação, utilize o Prompt de Comando ou execute diretamente o Python do ambiente virtual.

### Linux e macOS

Crie e ative o ambiente:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 📦 Instalação do gerador de gráficos

Para utilizar a funcionalidade de gráficos, é necessário instalar a biblioteca **Matplotlib**.

Ela é responsável por criar os gráficos, desenhar os eixos cartesianos e exibir as funções matemáticas.

### Método recomendado

Com o terminal aberto na pasta `desafio - 02`, e o ambiente virtual ativado, execute:

```bash
python -m pip install -r requirements.txt
```

O arquivo `requirements.txt` deve conter:

```text
matplotlib
```

Esse comando instala o Matplotlib e suas dependências automaticamente.

### Instalação manual

Se preferir, instale diretamente:

```bash
python -m pip install matplotlib
```

### Verificar se a instalação funcionou

Execute:

```bash
python -c "import matplotlib; print(matplotlib.__version__)"
```

Se aparecer o número da versão instalada, a biblioteca foi encontrada corretamente.

**Observação:** não é necessário instalar extensões adicionais do VS Code para gerar gráficos. O Matplotlib é uma biblioteca Python, não uma extensão do editor.

---

## ▶️ Como executar a calculadora

Com o terminal aberto dentro da pasta do desafio, execute:

```bash
python calculadora.py
```

No Windows, você também pode utilizar:

```bash
py calculadora.py
```

O programa apresentará as operações disponíveis e aguardará um comando.

### Exemplo de utilização

```text
CALCULADORA CIENTÍFICA EM PYTHON

Operações disponíveis:

+    : Soma
-    : Subtração
*    : Multiplicação
/    : Divisão
^    : Exponenciação
raiz : Raiz
%    : Porcentagem
g    : Gráfico de f(x)
h    : Ver Histórico
c    : Limpar Histórico
s    : Sair
```

Para realizar um cálculo, basta digitar a expressão desejada.

Exemplo:

```text
Digite a operação: 25 * 4

=> Resultado: 100
```

---

## 📊 Como gerar gráficos

O gerador de gráficos permite visualizar funções matemáticas utilizando o Matplotlib.

### Passo a passo

**1.** Inicie a calculadora:

```bash
python calculadora.py
```

**2.** Digite o comando:

```text
g
```

**3.** Informe a função desejada:

```text
x^2 - 4
```

**4.** Informe o intervalo inicial e final de X.

Exemplo:

```text
Digite o valor inicial de X [Padrão: -10]: -10
Digite o valor final de X [Padrão: 10]: 10
```

Se desejar utilizar os valores padrão, basta pressionar Enter nos campos.

**5.** Uma janela será aberta exibindo o gráfico da função.

**6.** Feche a janela do gráfico para retornar ao terminal.

### Exemplos de funções

| Tipo | Expressão |
|---|---|
| Linear | `2*x + 1` |
| Quadrática | `x^2 - 4` |
| Cúbica | `x^3` |
| Seno | `sin(x)` |
| Cosseno | `cos(x)` |
| Raiz quadrada | `sqrt(x)` |
| Logarítmica | `log(x)` |
| Exponencial | `exp(x)` |
| Valor absoluto | `abs(x)` |

**Atenção:** utilize `*` para indicar multiplicação, como em `2*x`, e não `2x`.

As funções `log(x)` e `sqrt(x)` possuem restrições matemáticas de domínio. Valores inválidos não serão representados no gráfico.

---

## 💾 Histórico de cálculos

O histórico é armazenado automaticamente no arquivo:

```text
historico_calculos.json
```

O arquivo fica localizado na mesma pasta de `calculadora.py`.

O armazenamento é local e não depende de conexão com a internet.

### Consultar histórico

Com a calculadora em execução, digite:

```text
h
```

O programa exibirá os cálculos anteriores, incluindo resultados e horários.

### Limpar histórico

Digite:

```text
c
```

O histórico será apagado.

### Persistência

Ao encerrar a calculadora e executá-la novamente, as operações anteriores continuarão disponíveis, desde que o arquivo de histórico não tenha sido excluído.

O programa mantém até 100 operações recentes.

O arquivo JSON está incluído nas regras do `.gitignore` para evitar o envio acidental do histórico pessoal ao repositório.

---

## 🔧 Recursos adicionais — Integração via JSON

Além do modo interativo, a calculadora possui recursos para receber operações através de argumentos JSON no terminal.

Isso permite utilizar sua lógica em integrações futuras com outras aplicações.

### Exemplo de cálculo

No Bash:

```bash
python calculadora.py --eval '{"a":10,"op":"+","b":5}'
```

### Consultar o histórico em JSON

```bash
python calculadora.py --historico
```

### Limpar o histórico pelo terminal

```bash
python calculadora.py --limpar-historico
```

Também existem argumentos para cálculos unários e geração de gráficos.

> O formato de aspas para argumentos JSON pode variar conforme o terminal utilizado, especialmente entre PowerShell, Prompt de Comando e Bash.

---

## ❗ Solução de problemas

### Python não é reconhecido

Verifique se o Python está instalado e disponível no terminal.

No Windows, tente:

```bash
py --version
```

Caso necessário, reinstale o Python utilizando o instalador oficial.

### Erro `ModuleNotFoundError: No module named 'matplotlib'`

Indica que o Matplotlib não está instalado no ambiente Python utilizado para executar a calculadora.

Execute:

```bash
python -m pip install matplotlib
```

Se você utiliza um ambiente virtual, certifique-se de que ele esteja ativado.

### O gráfico não aparece

Verifique:

1. Se o Matplotlib está instalado.
2. Se a expressão matemática está correta.
3. Se o intervalo inicial de X é menor que o final.
4. Se o sistema possui um ambiente gráfico disponível.

A funcionalidade foi desenvolvida para abrir uma janela interativa, portanto pode não funcionar normalmente em terminais sem interface gráfica.

### O histórico não está sendo salvo

Verifique se a pasta do projeto permite a criação e alteração de arquivos.

A aplicação precisa de permissão de escrita para criar e atualizar `historico_calculos.json`.

### Erro na expressão matemática

Confira se a sintaxe segue os padrões aceitos.

Por exemplo:

- Correto: `2*x + 1`
- Incorreto: `2x + 1`

---

## 🧠 Conceitos e aprendizados

Durante o desenvolvimento deste desafio, foram trabalhados:

- Lógica de programação e algoritmos.
- Programação orientada a objetos.
- Métodos e organização de classes.
- Tratamento de exceções e validação.
- Manipulação de números e operações matemáticas.
- Integração de bibliotecas Python.
- Representação gráfica de funções.
- Persistência de dados utilizando JSON.
- Manipulação de arquivos locais.
- Argumentos de linha de comando.
- Documentação e versionamento de projetos.

---

## 🔄 Evolução do projeto

| Funcionalidade | Desafio 01 | Desafio 02 |
|---|:---:|:---:|
| Operações básicas | ✅ | ✅ |
| Tratamento de erros | ✅ | ✅ |
| Histórico de cálculos | ✅ | ✅ |
| Exponenciação | — | ✅ |
| Raízes | — | ✅ |
| Porcentagem | — | ✅ |
| Gráficos de funções | — | ✅ |
| Persistência do histórico | — | ✅ |
| Integração via JSON | — | ✅ |

O segundo desafio amplia as funcionalidades da primeira versão e introduz novos recursos matemáticos e de integração.

---

## 🚀 Possíveis melhorias futuras

- Exportação de gráficos em PNG ou PDF.
- Testes automatizados das operações.
- Interface gráfica personalizada.
- Ampliação das funções matemáticas.
- Melhorias na organização e validação do código.

---

## 👨‍💻 Desenvolvedor

**Miguel Saganski**

[![GitHub](https://img.shields.io/badge/GitHub-Saganski-181717?style=flat&logo=github&logoColor=white)](https://github.com/Saganski)

Projeto desenvolvido para fins de estudo, prática e evolução profissional durante a Imersão Engenharia de Software: Dev na Era da IA.

---

**Desafio 02 — Calculadora Científica em Python**

*Aprendizado prático, evolução contínua e desenvolvimento de soluções com tecnologia.*
