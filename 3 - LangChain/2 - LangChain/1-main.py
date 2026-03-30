import sys
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Console no Windows: saída em UTF-8 para acentos e emojis
if hasattr(sys.stdout, "reconfigure") and getattr(sys.stdout, "encoding", "") != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
    
# Carrega as variáveis do arquivo .env
load_dotenv()
# Acessa a chave de uma API de forma segura
api_key = os.getenv("GROQ_API_KEY")

if api_key is None:
    raise ValueError("A chave da API não foi definida no .env")

print("Chave carregada com sucesso!")


prompt_cidade = PromptTemplate(
    template="""
    Sugira uma cidade dado o meu interesse por {interesse}.
    """,
    input_variables=["interesse"],
)

modelo = ChatGroq(
    groq_api_key=api_key,
    model="openai/gpt-oss-120b",
    temperature=0.5,
)

cadeia = prompt_cidade | modelo | StrOutputParser()

# O ChatGroq não aceita o dict do template; o PromptTemplate da cadeia formata o texto primeiro.
resposta = cadeia.invoke({"interesse": "praias"})
print(resposta)