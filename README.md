# Sistema bancário em Python atualizado

## Descrição
Projeto desenvolvido no bootcamp de Ciência de Dados da DIO. É um sistema bancário simples, que realiza operações de depósito, saque, visualização de extrato, cadastro de usuário e criação de conta. [Aqui está a primeira versão](https://github.com/mr-miguelrangel/sistema-bancario-DIO)

## Funções

**Depósito:** o usuário digita o valor a ser depositado, o sistema verifica se o valor é positivo e,portanto, válido para depois incrementar no saldo. Ao fim da operação o sistema acrescenta uma linha na string "extrato" com as informações do depósito.

**Saque:** o usuário digita o valor a ser sacado em seguida o sistema faz as seguintes verificações:

    1) Valor digitado é válido?
    2) O cliente já fez a quantidade máxima de saques permitida por dia?
    3) O valor digitado é maior que o máximo permitido?
    4) O cliente tem saldo para sacar o valor digitado?

Se o valor digitado passar em todos os testes, o valor é decrementado do saldo e um contador de saques é incrementado por 1. Ao fim da operação o sistema acrescenta uma linha na string "extrato" com as informações do saque.

**Extrato:** todas as operações realizadas e o saldo atual são mostradas na tela.

**Criar usuário:** essa função recebe uma lista de usuários a fim de acrescentar um novo elemento a ela. Cada elemento é um dicionário com as chaves:
    
    - Nome;
    - Data de nascimento;
    - CPF;
    - Endereço.

O usuário digita seu CPF e as seguintes verificações são feitas:

    1) O CPF digitado é composto somente por números?
    2) O CPF digitado já foi cadastrado no sistema?

Se o valor digitado passar nos testes o usuário digita os demais dados e é integrado à lista de usuários do sistema.

**Criar conta:** essa função recebe uma lista de contas a fim de acrescentar um novo elemento a ela. Cada elemento é um dicionário com as chaves:

    - Agência;
    - Número da conta;
    - CPF do usuário.

O usuário digita seu CPF, que será procurado no banco de dados caso não esteja uma mensagem de erro será impressa na tela. O número da agência é fixo, e o número das contas é sequencial, começando em 1. Um usuário pode ter mais de uma conta.