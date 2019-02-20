class ContoCorrente:
    def __init__(self, nome, conto, importo):
        self.nome = nome
        self.conto = conto
        self.__saldo = importo


    def preleva(self, importo):
        self.__saldo -= importo

    def deposita(self, importo):
        self.__saldo += importo

    def descrizione(self):
        print(self.nome, self.conto, self.__saldo)

    @property
    def saldo(self):
        print("Sono dentro il getter")
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        print("Sono dentro il setter")
        self.preleva(self.__saldo)
        self.deposita(importo)


c1 = ContoCorrente("Alessandra", "10", 2000)
c1.descrizione()
c1.saldo = 10000
print(c1.saldo)

# print(c1.__saldo)
# print(c1.saldo)