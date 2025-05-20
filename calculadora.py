def calculadora():

    try:
        primeiroNumero = float(input("Digite o primeiro valor: "))
        segundoNumero = float(input("Digite o segundo valor: "))
        operador = input("Digite a operação desejada: + para adição, - para subtração , * para multiplicação e / para divisão: ")

    
        if operador == "+":
            print("A soma do números é: ", primeiroNumero + segundoNumero)

        elif operador == "-":
            print("A subtração entre os dois números é: ", primeiroNumero - segundoNumero)

        elif operador == "*":
            print("A multiplicação entre os dois números é: ", primeiroNumero * segundoNumero)

        elif operador == "/":
            if segundoNumero == 0:
                print("Erro: Divisão por zero, digite um número maior que zero. ")
                return calculadora()
            print("A divisão entre os dois números é: ", primeiroNumero / segundoNumero)

        else:
            print("Digite uma operação válida! As operações válidas são: +, -, * e /: ")

    except ValueError:
        print("Erro: Entrada inválidaDigite um número válido! .\n")
        return calculadora()
    
calculadora()