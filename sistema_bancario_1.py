menu = """======== MENU =========

BEM-VINDO, usuário!

digite a opção que
 deseja realizar.

 [1] Depositar
 [2] Sacar
 [3] Extrato
 [4] Sair
"""


saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
     opção = int(input(menu))
     
     if opção == 1:
         while True:
             valor = float(input("Porfavor, informe o valor que deseja depositar: "))
         
             if valor > 0 :
                 saldo += valor
                 extrato += f"Deposito: R$ {valor:.2f}\n"
                 print("Deposito realizado com sucesso!")
                 break
             
             else:
                 continuar = str(input("Valor inválido. Deseja tentar novamente? \nDigite S caso sim ou qualquer outra teclapara sair: "))
                 if continuar.upper() == "S":
                     opção
                 else:
                     break
        
     elif opção == 2:
         while True:
             
             valor = float(input("Por favor, informe o valor que deseja sacar: "))
             exedeu_saldo = valor > saldo
             exedeu_limite = valor > limite
             exedeu_saque = numero_de_saques >= LIMITE_DE_SAQUES

             if exedeu_saldo:
                 (print(f"Você não possui essa quantia em sua conta, seu saldo atual é de R$ {saldo}! "))
                 continuar = str(input("Digite s se deseja tentar novamente ou qualquer \noutra tecla para voltar ao menu: "))
                 if continuar.upper() == "S":
                     opção
                 else:
                     break
                 
             elif exedeu_limite:
                 print("Você não pode sacar valores maiores que R$500,00 de uma única vez, por favo, insira um valor válido.")
                 continuar = str(input("Digite s se deseja tentar novamente ou qualquer \noutra tecla para voltar ao menu: "))
                 if continuar.upper() == "S":
                     opção
                 else:
                     break
             elif exedeu_saque :
                 print("Você já realizou a quantidade maxima de saque no dia, por favor, volte outro dia!")
                 break
             elif valor > 0:
                 saldo -= valor
                 extrato += f"Saque: R${valor:.2f}\n"
                 numero_de_saques += 1
                 print("Saque relizado com sucesso!")
                 break
             else:
                 print("Insira um valor válido!")
                 break

     elif opção == 3:
         print("\n====== EXTRATO ======")
         print("Ainda não foram relizada movimentações!" if not extrato else extrato)
         print(f"Saldo: R$ {saldo:.2f}\n")
         print("#######################")
     elif opção == 4:
         break
     else:
         print("Operação inválida, tente novamente!")

