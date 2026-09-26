#Operador maior ou menor e igual ou maior e maior ou igual

# > operador maior
# < operador menor
# >= operador maior ou igual
# <= operador menor ou igual
#operadores sempre retornarão verdadeiro ou falso para a pergunta.

print(10 > 10) #False, 10 não é maior que 10
print(10 >= 10) #True, 10 é maior ou igual a 10
print(1.1 > 1) #True, 1.1 é maior que 1

print(10 < 10) #False, 10 não é maior que 10
print(10 <= 10) #True, 10 é menor ou igual a 10
print(1.1 <= 1) #False, 1.1 não é maior ou igual a 1


#operador de comparação ==

#o operador == serve para comparação do primeiro VALOR com o segundo VALOR diferente do = que serve para atribuição.

print(10.0 == 10) #True
print("nome@gmail.com" == "nome@cna.com") #False
print(9.1 == 9) #False

#Operador de Diferença !=

#Ele é utilizado para verificar se o primeiro valor é diferente do segundo valor, retornando sempre Ture ou False.

print(10.0 != 10) #True
print("professor" != "professor") #False
print(09.1 != 9) #False


#Estruturas Condicionais

# if que significa SE
# else que significa SE NAO
# else if que significa SE NAO SE

if True:
    print("teste") #Como retornou VERDADEIRO o bloco de código executa


if False:
    print("teste") #Como retornou FALSO o bloco de código não executa

#Exemplo 1

teste = True

if teste:
    print("É verdadeiro")

teste = False

if teste:
    print("É verdadeiro")


#Exemplo 2

teste = input("Você já brincou com fogo?") # Input sempre retorna uma string

if teste == "sim":
    print("Então já se queimou :(")

else:
    print("Então não brinque, se não vai se queimar.")

#Exemplo 3 IF aninhado quando a primeira condição do primeiro IF precisa ser VERDADEIRO para que os demais IFs dentro dele sejam executados

tem_documento = True
pagou_ingresso = True
idade = 16

if idade >= 18:
    print("É maior de idade.")

    if tem_documento:
        print("Apresentou um Documento.")

        if pagou_ingresso:
            print("Entrada permitida!")



print()
print("Exemplo if independentes")
print()

#IF INDEPENDENTES, quando um if não depende do outros ser verdadeiro para ser executado


if idade >= 18:
    print("É maior de idade.")

if tem_documento:
    print("Apresentou um Documento.")

if pagou_ingresso:
    print("Entrada permitida!")

#Estrutura condicional ELIF

teste = input("Você já brincou com fogo?") # Input sempre retorna uma string

if teste == "sim":
    print("Então já se queimou :(")

elif teste == "talvez":
    print("Então não brinque, se não vai se queimar.")

else:
    print("Então não brinque, se não vai se queimar.")


#Operadores lógicos not, or, and

#not = not
#or = || ou |
#and = && ou &


estudante = True
print(not estudante)          		#Não é estudante? Não (False)

proplayer = True
print(not proplayer)         		 #Não é pro player? Não (False)

maior_de_idade = False
print(not maior_de_idade)     		#Não é maior de idade? Sim (True)

goku_venceria_madoka = False
print(not goku_venceria_madoka)  	#Goku não venceria a Madoka? Sim (True)

#Operador OR

True or False		# -> True

True or True		# -> True

False or False		# -> False

10 >= 10 or 1 > 2	# -> True, a primeira condição é verdadeira

10 < 10 or 1 > 2	# -> False, ambas condições são falsas

#Operador AND

True and False	# -> False

True and True		# -> True

False and False	# -> False

10 >= 10 and 1>2	# -> False, a segunda condição é falsa

10 < 11 and 1 < 2	# -> True, ambas condições são verdadeiras

#Exemplo 4 - Atividade Prática

coral = True

print("Treinamento Iniciado!")

Resposta = input("A Cobra registrada é uma Coral Verdadeira ? (s/n):")

if coral == True and Resposta == "s" or Resposta == "S":
    print("Identificação Correta!")

else:
    print("Identificação incorreta")



coral = False

print("Treinamento Iniciado!")

Resposta = input("A Cobra registrada é uma Coral Verdadeira ? (s/n):")

if coral == False and Resposta == "n" or Resposta == "N":
    print("Identificação Incorreta")

else:
    print("Identificação Correta!")