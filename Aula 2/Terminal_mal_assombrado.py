print("═" * 50)
print("   🛸 PLAY LAB — MISSÃO: TERMINAL MAL-ASSOMBRADO")
print("═" * 50)
print()
print("Tripulante, um fantasma está assombrando este terminal.")
print("Ele deixou 3 enigmas escondidos no sistema.")
print("Sua missão: decifrar as pistas. O sistema vai calcular")
print("automaticamente se sua resposta bate — mostrando a")
print("MARGEM DE ERRO, sem revelar se você acertou ou errou.")
print()
input("Pressione ENTER para iniciar o protocolo de acesso...")
print()


print("╔════════════════════════════════════╗")
print("║       TERMINAL FANTASMA            ║")
print("║      PROTOCOLO: COFRE_00X          ║")
print("╚════════════════════════════════════╝")
print()


nome = input("Insire o seu usuário: ")
print()
print(nome + ", resolva 3 enigmas antes do cofre abrir")
print()

print("ENIGMA 1: 'Sou o dobro de 21, menos a idade que você tinha aos 7 anos multiplicada por 3.' ")
resposta = int(input("Digite sua resposta: ")) #Recebe um input e converte em int(número inteiro) e guarda na variável resposta
certa1 = 42 - 21
erro1 = resposta - certa1
respostaErrada = bool(erro1) #0 igual a falso e qualquer coisa sem ser 0 ou ""(aspas vazia e sem espaço) é verdadeiro

print("ENIGMA 2: 'Qual a raíz quadrada de 2, com 3 casas decimais? (ex: 1.234)' ")
resposta2 = float(input("Digite sua resposta: ")) #Recebe um input e converte em float(número quebrado) e guarda na variável resposta
certa2 = 1.414
erro2 = resposta2 - certa2
respostaErrada2 = bool(erro2) #0 igual a falso e qualquer coisa sem ser 0 ou ""(aspas vazia e sem espaço) é verdadeiro

print("ENIGMA 3: 'Sou metade da temperatura de eblição da água em celsius, mais a quantidade de patas de uma aranha dividida por 2.' ")
resposta3 = float(input("Digite sua resposta: ")) #Recebe um input e converte em float(número quebrado) e guarda na variável resposta
certa3 = 50.0 + 4
erro3 = resposta3 - certa3
respostaErrada3 = bool(erro3) #0 igual a falso e qualquer coisa sem ser 0 ou ""(aspas vazia e sem espaço) é verdadeiro

print()
print("---ANALISANDO RESPOSTAS---")
print()

pontuacao = 100 -(erro1 * erro1)- (erro2 * erro2)- (erro3 * erro3 * 100)
pontuacao = int(pontuacao)

print("Enigma 1 - Desvio de Resposta" + str(erro1) + "| Erro Detectado:" + str(respostaErrada))
print("Enigma 2 - Desvio de Resposta" + str(erro2) + "| Erro Detectado:" + str(respostaErrada2))
print("Enigma 3 - Desvio de Resposta" + str(erro3) + "| Erro Detectado:" + str(respostaErrada3))
print()

print("╔═══════════════════════════════════════════════╗")
print("║  PONTUAÇÃO FINAL" + str(pontuacao) + " / 100  ║")
print("╚═══════════════════════════════════════════════╝")
print()