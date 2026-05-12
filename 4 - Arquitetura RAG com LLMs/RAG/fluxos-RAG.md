# Fluxos do RAG (Retrieval Augmented Generation)

Este documento descreve a funcionalidade de cada fluxo do diagrama **RAG** aplicado a uma base de conhecimento de RH, conforme o material da Alura.

O sistema divide-se em **dois fluxos principais**: preparação da base (offline ou assíncrona) e atendimento à pergunta do usuário (online).

---

## Visão geral

| Fluxo | Objetivo |
|--------|-----------|
| **Ingestão** | Transformar documentos em representações numéricas pesquisáveis e guardá-las. |
| **Consulta e geração** | Recuperar trechos relevantes e produzir uma resposta fundamentada no contexto recuperado. |

---

## Fluxo 1 — Preparação da base (ingestão)

**Caminho:** Base de conhecimento → Transformação em vetores (embeddings) → Vector Store.

### 1. Base de conhecimento de um RH

- **Função:** É a **fonte de verdade** antes do modelo “aprender” por recuperação.
- Conteúdo típico: PDFs, planilhas (Excel), bases de dados, documentos de texto e outros formatos onde estão políticas, benefícios, regras internas, etc.
- **Por que importa:** O LLM sozinho não tem esses dados atualizados nem autoridade sobre o que é verdade na empresa; o RAG injeta pedaços desses documentos na hora da resposta.

### 2. Transformação de texto em vetores numéricos (embeddings)

- **Função:** Converter trechos de texto em **vetores** (listas de números) que capturam significado de forma aproximada.
- Um **modelo de embeddings** codifica “semelhança de sentido”: textos parecidos ficam com vetores mais próximos no espaço matemático.
- **Saída:** Embeddings prontos para comparação por similaridade, não para leitura humana direta.

### 3. Armazenamento em Vector Store

- **Função:** Guardar os embeddings (e, em geral, o texto original ou metadados associados) em um **banco vetorial** otimizado para busca por proximidade.
- **Papel no sistema:** Permite que, dada uma pergunta também convertida em vetor, o sistema encontre rapidamente os **trechos mais relevantes** da base, em escala.

**Resumo do fluxo 1:** documentos brutos → fragmentação/limpeza (implícita no processo) → vetores → persistência para busca semântica.

---

## Fluxo 2 — Consulta, recuperação e geração

**Caminho:** Pergunta do usuário → Retriever ↔ Vector Store → LLM (pergunta + contexto externo) → Resposta.

### 1. Pergunta do usuário

- Exemplo do diagrama: *“Quais são as regras de retirada da cestas de Natal?”*
- **Função:** É a **intenção** que dispara toda a cadeia: sem ela não há critério de busca nem foco na resposta.

### 2. Retriever (recuperador)

- **Função:** Orquestrar a **busca** no conhecimento indexado.
- Em geral: a pergunta é transformada no **mesmo tipo de embedding** usado na ingestão; o retriever compara com o Vector Store e traz os **top-k** trechos mais similares (ou usa outra estratégia híbrida, dependendo da implementação).
- A ligação **bidirecional** com o Vector Store no diagrama representa o **ciclo de consulta à base**: consulta → resultados; em alguns desenhos isso também sugere leitura/atualização, mas o núcleo operacional é **recuperar contexto** alinhado à pergunta.

### 3. LLM com pergunta + contexto externo

- **Função:** O modelo de linguagem recebe **dois insumos**:
  1. A **pergunta** (ou instrução) do usuário.
  2. O **contexto externo** retornado pelo retriever (trechos da base de RH).
- **Efeito:** A geração fica **ancorada** no material recuperado, reduzindo invenção de fatos em relação à política real (quando o contexto é correto e suficiente).
- **Nome no diagrama:** “LLM com pergunta + contexto externo” — é o **núcleo de augmented generation**: gerar texto **aumentado** pela recuperação.

### 4. Resposta

- **Função:** Texto final apresentado ao usuário (no diagrama, associado ao ícone de “ideia” / lâmpada).
- Idealmente: **clara**, **alinhada aos documentos** citados implicitamente pelo contexto e, em produção, muitas vezes com **citações** ou indicação de fonte para auditoria.

**Resumo do fluxo 2:** pergunta → busca semântica na base vetorial → montagem do prompt (pergunta + trechos) → geração pela LLM → resposta.

---

## Como os dois fluxos se conectam

- O **fluxo de ingestão** constrói e mantém o **Vector Store**.
- O **fluxo de consulta** depende desse armazenamento: sem ingestão prévia (ou atualização periódica), o retriever não tem o que buscar ou devolve informação desatualizada.
- **Atualizações** na base de RH exigem **reprocessar** documentos novos ou alterados e **atualizar** o Vector Store para o RAG refletir as regras atuais.

---

## Referência visual

Diagrama de origem: `RAG.png` (mesma pasta deste arquivo).


Pergunta -> Embedding -> Vector Store -> Top-k trechos -> LLM com pergunta + contexto externo -> Resposta
