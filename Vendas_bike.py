class bikes:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("\nBI BI BIIIII!")

    def parar(self):
        print("\nConsegui para a bike!")
    
    def correr(self):
        print("\nVRUUUUUuuum!!\n")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        

b1 = bikes("Rosa pink", "MTB", 2024, 1500.99)
b1.buzinar()
b1.parar()
b1.correr()
print(b1)