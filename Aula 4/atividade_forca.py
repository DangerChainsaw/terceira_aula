#Requisitos Funcionais

#Mostrar o número de tentativas restantes
#Mostrar as letras corretas
#Permitir vencer
#Permitir perder
#Apenas aceitar uma letra por tentativa
#Impedir que a mesma letra seja digitada novamente

import random

palavra_secreta = random.choice(["pietro","davi","paul"])
Letras_certas = []
Letras_erradas = []
tentativas = 6

while tentativas > 0: 
    palavra_formada = ""

    for letra in palavra_secreta: 
        if letra in Letras_certas: 
            palavra_formada += letra
        
        else:
            palavra_formada += "_"

    print("\nPalavra:", palavra_formada)

    if len(Letras_erradas) > 0:
        print("\nPalavra:", Letras_erradas)

    else:
        print("Letras erradas: nenhuma")

    print("\nTentativas restantes:", tentativas)

    if palavra_formada == palavra_secreta:
        print("Palavra formada corretamente")
        break

    chute = input("Digite uma letra: ")

    chute = chute.lower()

    if len(chute) != 1:
        print("Digite apenas uma letra válida")
        continue

    if chute in Letras_certas or chute in Letras_erradas:
            print("Você já digitou essa letra:")
            continue

    if chute in palavra_secreta:
        Letras_certas.append(chute)
        print("letra correta")
        continue

    else:
        Letras_erradas.append(chute)
        print("letra incorreta")
        tentativas -= 1

    if tentativas == 0:
        print("\nDerrota. A palavra era:", palavra_secreta)

    