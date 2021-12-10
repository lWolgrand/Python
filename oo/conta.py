import teste
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("constuindo objeto ...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self, valor):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def get_saldo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular

    @property
    def get_limite(self):
        return self.__limite

    @limite.setter
    def set_limite(self, limite):
        self.__limite = limite
        