class Cachorro:
    def _init_(self, nome, raca, comida):
        self.nome = nome
        self.raca = raca
        self.comida = comida
        self.acordado = True
        self.feliz = True

    def _str_(self):
        return f"Nome: {self.nome}, Raça: {self.raca}, Comida: {self.comida}, Acordado: {self.acordado}, Feliz: {self.feliz}"

    def comer(self):
        if self.comida > 0:
            self.comida -= 1
            self.feliz = True
            print(f"{self.nome} comeu e está muito FELIZ!!!. Comida restante: {self.comida}.")
        else:
            print(f"{self.nome} está morrendo de Fome, mas há Comida Acabou")

    def dormir(self):
        self.acordado = False
        print(f"{self.nome} está cansado e foi Dormir.")

    def acordar(self):
        self.acordado = True
        print(f"{self.nome} Acordou, mas está morrendo de Fome!.")

    def brincar(self):
        self.feliz = True
        print(f"{self.nome} Brincou e está muito FELIZ!!!")

    def ignorar(self):
        self.feliz = False
        print(f"{self.nome} foi ignorado e está muito Triste.")

    def latir(self):
        if self.acordado:
            print(f"{self.nome} está Latindo! AU! AU! AU!")
        else:
            print(f"{self.nome} está Dormindo e não pode Latir.")

# Instanciando dois cachorros
cachorro1 = Cachorro("Lazer Dim", "Pincher", 5)
print(cachorro1)
cachorro2 = Cachorro("Don Toliver", "Golden Retriever", 4)
print(cachorro2)

# Interagindo com os cachorros
cachorro1.comer()
cachorro1.latir()
cachorro1.brincar()
cachorro1.dormir()
cachorro1.latir()
cachorro1.acordar()
cachorro1.comer()
