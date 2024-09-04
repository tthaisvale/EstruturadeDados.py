#Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um  método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário  do funcionário.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual):
        if percentual > 0:
            aumento = self.salario * (percentual / 100)
            self.salario += aumento
            return f"Salário aumentado para R${self.salario:.2f}"
        else:
            return "O percentual de aumento deve ser positivo."

funcionario = Funcionario("Ana", 3000.00, "Analista")

resultado = funcionario.aumentar_salario(10)

print(resultado) 

resultado = funcionario.aumentar_salario(-5)

print(resultado)
