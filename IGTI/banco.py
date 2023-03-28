def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

conta_maria = cria_conta(123, "Maria", 1000, 2000)

def deposita(conta, valor):
    conta["saldo"] = conta["saldo"] + valor

def saca(conta, valor):
    conta["saldo"] =conta["saldo"] - valor

def extrato(conta):
    print("Número", conta["numero"], "Saldo", conta["saldo"])

def aumentalimite(conta, valor):
    conta["limite"] = conta["limite"] + valor

extrato(conta_maria)
saca(conta_maria, 145)

#representa acoes do dia-a-dia

class Conta():
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposito(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    def extrato(self):
        print("Número: {} \nSaldo: {} \nLimite: {}".format(self.numero, self.saldo, self.limite))

    def aumentalimite(self, valor):
        self.limite += valor


conta_weslley = Conta(12387654, "weslley", 1000, 250)
conta_weslley.extrato()
conta_weslley.saca(134.87)
conta_weslley.extrato()
conta_weslley.aumentalimite(134)
conta_weslley.extrato()


#herança orientacao objeto

class ContaBase():
    def __init__(self, numero, titular, saldo, limite):
        """Define a nova conta bancaria"""
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposito(self, valor):
        """Acrescenta valores a conta"""
        self.saldo += valor

    def saca(self, valor):
        """Retira valores da conta verificando se existe saldo."""
        novo_saldo = self.saldo - valor
        if novo_saldo < 0:
            print("Saldo de {} insuficiente para sacara {}".format(self.saldo, valor))
        else:
            self.saldo = novo_saldo
            print("Seu saldo atual é de {}. \n=================".format(self.saldo))

    def extrato(self):
        """Apresenta o saldo atual da conta."""
        print("Número: {} - {} \nSaldo: {} \nLimite: {} \n=================".format(self.numero, self.titular, self.saldo, self.limite))

    def aumentalimite(self, valor):
        """Aumenta o limite da conta"""
        self.limite += valor

# novaconta = ContaBase(89654263, "Thaisa Fais", 1500, 250)
# novaconta.extrato()
# novaconta.saca(2000)


class ContaPoupanca(ContaBase):
    def __init__(self, numero, titular, saldo, limite=0, rendimento=0.01):
        super().__init__(numero, titular, saldo, limite)
        self.rendimento = rendimento
    
    def render(self):
        self.saldo += self.saldo * self.rendimento

novacontapoupanca = ContaPoupanca(76540937, "Calebe Fais", 300)
novacontapoupanca.titular
novacontapoupanca.saldo
novacontapoupanca.render()
novacontapoupanca.saldo
novacontapoupanca.extrato()
novacontapoupanca.deposito(200)
novacontapoupanca.extrato()
novacontapoupanca.render()
novacontapoupanca.extrato()

class ContaSalario(ContaBase):
    def __init__(self, numero, titular, saldo, salario, limite=0):
        super().__init__(numero, titular, saldo, limite)
        self.salario = salario
    
    def receber(self):
        self.deposito(self.salario)
    
    def novo_salario(self, novo_salario):
        self.salario = novo_salario

contasalario = ContaSalario(23875402984, "Thaisa Fais", 0, 0, 1600)
contasalario2 = ContaSalario(27384874, "Weslley", 0, 1800)
contasalario.receber()
contasalario.extrato()
contasalario2.extrato?















