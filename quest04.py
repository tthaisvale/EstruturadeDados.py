#Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente  métodos “depositar” e “sacar” para manipular o saldo.

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f'Depósito de R${valor:.2f} realizado com sucesso!'
        else:
            return 'O valor do depósito deve ser positivo.'

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                return f'Saque de R${valor:.2f} realizado com sucesso!'
            else:
                return 'Saldo insuficiente para realizar o saque.'
        else:
            return 'O valor do saque deve ser positivo.'

    def consultar_saldo(self):
        return f'O saldo atual é: R${self.saldo:.2f}'


conta = ContaBancaria("João Silva", 1000.0)
print('A {} teve a seguinte movimentação nos últimos 30 dias:'.format(conta))

print(conta.depositar(200.0))

print(conta.sacar(150.0))

print(conta.sacar(2000.0))

print(conta.consultar_saldo())
