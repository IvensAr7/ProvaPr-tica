from time import sleep
from random import randint

def init():
    print("Bem-vindo ao Jogo de Roleta!")
    print("""As regras são simples:
          1. Você começa com 200 pontos
          2. Pode apostar quantas moedas quiser em uma das opções a seguir:
            A - Números iguais
                - Se os três números forem iguais, você ganha 50x sua aposta!
                - Se dois números forem iguais, você ganha 20x sua aposta!
            B - Números diferentes
                - Se os três números forem diferentes, você ganha 2x sua aposta!
            C - Números pares ou ímpares
                - Se o resultado for todo par ou todo ímpar, você ganha 10x sua aposta!
            D - Números específicos
                - Se você adivinhar um número específico, você ganha 5x sua aposta!
          """)
    print("Boa sorte!\n")


def options():
    print("Escolha uma opção de aposta:")
    print("A - Números iguais")
    print("B - Números diferentes")
    print("C - Números pares ou ímpares")
    print("D - Números específicos")
    escolha = input("Digite sua escolha (A, B, C ou D): ").upper()
    return escolha


def roulete():
    clock = 0.01
    c1 = c2 = c3 = "\033[0m"
    while clock < 0.41:
        if clock < 0.2:
            s1 = randint(1, 7)
        else:
            c1 = f"\033[32m"
        if clock < 0.3:
            s2 = randint(1, 7)
        else:
            c2 = f"\033[32m"
        if clock < 0.4:
            s3 = randint(1, 7)
        else:
            c3 = f"\033[32m"
        clock += 0.01
        print("\033[F\033[K", end="")
        print("\033[F\033[K", end="")
        print(f"ROLETA: \n {c1}{s1} : {c2}{s2} : {c3}{s3} \n", end="\r")
        sleep(clock)
    return int(s1), int(s2), int(s3)


def main():
    init()
    valores = roulete()
    if valores[0] == valores[1] == valores[2]:
        print(f"\033[32mPARABÉNS! VOCÊ GANHOU! O NÚMERO SORTEADO FOI {valores[0]}!\033[0m")
    elif valores.count(valores[0]) > 1 or valores.count(valores[1]) > 1 or valores.count(valores[2]) > 1:
        print(f"\033[33mQUASE! VOCÊ GANHOU METADE! OS NÚMEROS SORTEADOS FORAM {valores[0]}, {valores[1]} e {valores[2]}!\033[0m")
    else:
        print(f"\033[31mQUE PENA! VOCÊ PERDEU! OS NÚMEROS SORTEADOS FORAM {valores[0]}, {valores[1]} e {valores[2]}!\033[0m")


if __name__ == "__main__":
    main()