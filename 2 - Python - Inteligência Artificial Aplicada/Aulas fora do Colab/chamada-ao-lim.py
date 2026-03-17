import sys
from openai import OpenAI

# Evita UnicodeEncodeError no Windows quando a resposta tem emojis
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="qualquer-coisa",
)

response = client_openai.chat.completions.create(
    model="google/gemma-3-4b",
    messages=[
        {"role": "system", "content": "Você é um assistente de IA prestativo que responde em português brasileiro."}, 
        {"role": "user", "content": "O que é a Inteligência Artificial?"}
    ],
    temperature=1.0,
    
)

print(response.choices[0].message.content)