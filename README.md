# Criando um Sistema Bancário com Python
## Desafio

Este projeto tem como objetivo desenvolver um sistema bancário simples utilizando a linguagem de programação Python. A proposta do sistema é modernizar as operações básicas de um banco. A versão inicial do sistema abrange três operações principais: depósito, saque e visualização de extrato. A simplicidade do projeto permite uma implementação direta, sem a necessidade de gerenciar múltiplas contas ou agências, focando apenas na lógica central dessas operações bancárias.
## Objetivo
Criar um sistema bancário com as seguintes operações:

* **1. Depositar**
* **2. Sacar**
* **3. Visualizar extrato**
## Funcionalidades do Sistema
* **Operação de depósito:**
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
* **Operação de saque:**
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
* **Operação de extrato:**
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx. Exemplo: 1500.45 = R$ 1500.45
## Implementação do Menu Interativo
Para tornar o sistema fácil de usar, um menu interativo foi implementado. Através deste menu, o usuário pode selecionar as operações desejadas (depositar, sacar, visualizar o extrato ou sair) de maneira intuitiva. A interação ocorre em um loop contínuo que só é interrompido quando o usuário escolhe a opção de sair do sistema.
#### Como Usar:
* **Depositar:** Escolha a opção "1" e insira o valor a ser depositado.
* **Sacar:** Escolha a opção "2" e insira o valor a ser sacado.
* **Visualizar Extrato:** Escolha a opção "3" para exibir o extrato da conta.
* **Sair:** Escolha a opção "0" para encerrar o programa.
## Considerações  Finais
A criação deste sistema bancário básico é um passo inicial importante para entender como funcionam as operações bancárias no mundo real e como elas podem ser automatizadas e otimizadas com o uso de tecnologia. O projeto também serve como um ponto de partida para futuros aprimoramentos e expansões, como a adição de múltiplos usuários, segurança avançada, e integração com sistemas externos.


