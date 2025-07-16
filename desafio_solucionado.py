class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class Conta:
    def __init__(self, cliente, numero, agencia="0001"):
        self.cliente = cliente
        self.numero = numero
        self.agencia = agencia
        self.saldo = 0
        self.limite = 500
        self.extrato_str = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato_str += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            raise ValueError("Operação falhou! O valor informado é inválido.")

    def saque(self, valor):
        if valor > self.saldo:
            raise ValueError("Operação falhou! Você não tem saldo suficiente.")
        if valor > self.limite:
            raise ValueError("Operação falhou! O valor do saque excede o limite.")
        if self.numero_saques >= self.LIMITE_SAQUES:
            raise ValueError("Operação falhou! Número máximo de saques excedido.")

        self.saldo -= valor
        self.extrato_str += f"Saque: R$ {valor:.2f}\n"
        self.numero_saques += 1
        print("Saque realizado com sucesso!")

    def extrato(self):
        return self.extrato_str if self.extrato_str else "Não foram realizadas movimentações."

clientes = []
contas = []
numero_conta = 1

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Cliente
[l] Listar Clientes
[q] Sair
=> """

def cadastrar_cliente():
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento (DD/MM/YYYY): ")
    cpf = input("CPF (somente números): ")
    
    # Validação: Verificar se já existe um cliente com o mesmo CPF
    for cliente in clientes:
        if cliente.cpf == cpf:
            print("CPF já cadastrado. Tente novamente.")
            return
    
    endereco = input("Endereço: ")
    cliente = Cliente(nome, data_nascimento, cpf, endereco)
    clientes.append(cliente)
    
    global numero_conta
    conta = Conta(cliente, numero_conta)
    contas.append(conta)
    numero_conta += 1
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        print("\n===== CLIENTES CADASTRADOS =====")
        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. Nome: {cliente.nome} | CPF: {cliente.cpf} | Nascimento: {cliente.data_nascimento} | Endereço: {cliente.endereco}")
        print("================================")

while True:
    opcao = input(menu)

    try:
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            if contas:
                contas[0].deposito(valor)
            else:
                print("Nenhuma conta cadastrada. Cadastre um cliente primeiro.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            if contas:
                contas[0].saque(valor)
            else:
                print("Nenhuma conta cadastrada. Cadastre um cliente primeiro.")

        elif opcao == "e":
            if contas:
                extrato = contas[0].extrato()
                print("\n================ EXTRATO ================")
                print(extrato)
                print(f"Saldo: R$ {contas[0].saldo:.2f}")
                print("==========================================")
            else:
                print("Nenhuma conta cadastrada. Cadastre um cliente primeiro.")

        elif opcao == "c":
            cadastrar_cliente()

        elif opcao == "l":
            listar_clientes()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

    except ValueError as e:
        print(e)