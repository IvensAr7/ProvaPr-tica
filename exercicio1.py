from time import sleep
from random import randint
import os


def limpar_tela():
    os.system('cls')


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
    while True:
        escolha = input("Digite sua escolha (A, B, C ou D): ").upper().strip()
        if escolha in ["A", "B", "C", "D"]:
            return escolha
        else:
            print("Opção inválida. Tente novamente.")


def aposta(pontos):
    print(f"Você tem {pontos} pontos.")
    valor = 0
    while True:
        valor = int(input("Quanto você quer apostar? "))
        if valor > pontos or valor <= 0:
            print("Valor inválido. Tente novamente.")
        else:
            break
    return valor


def roulete(escolha):
    clock = 0.01
    c1 = c2 = c3 = "\033[0m"
    if escolha == "A":
        regra = "3 iguais: 50x | 2 iguais: 20x"
    elif escolha == "B":
        regra = "3 diferentes: 2x"
    elif escolha == "C":
        regra = "Todos pares ou todos ímpares: 10x"
    elif escolha == "D":
        regra = "Número específico: 5x"
    
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
        print(f"ROLETA {regra}: \n {c1}{s1} : {c2}{s2} : {c3}{s3} \n", end="\r")
        sleep(clock)
    print("\033[m")
    return int(s1), int(s2), int(s3)


def main():
    pontos = 200
    init()
    while True:
        escolha = options()
        valor = aposta(pontos)
        limpar_tela()
        if escolha == "A":
            valores = roulete(escolha)
            if valores[0] == valores[1] == valores[2]:
                print(f"\033[0;32m+{valor*50}\033[m")
                print("Parabéns! Você ganhou 50x sua aposta!")
                pontos += valor * 50
            elif valores[0] == valores[1] or valores[1] == valores[2] or valores[0] == valores[2]:
                print(f"\033[0;32m+{valor*20}\033[m")
                print("Parabéns! Você ganhou 20x sua aposta!")
                pontos += valor * 20
            else:
                print(f"\033[0;31m-{valor}\033[m")
                print("Que pena! Você não ganhou nada dessa vez.")
                pontos -= valor
        elif escolha == "B":
            valores = roulete(escolha)
            if valores[0] != valores[1] and valores[1] != valores[2] and valores[0] != valores[2]:
                print(f"\033[0;32m+{valor*2}\033[m")
                print("Parabéns! Você ganhou 2x sua aposta!")
                pontos += valor * 2
            else:
                print(f"\033[0;31m-{valor}\033[m")
                print("Que pena! Você não ganhou nada dessa vez.")
                pontos -= valor
        elif escolha == "C":
            valores = roulete(escolha)
            if (valores[0] % 2 == 0 and valores[1] % 2 == 0 and valores[2] % 2 == 0) or (valores[0] % 2 != 0 and valores[1] % 2 != 0 and valores[2] % 2 != 0):
                print(f"\033[0;32m+{valor*10}\033[m")
                print("Parabéns! Você ganhou 10x sua aposta!")
                pontos += valor * 10
            else:
                print(f"\033[0;31m-{valor}\033[m")
                print("Que pena! Você não ganhou nada dessa vez.")
                pontos -= valor
        elif escolha == "D":
            num = int(input("Escolha um número entre 1 e 7: "))
            valores = roulete(escolha)
            if num in valores:
                print(f"\033[0;32m+{valor*5}\033[m")
                print("Parabéns! Você ganhou 5x sua aposta!")
                pontos += valor * 5
            else:
                print(f"\033[0;31m-{valor}\033[m")
                print("Que pena! Você não ganhou nada dessa vez.")
                pontos -= valor
        
        if pontos <= 0:
            print("\033[0;31mSaldo 0 !!!\033[m")
            print("Você ficou sem pontos! Fim de jogo.")
            break
        else:
            print(f"Você agora tem {pontos} pontos.\n")


if __name__ == "__main__":
    main()