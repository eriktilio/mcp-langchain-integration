# LangChain + Gemini + MCP (Tool Server)

Este projeto demonstra como criar um chain com LangChain usando o modelo **gemini-2.0-flash** do Google e integrá-lo com ferramentas customizadas usando o **MCP** (Multi-Chain Protocol), via conexão `stdio`.

## ✨ Funcionalidade

A chain é capaz de:

- Interpretar linguagem natural com o Gemini.
- Usar ferramentas externas via MCP — neste exemplo, uma calculadora de expressões matemáticas.
- Executar localmente um servidor de ferramentas que se conecta à chain automaticamente.

## 🔧 Requisitos

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (ou `pip` tradicional)

## 📦 Instalação

#### Com uv (recomendado)

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

#### Ou com pip tradicional

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### Crie um arquivo .env:

```bash
GOOGLE_API_KEY=sua_chave_google_api
```

## 🚀 Execução

### 1. Execute o servidor de ferramentas (MCP)

Primeiro, execute o servidor de ferramentas. Este servidor vai processar as expressões matemáticas.

```bash
python server.py
```

### 2. Execute o cliente

Em seguida, execute o cliente, que se conecta ao servidor e faz as requisições, passando a pergunta para a chain e recebendo o resultado do cálculo.

```bash
python client.py
```

### Como Funciona?

- O chain usa o modelo Gemini-Pro do Google para interpretar a linguagem natural.
- Uma LLMChain é criada usando o modelo e um PromptTemplate para extrair a expressão matemática de uma pergunta.
- A expressão extraída é então passada para uma ferramenta de cálculo via o protocolo MCP.
- O servidor MCP calcula a expressão matemática e retorna o resultado.
