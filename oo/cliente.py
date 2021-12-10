
class Cliente:

    def __init__(self, nome):
        self.nome = nome

        @property
        def nome(self):
            print("chamando @property nome()")
            return self.__nome.title()

        @nome.property
        def nome(self, nome):
            print("Chamando setter nome()")
            self.__nome = nome