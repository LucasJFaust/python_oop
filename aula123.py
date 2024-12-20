# Escopo da classe e de métodos da clase

class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


# print(Animal.nome)

leao = Animal('Leão')
print(leao.nome)
print(leao.comendo('carne'))
print(leao.executar('maçã'))

