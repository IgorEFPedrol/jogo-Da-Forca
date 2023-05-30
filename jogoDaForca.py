import random

palavras = ["primeiro", "carlos", "jogar", "pizza", "hamburguer", "riacho", "sol", "andar", "correr", "ultimo"]

randomPalavra = random.choice(palavras)

print(randomPalavra)

num = int(input('Insira um número: '))

if num %2 == 0:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar") 

for num in range(len(palavras)):
    print(palavras[num])