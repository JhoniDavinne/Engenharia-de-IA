import os 
import sys
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

modelo = ChatGroq(
    groq_api_key=api_key,
    model="openai/gpt-oss-120b",
    temperature=0.5,
)

memoria = {}
sessao = "aula_langchain_alura"

prompt_sugestao = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um assistente de viagem que sugere destinos para viajantes."),
        ("placeholder", "{historico}"),
        ("human", "{query}")
    ]
)

cadeia = prompt_sugestao | modelo | StrOutputParser()

def historico_por_sessao(sessao: str):
    print(f"Recuperando histórico para a sessão: {sessao}")
    if sessao not in memoria:
        memoria[sessao] = InMemoryChatMessageHistory()
    return memoria[sessao]
        

perguntas = [
    "Quero visitar um lugar no Brasil, famoso por praias e cultura. Pode sugerir?",
    "Qual a melhor época do ano para ir?"
]

cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=cadeia, 
    get_session_history=historico_por_sessao, 
    input_messages_key="query",
    history_messages_key="historico"
)

for pergunta in perguntas:
    resposta = cadeia_com_memoria.invoke(
        {
            "query": pergunta,
        },
        config={"session_id": sessao}
    )
    print("Usuario: ", pergunta)
    print("IA: ", resposta, "\n")
    print("-" * 100)