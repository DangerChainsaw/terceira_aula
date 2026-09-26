#Requisitos Funcionais

#Mostrar o número de tentativas restantes
#Mostrar as letras corretas
#Permitir vencer
#Permitir perder
#Apenas aceitar uma letra por tentativa
#Impedir que a mesma letra seja digitada novamente

palavra_secreta = "python"
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