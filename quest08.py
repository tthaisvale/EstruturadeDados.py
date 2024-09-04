#Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado  “calcular_media” que retorna a média das notas do aluno.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

aluno = Aluno("Ana", [6.5, 9.0, 4.5, 10.0])

media = aluno.calcular_media()

print(f"A média das notas da aluna {aluno.nome} é: {media:.2f}")
