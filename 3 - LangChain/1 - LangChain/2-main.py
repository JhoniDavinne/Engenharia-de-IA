import sys
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

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

numero_dias = 7
numero_pessoas = 4
atividade = "praia"

modelo_de_prompt = PromptTemplate(
    template="""
    Crie um roteiro de viagens de {numero_dias} dias, 
    para uma familia com {numero_pessoas} crianças, 
    que gostam de {atividade}.
    """,
    input_variables=["numero_dias", "numero_pessoas", "atividade"],
)

prompt = modelo_de_prompt.format(numero_dias=numero_dias, numero_pessoas=numero_pessoas, atividade=atividade)

print("Prompt: \n", prompt)

llm = ChatGroq(
    groq_api_key=api_key,
    model="openai/gpt-oss-120b",
    temperature=0.5,
)

resposta = llm.invoke(
    [
        SystemMessage(content="Você é um assistente de roteiro de viagens."),
        HumanMessage(content=prompt),
    ]
)


print(resposta)

resposta_em_texto = resposta.content
print(resposta_em_texto)
