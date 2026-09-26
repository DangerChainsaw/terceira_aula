valor = 10 #Variável inteira que guarda números inteiros

nome = "Pietro" #Variável do tipo string guarda palavras

Idade_escrita = "Dezesseis" #Variável do tipo string guarda palavras

print(valor) #Print imprimindo o conteúdo da vraiável "valor"
print(nome) #Print imprimindo o conteúdo da vraiável "nome"
print(Idade_escrita) #Print imprimindo o conteúdo da vraiável "Idade_escrita"

Idade_escrita = 32 #Variável "Idade_escrita" sendo alterada

print(Idade_escrita)

nome = input("Digite seu nome:") #input serve para receber algo escrito pelo usuário

print("Prazer,", nome, "seja bem vindo") #A vírgula serve para introduzir uma variável no texto do print

numero1 = 10
numero2 = 15

numero3 = 0
numero4 = 0

resposta = 0

resposta2 = 0

numero1 = input("Digite um número:") #O input recebe um texto do tipo string do usuário

numero2 = input("Digite outro número:") #O input recebe um texto do tipo string do usuário

numero3 = input("Digite um número quebrado:") #Recebe um texto do tipo string de um número quebrado (.)

numero4 = input("Digite outro número quebrado:") #Recebe um texto do tipo string de um número quebrado (.)

resposta = int(numero1) + int(numero2)

resposta2 = float(numero3) + float(numero4)

print("resultado inteiro:", resposta)

print("resultado quebrado:", resposta2)