'''
variavel = 'senha1'
print(len(variavel))

print(variavel.isdigit())
'''



def verificarSenha(senha):
    if len(senha) < 8:
        print("A senha inserida tem poucos caracteres")

    if not any(char.isdigit() for char in senha):
            print("Senha deve conter números")
            return False
    elif not any(char.isalpha() for char in senha):
        return True

while True:
    senha = input("Digite a sua senha desejada ou escreva sair: ")

    if senha == "sair":
        print("Saindo...")
        break
    
    if verificarSenha(senha):
        print("Senha válida")
        

         
