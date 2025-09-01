

# 💳 Sistema Bancário em Python


   
## Santander 2025 - Back-End com Python 
📄 Licença
Projeto desenvolvido durante o curso Back-End com Python (2025), oferecido pelo Santander, com a orientação do instrutor Guilherme Carvalho.

Este curso é muito bom e excelente, proporcionando aprendizado prático e direto em desenvolvimento Python, com enfoque em projetos reais e funcionalidades de sistemas bancários. 😉

🔗 Links Úteis
Santander 2025 - Back-End com Python <a href="https://web.dio.me/track/santander-2025-python-back-end"><strong>➥ Link </strong></a>

Digital Innovation One

Desenvolvido como parte do Bootcamp Santander 2025 - Back-End com Python




![Banner 1](banner1.JPG)
![Banner 2](banner2.JPG)
![Banner 3](banner3.JPG)



---

## 📌 Sobre o Projeto
Este é um sistema bancário simples desenvolvido em **Python**, como parte dos estudos do **Santander Bootcamp 2025 - Back-End com Python**.  
O projeto simula operações bancárias básicas, como depósitos, saques, Pix, débito e exibição de extrato.

---

## 🚀 Funcionalidades
- ✅ **Depósito: Adicionar valores à conta, com validação de valores válidos.  
- ✅ **Saque: Retirar valores com limite diário, saldo suficiente e controle por tipo (Débito, Pix ou Saque comum).
- ✅ **Pix: Realizar transferências instantâneas com limite específico.
- ✅ **Débito: Retirar valores diretamente da conta com limite definido. 
- ✅ **Extrato: Consultar todas as movimentações realizadas e saldo atual.
- ✅ **Limites e segurança: Controla limites de débito, Pix, saque e número máximo de saques diários.

---

## 📂 Estrutura do Código

Banner Inicial: Exibe identificação do projeto e autor.

Menu Principal: Opções interativas para Débito, Pix, Depósito, Saque, Extrato e Sair.

Variáveis de Controle:

saldo, extrato → controle do saldo e histórico de movimentações

limite_debito, limite_pix, limite_saque → limites por tipo de transação

saques_debito, saques_pix, saques_comum → contador de saques diários

Funções Principais:

depositar(saldo, extrato) → realiza depósitos

sacar(saldo, extrato, tipo, limite, contador_saques) → realiza saques e Pix com validações

exibir_extrato(saldo, extrato) → imprime o extrato detalhado

Loop Principal: Mantém o sistema rodando até o usuário selecionar Sair.
