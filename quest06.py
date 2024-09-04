#Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um  método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

produto = Produto("Calça", 37.99, 1)

total = produto.calcular_total()

print(f"O valor total do produto é: R${total:.2f}")
