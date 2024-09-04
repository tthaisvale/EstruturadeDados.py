#Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método  chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f'Título: {self.titulo}\nAutor: {self.autor}'

meu_livro = Livro('O Pequeno Príncipe', 'Antoine de Saint-Exupéry')
info = meu_livro.detalhes()
print(info)
