#listas

alunos = ["pietro", "paul", "davi", "professor Matheus"]

print("Lista Original: ", alunos)

alunos.append("tiago") # adiciona um novo valor a variável do tipo lista

print("-"*83) # Serve para criar um espaço acima

print("Lista após metodo append: ", alunos)

alunos.remove("professor Matheus")

print("-"*83) # Serve para multiplicar a string pelo número multilicado

print("Lista após metodo remove: ", alunos)

print("-"*62)

alunos.sort() # Order Crescente
print("Lista após metodo sort: ", alunos)

print("-"*60)

print(len(alunos)) # Funciona para ler a quantidade de dados dentro da lista ou outros métodos

print("-"*60)

contador = 0

while contador <= 10:
    print(contador)
    contador = contador + 1

print("-"*60)
for alunos in ["pietro", "paul", "davi", "professor Matheus"]:
    print(alunos)

for contador in range(10):

    if contador == 3:

        print("O passo 3 será pulado :P")

        continue


    print("Degrau:", contador)