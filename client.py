import asyncio
import os
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Inicializa o modelo LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

# Criação de um PromptTemplate que recebe a pergunta
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="Extraia e retorne apenas a expressão matemática da seguinte pergunta: {question}"
)

# Cria a LLMChain com o modelo e o prompt template
chain = LLMChain(prompt=prompt_template, llm=llm)

# Define os parâmetros do servidor MCP
server_params = StdioServerParameters(
    command="python",
    args=["server.py"],
)

async def run_agent():
    print("Iniciando o agente...")

    # Conecta com o servidor MCP via stdio
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Usa a LLMChain para obter a expressão matemática
            expression = await chain.apredict(question="quanto é 5 mais 5 menos 2 e dividido para 2?")
            print(f"Expressão extraída: {expression}")

            # Agora chama a ferramenta 'calculate_expression' com a expressão extraída
            result = await session.call_tool("calculate_expression", {"expr": expression})
            print("Resultado:", result)

if __name__ == "__main__":
    asyncio.run(run_agent())
