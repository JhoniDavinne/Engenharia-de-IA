## Desafio: Melhorar o Atendimento ao Cliente

Você foi contratado como analista em uma empresa de tecnologia e recebeu a seguinte demanda do time de Customer Success (Sucesso do Cliente):

> “Precisamos melhorar a forma como lidamos com os pedidos de suporte dos usuários. As mensagens chegam com vários problemas misturados, como dificuldades para acessar o sistema, dúvidas sobre pagamento ou erros no uso de funcionalidades. Está tudo confuso e difícil de responder de forma ágil.”

Utilize os principais fundamentos do pensamento computacional para propor um plano que ajude a organizar e automatizar o atendimento. Considere:

> Como decompor o problema?

> É possível reconhecer padrões nos pedidos?

> Que tipo de abstrações pode ser criada para simplificação do fluxo?

> É viável criar um algoritmo para lidar com cada tipo de solicitação?


Uma forma possível de resolver esse desafio é:

- **Decomposição**: separar os atendimentos em categorias (acesso, pagamento, uso da plataforma).
- **Padrões**: identificar que muitas dúvidas se repetem em cada categoria.
- **Abstração**: criar modelos de resposta ou uma FAQ automática.
- **Algoritmo**: montar um fluxo de decisão simples para atendimento:  
    *Recebeu mensagem → Identifica categoria → Verifica se há resposta padrão → Envia ou encaminha.*