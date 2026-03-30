import os 
import sys
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import Literal, TypedDict

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

modelo = ChatGroq(
    groq_api_key=api_key,
    model="llama-3.3-70b-versatile",
    temperature=0.5,
)

prompt_consultor_praia = ChatPromptTemplate.from_messages(
    [
        ("system", "Apresente-se como Sra Praia. Você é uma especialista em viagens com destinos para praias."),
        ("human", "{query}")
    ]
)

prompt_consultor_montanha = ChatPromptTemplate.from_messages(
    [
        ("system", "Apresente-se como Sro Montanha. Você é uma especialista em viagens com destinos para montanhas e atividades radicais."),
        ("human", "{query}")
    ]
)

cadeia_praia = prompt_consultor_praia | modelo | StrOutputParser()
cadeia_montanha = prompt_consultor_montanha | modelo | StrOutputParser()

class Rota(TypedDict):
    destino: Literal["praia", "montanha"]

prompt_roteador = ChatPromptTemplate.from_messages(
    [
        ("system", "Responda apenas com 'praia' ou 'montanha'."),
        ("human", "{query}")
    ]
)

roteador = prompt_roteador | modelo.with_structured_output(Rota)

def response(pergunta: str):
    rota = roteador.invoke({"query": pergunta})["destino"]
    if rota == "praia":
        return cadeia_praia.invoke({"query": pergunta})
    else:
        return cadeia_montanha.invoke({"query": pergunta})
    
print(response("Quero surfar em um lugar quente"))

    