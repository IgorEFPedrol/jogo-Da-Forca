import random

palavras = ["primeiro", "carlos", "jogar", "pizza", "hamburguer", "riacho", "sol", "andar", "correr", "ultimo"]
vidas = 6
display = []

randomPalavra = random.choice(palavras)

for n in range(len(randomPalavra)):
    display.append("_")
print(display)

while vidas > 0:
    chute = input("Digite uma letra: ")
    
    cont = 0
    acertou = False
    for letra in randomPalavra:
        if chute == letra:
            display[cont] = chute
            acertou = True    
        cont += 1
    if not acertou:
        vidas -= 1
    print(display)        
    print(vidas)
    if '_' not in display:
        print("Você ganhou!!")
        break

print("Você perdeu!!!\nA palavra era " + randomPalavra)