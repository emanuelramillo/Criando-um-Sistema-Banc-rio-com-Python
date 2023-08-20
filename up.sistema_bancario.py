def menu():
     menu = """======== MENU =========
     BEM-VINDO, usuário!
     digite a opção que
      deseja realizar.
      [1] Depositar
      [2] Sacar
      [3] Extrato
      [4] Novo Usuario
      [5] Nova Conta
      [6] Listar Contas
      [7] Sair
     ==> """
     return input(menu)

def depositar(saldo,extrato,/):
    while True:
        valor = float(input("\nPorfavor, informe o valor que deseja depositar: "))
        if valor > 0 :
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("\nDeposito realizado com sucesso!")
            break        
        else:
            continuar = str(input("\nValor inválido. Deseja tentar novamente? \nDigite 'S' caso sim ou qualquer outra tecla para sair: "))
            if continuar.upper() == "S":
                continue
            else:
                return   
    return saldo, extrato
    
def sacar(*,saldo, extrato, limite, numero_de_saques, LIMITE_DE_SAQUES):
     while True:
             
         valor = float(input("\nPor favor, informe o valor que deseja sacar: "))
         exedeu_saldo = valor > saldo
         exedeu_limite = valor > limite
         exedeu_saque = numero_de_saques >= LIMITE_DE_SAQUES

         if exedeu_saldo:
             (print(f"\nVocê não possui essa quantia em sua conta, seu saldo atual é de R$ {saldo}! "))
             continuar = str(input("Digite s se deseja tentar novamente ou qualquer \noutra tecla para voltar ao menu: "))
             if continuar.upper() == "S":
                     valor
             else:
                 break
                 
         elif exedeu_limite:
             print("\nVocê não pode sacar valores maiores que R$500,00 de uma única vez, por favo, insira um valor válido.")
             continuar = str(input("Digite 'S' se deseja tentar novamente ou qualquer \noutra tecla para voltar ao menu: "))
             if continuar.upper() == "S":
                 valor
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
         return saldo, extrato

def extrato_bancario(saldo,/,*,extrato):
     print("\n====== EXTRATO ======")
     print("Ainda não foram relizada movimentações!" if not extrato else extrato)
     print(f"Saldo: R$ {saldo:.2f}\n")
     print("#######################")

def criar_usuario(usuarios):
     cpf = input("Informe o CPF (somente números): ")
     usuario = filtrar_usuario(cpf,usuarios)
     
     if usuario:
        print("\n Já existe usuário com esse CPF!")
     
        return
     nome = input("Informe o nome completo: ")
     data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
     endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
     
     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
     print("\nUsuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    novo = input("Usuario não encontrado, digite a tecla 'n' se deseja criar um novo usuario: ")
    if novo.upper() == "N":
        criar_usuario(usuarios)
    else:
        print("\nVocê não pode criar sua conta se não possuir um usuario usuario!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def start():
    
     saldo = 0
     limite = 500
     extrato = ""
     numero_de_saques = 0
     LIMITE_DE_SAQUES = 3
     usuarios = []
     contas = []
     AGENCIA = "0001"
     while True:
         opção = int(menu())
         
         if opção == 1:
             
             saldo, extrato = depositar(saldo,extrato)
         elif opção == 2:
             sacar(saldo=saldo,extrato=extrato,limite=limite,numero_de_saques=numero_de_saques, LIMITE_DE_SAQUES=LIMITE_DE_SAQUES)
         elif opção == 3:
             extrato_bancario(saldo, extrato=extrato)
         elif opção == 4:
             criar_usuario(usuarios)
         elif opção == 5:
             numero_conta = len(contas) + 1
             conta = criar_conta(AGENCIA, numero_conta, usuarios)
             if conta:
                 contas.append(conta)
         elif opção == 6:
             listar_contas(contas)
         elif opção == 7:
             break
         else:
             print("Insira uma opção válida!")

     
start()