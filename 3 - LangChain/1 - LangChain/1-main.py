import sys
from groq import Groq
from dotenv import load_dotenv
import os

# Console no Windows: saída em UTF-8 para acentos e emojis
if hasattr(sys.stdout, "reconfigure") and getattr(sys.stdout, "encoding", "") != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

numero_dias = 3
numero_pessoas = 2
atividade = "caminhada"


prompt = f"Crie um roteiro de viagens, para um período de {numero_dias} dias, para uma familia com {numero_pessoas} crianças, que gosta de {atividade}."


cliente = Groq(api_key=api_key)

resposta = cliente.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "Você é um assistente de roteiro de viagens."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)


print(resposta)

resposta_em_texto = resposta.choices[0].message.content
print(resposta_em_texto)