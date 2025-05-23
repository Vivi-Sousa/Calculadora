'''

def soma (a, b):

    resultado = (a + b)
    return resultado

valor1= int(input("Digite o primeiro valor: "))
valor2= int(input("Digite o segundo valor: "))

soma(valor1, valor2)

'''

def calcularGorjeta ():
    valorConta = float(input("Insira o valor da sua conta: "))
    porcentagemGorjeta = float(input("Insira o  valor da taxa da gorjeta: "))

    resultado = valorConta * (porcentagemGorjeta/100)
    print(resultado)

calcularGorjeta()



