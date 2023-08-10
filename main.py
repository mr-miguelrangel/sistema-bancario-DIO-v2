import os

# A função recebe uma lista para acrescentar um novo elemento do tipo dicionário a ela
def cria_usuario (usuarios):
  novo_usuario = {}
  
  while (True):
    novo_usuario['cpf'] = input ("Digite seu CPF (somente números): ")

    ja_cadastrado = False
    for usuario in usuarios:
      if usuario['cpf'] == novo_usuario['cpf']:
        ja_cadastrado = True
        break

    if ja_cadastrado:
      print ("Este CPF já está cadastrado.")
    elif not(novo_usuario['cpf'].isdigit()):
      print ("Número inválido. Digite somente número.")
    else:
      break

  novo_usuario['nome'] = input ("Digite seu nome: ")
  novo_usuario['nascimento'] = input ("Data de nascimento (dd/mm/aaaa): ")
  logradouro = input ("Rua: ")
  numero = input ("Número: ")
  bairro = input ("Bairro: ")
  cidade = input ("Cidade: ")
  estado = input ("Estado: ")
  novo_usuario['endereco'] = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"

  return novo_usuario

# A função recebe uma lista para acrescentar um novo elemento do tipo dicionário a ela
def cria_conta (contas, usuarios):
  nova_conta = {}
  nova_conta['agencia'] = '0001'
  nova_conta['numero'] = len(contas) + 1
  while (True):
    nova_conta['usuario'] = input ("CPF do usuário")
    usuario_cadastrado = False

    for usuario in usuarios:
      if usuario['cpf'] == nova_conta['usuario']:
        usuario_cadastrado = True
        break

    if usuario_cadastrado:
      return nova_conta
    else:
      print ("Este CPF não está cadastrado.")

# A função recebe um float e uma string para devolve-los atualizados 
def deposito (saldo, extrato):
  deposito = float (input ("Digite o valor a ser depositado: "))
    
  if (deposito > 0): 
    saldo += deposito
    extrato += f"+ R$ {deposito:.2f}\n"
    os.system('clear') or None
    print (f"Depósito de R$ {deposito:.2f} realizado com sucesso!")   
      
  else:
    print ("Valor inválido!")

  return saldo, extrato    

# A função recebe saldo do tipo float e extrato do tipo string para devolve-los atualizados 
# usando os inteiros conta_saque, QUANTIDADE_SAQUES e LIMITE_SAQUE para validar a operação
def saque (*, saldo, conta_saque, QUANTIDADE_SAQUES, LIMITE_SAQUE, extrato):
  saque = float (input ("Digite o valor a ser sacado: "))

  saldo_insuficiente = (saque > saldo)
  quantidade_excedida = (conta_saque == QUANTIDADE_SAQUES)
  limite_excedido = (saque > LIMITE_SAQUE)

  if (saque < 0):
    print ("Valor inválido")
  
  elif (quantidade_excedida):
    print (f"Operação falhou! Você já sacou {QUANTIDADE_SAQUES} vezes hoje. Tente novamente amanhã")

  elif (limite_excedido):
    print (f"Operação falhou! Valor máximo para saque: R$ {LIMITE_SAQUE:.2f}")

  elif (saldo_insuficiente):
    print ("Operação falhou! Seu saldo é insuficiente.")

  else:
    saldo -= saque
    extrato += f"- R$ {saque:.2f}\n"
    conta_saque += 1
    os.system('clear') or None
    print (f"Saque de R$ {saque:.2f} realizado com sucesso!") 

  return saldo, extrato, conta_saque

# A função recebe saldo do tipo float e extrato do tipo string para imprimir os extrato do
# cliente
def exibe_extrato (saldo, /, *, extrato):
  print(extrato + f"\nSaldo: R$ {saldo:.2f}")  
  print(19 * "=")

menu = '''
DIGITAL INNOVATION BANK

1 - Depositar
2 - Sacar
3 - Extrato
4 - Registrar usuário
5 - Criar conta
6 - Sair

Escolha uma das opções: 
'''

saldo = 0.00
extrato = "======EXTRATO======\n"
LIMITE_SAQUE = 500
QUANTIDADE_SAQUES = 3
conta_saque = 0
usuarios = []
contas = []

while (True):
  opcao = int(input(menu))

  if (opcao == 1):
    os.system('clear') or None
    saldo, extrato = deposito (saldo, extrato)
      
  elif (opcao == 2):
    os.system('clear') or None
    saldo, extrato, conta_saque = saque (saldo= saldo, conta_saque= conta_saque, QUANTIDADE_SAQUES= QUANTIDADE_SAQUES,
                           LIMITE_SAQUE= LIMITE_SAQUE, extrato= extrato)
      
  elif (opcao == 3):
    os.system('clear') or None
    exibe_extrato (saldo, extrato= extrato)

  elif (opcao == 4):
    os.system('clear') or None
    usuarios.append(cria_usuario(usuarios))

  elif (opcao == 5):
    os.system('clear') or None
    contas.append(cria_conta(contas, usuarios))
    
  elif (opcao == 6):
    os.system('clear') or None
    print ("Operação encerrada.\nVolte sempre!")
    break
    
  else:
    os.system('clear') or None
    print ("Opção inválida! Tente novamente.")