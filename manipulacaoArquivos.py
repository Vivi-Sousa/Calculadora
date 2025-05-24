# Criando o arquivo para escrever as três notas nele    
arquivo = open("minhas_notas.txt", "w")
arquivo.write("Matematica: 10\n")
arquivo.write("Portugues: 9\n")
arquivo.write("Historia: 8\n")
arquivo.close()

#adicionando mais duas notas no arquivo no final dele sem apagar o que já existe
arquivo = open("minhas_notas.txt", "a")
arquivo.write("Frase nova adicionada no final - Geografia: 7\n")
arquivo.write("Segunda frase nova adicionada no final - Ciencias: 6\n")
arquivo.close()

#Agora vai fazer a leitura do aqrquivo e impirimir usando WITH
with open ("minhas_notas.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
