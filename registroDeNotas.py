
'''
Tentativa de código Vitoria Oliveira Sousa - Vou aprimorar o código

while True:
    notas = input("Digite a sua nota ou digite 'FIM' para parar o looping: ")
    listaNotas=[notas]

    print(listaNotas)

    if notas == "FIM":
        break
'''
#codigo corrigido pelo professor Edson
def registroDeNotas():

    listaNotas = []

    while True:
        entrada = input("Digite a nota do aluno ou digite FIM para sair: ")
        if entrada == "Fim":
            print("Encerrando o seu registro de notas")
            break
        else:
            try:
                nota = float(entrada)
                if 0 <= nota <= 10:
                        listaNotas.append(nota)
                else:
                    print("Nota inválida. Digite uma nota de 0 a 10. \n")
            except ValueError:
                print("Nota inválida. Digite uma nota de 0 a 10. \n")

    calcularMedia(listaNotas)          
        
def calcularMedia(listaNotas):      
    if listaNotas:

        media = sum(listaNotas)/len(listaNotas)

        print("A média do aluno é:" + str(media))
    else:
        print("Nenhuma nota válida foi inserida")

registroDeNotas()




