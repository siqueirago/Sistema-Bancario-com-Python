# Atualização da Sistema bancário 
Para atualizar o sistema bancário com uma abordagem mais orientada a objetos, criamos classes representando clientes, contas, histórico de transações e tipos de transações como saque e depósito. A ideia é organizar o código de maneira que cada classe tenha responsabilidades bem definidas, facilitando a manutenção e a expansão do sistema.
## Explicação do Código Atualizado
* **Cliente e PessoaFisica:** A classe Cliente é a classe base para representar um cliente. PessoaFisica é uma subclasse de Cliente que adiciona um atributo específico para pessoa física, como a data de nascimento.

* **Conta e ContaCorrente:** A classe Conta é a classe base para diferentes tipos de contas bancárias. A classe ContaCorrente herda de Conta e adiciona funcionalidade específica para uma conta corrente, como limites de saque.

* **Historico:** A classe Historico armazena as transações da conta, como saques e depósitos.

* **Transacao, Saque, Deposito:** A classe Transacao é uma classe abstrata (usando ABC) que define um método abstrato registrar que deve ser implementado por todas as subclasses, como Saque e Deposito.

* **Funções do Sistema Bancário:** Funções como criar_cliente, criar_conta, listar_contas, depositar, sacar e exibir_extrato são usadas para realizar operações no sistema bancário.

* **Menu Principal:** O menu principal é um loop while que exibe opções para o usuário interagir com o sistema bancário.








