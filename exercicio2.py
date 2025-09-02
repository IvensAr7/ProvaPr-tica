import random
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def roleta_animacao(opcoes, resultado):
    for i in range(15):
        escolha = random.choice(opcoes)
        clear()
        print("Girando a roleta...\n")
        print(f"[ {escolha} ]")
        time.sleep(0.1 + i*0.03)
    clear()
    print("A roleta parou!\n")
    print(f"*** [ {resultado} ] ***\n")

def main():
    opcoes = [str(i) for i in range(0, 37)] + ['00']
    print("Bem-vindo ao Jogo de Roleta!")
    print("Opções: 0-36 e 00")
    aposta = input("Em qual número você aposta? ")

    if aposta not in opcoes:
        print("Aposta inválida!")
        return

    resultado = random.choice(opcoes)
    roleta_animacao(opcoes, resultado)

    if aposta == resultado:
        print("Parabéns! Você ganhou!")
    else:
        print(f"Você perdeu! O número sorteado foi {resultado}.")

if __name__ == "__main__":
    main()