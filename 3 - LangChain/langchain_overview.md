# LangChain -- Visão Geral

**LangChain** é um **framework para desenvolver aplicações baseadas em
LLMs (Large Language Models)**.\
Ele facilita integrar modelos de linguagem com **dados externos,
ferramentas e lógica de software**.

Foi criado para resolver um problema comum: LLMs como GPT, Claude ou
Llama sozinhos apenas geram texto. Aplicações reais normalmente precisam
de:

-   acesso a **bancos de dados**
-   **memória de conversa**
-   execução de **ferramentas ou APIs**
-   pipelines de prompts
-   recuperação de documentos (RAG)

O LangChain fornece abstrações para organizar esses componentes.

------------------------------------------------------------------------

# Componentes Principais

## 1. Chains

Uma **Chain** é uma sequência de operações envolvendo LLMs.

Exemplo de pipeline:

    Pergunta do usuário
            ↓
    Buscar documentos (Vector DB)
            ↓
    Construir prompt
            ↓
    Enviar para LLM
            ↓
    Resposta final

------------------------------------------------------------------------

## 2. Agents

**Agents** permitem que o LLM **decida quais ferramentas usar**.

Ferramentas comuns:

-   consulta SQL
-   chamadas de API
-   busca na web
-   execução de código

Fluxo típico:

    Pergunta → LLM decide ação → executa ferramenta → retorna resultado → resposta final

------------------------------------------------------------------------

## 3. Memory

Permite manter **contexto de conversa** entre mensagens.

Exemplo:

    User: Qual é a capital da França?
    LLM: Paris

    User: Qual a população dela?

A memória permite entender que **"dela" se refere a Paris**.

------------------------------------------------------------------------

## 4. RAG (Retrieval Augmented Generation)

Muito usado em aplicações corporativas.

Fluxo típico:

    Documentos → embeddings → vector database
                             ↓
                       busca semântica
                             ↓
                       contexto para LLM

Vector databases comuns:

-   Pinecone
-   Weaviate
-   Chroma

------------------------------------------------------------------------

# Exemplo simples (Python)

``` python
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4")

prompt = ChatPromptTemplate.from_template(
    "Explique {tema} de forma simples."
)

chain = prompt | llm

response = chain.invoke({"tema": "Docker"})
print(response)
```

------------------------------------------------------------------------

# Casos de Uso na Prática

LangChain é frequentemente usado para:

1.  **Chatbots corporativos**
2.  **Chat com documentos (PDF, Notion, Confluence)**
3.  **Assistentes de código**
4.  **Automação com IA**
5.  **Agentes autônomos**

Exemplo de fluxo:

    Usuário pergunta
          ↓
    Busca em documentos da empresa
          ↓
    LLM responde baseado nesses documentos

------------------------------------------------------------------------

# Limitações

Problemas frequentemente citados por desenvolvedores:

-   abstração excessiva
-   debug difícil
-   mudanças frequentes na API
-   overhead desnecessário em projetos simples

Por isso alguns projetos usam alternativas como:

-   LlamaIndex
-   Haystack

------------------------------------------------------------------------

# Resumo

  Conceito    Significado
  ----------- ---------------------------------------------
  LangChain   Framework para construir aplicações com LLM
  Chains      Pipelines de chamadas ao modelo
  Agents      LLM decide quais ferramentas usar
  Memory      Mantém contexto de conversa
  RAG         LLM combinado com base de conhecimento
