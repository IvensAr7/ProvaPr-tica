from time import sleep
from random import randint, choice
import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


class C:
    R = '\033[91m'
    G = '\033[38;5;76m' 
    O = '\033[38;5;202m'
    Y = '\033[38;5;184m'
    
    RESET = '\033[0m' # RESET

    # TEXTO COLORIDO
    def P(texto, cor):
        return f"{cor}{texto}{C.RESET}"

    # INPUT COLORIDO
    def input(msg, cor):          # Ativa a cor ANTES do input
        resposta = input(f"{msg}{cor}")                      # O que for digitado sai colorido
        print(C.RESET, end='', flush=True)          # Reseta cor após digitação
        return resposta


def regras():
    print(f"""As regras são simples:
{C.P('1.', C.G)} Você começa com {C.P('200', C.G)} pontos
{C.P('2.', C.G)} Pode apostar quantas moedas quiser em uma das opções a seguir:
    {C.P('A', C.O)} - Números iguais
        - Se os três números forem iguais: {C.P('30x', C.Y)}
        - Se dois números forem iguais: {C.P('5x', C.Y)}
    {C.P('B', C.O)} - Números diferentes
        - Se os três números forem diferentes:{C.P('4x', C.Y)}
    {C.P('C', C.O)} - Números pares ou ímpares
        - Se o resultado for todo par ou todo ímpar: {C.P('8x', C.Y)}
    {C.P('D', C.O)} - Números proibidos
        - Se não cair os números {C.P('1', C.R)} ou {C.P('7', C.R)} multiplica a {C.P('aposta', C.Y)} pela {C.P('soma dos números', C.Y)}
    {C.P('E', C.O)} - Números específicos
        - Se acertar um número que apareça ao menos uma vez nos três: {C.P('2x', C.Y)}
        - Se o número aparecer duas vezes: {C.P('6x', C.Y)}
        - Se aparecer três vezes: {C.P('10x', C.Y)}""")


def options():
    print(f"""Escolha uma opção de aposta:
{C.P("A", C.Y)} - {C.P("Números iguais", C.O)} - 3 iguais: {C.P("30x", C.Y)} | 2 iguais: {C.P("5x", C.Y)}
{C.P("B", C.Y)} - {C.P("Números diferentes", C.O)} - 3 diferentes: {C.P("4x", C.Y)}
{C.P("C", C.Y)} - {C.P("Números pares ou ímpares", C.O)} - Todos pares ou todos ímpares: {C.P("8x", C.Y)}
{C.P("D", C.Y)} - {C.P("Números proibidos", C.O)} - Se não cair os números 1 e 7: aposta x {C.P("soma dos números", C.Y)}         
{C.P("E", C.Y)} - {C.P("Número específico", C.O)} - Uma vez: {C.P("2x", C.Y)} | Duas vezes: {C.P("6x", C.Y)} | Três vezes: {C.P("10x", C.Y)}""")
     
    while True:
        escolha = C.input("Digite sua escolha (A, B, C, D, E): ", C.Y).upper().strip()
        if escolha in ["A", "B", "C", "D", "E"]:
            return escolha
        else:
            print("Opção inválida. Quer inventar regra agora ou só não sabe digitar mesmo?")


def aposta(pontos):
    msgs = ['Quanto você quer apostar? ', 'Quanto você quer apostar? ', 'Quanto você quer apostar? ', 'Quanto você quer apostar? ', 'Quanto você quer apostar? ', 'Quanto você quer apostar? ', 'Quanto você quer ~perder~? ', 'Quanto você quer apostar? (Vai no All-Win confia) ', f'Quanto você quer apostar? (metadinha de {pontos} é {int(pontos/2)}, vale a pena) ', 'Quanto você quer apostar? (Já disse que apostar tudo é o caminho?) ', 'Se tem coragem de verdade tu vai apostar tudo: ', f'Quanto você quer apostar? (Na minha mão, esses {pontos} pontos aí já tinham virado 1 bilhão!) ']
    
    print(f"Pontos: {C.P(f'{pontos}', C.G)}")
    valor = 0
    while True:
        msg = choice(msgs)
        try:
            valor = int(C.input(msg, C.Y))
        except ValueError:
            print(f"{C.P('[ ! ] Esse valor é inválido', C.R)}")
            continue
        if valor > pontos:
            print(f"Acho que você não tem tudo isso, ganhe mais {valor - pontos} que você pode apostar isso.")
        elif valor <= 0:
            print("Você achava mesmo que ia dar certo?")
        elif valor < (20/100) * pontos:
            print(f"Vai apostar SÓ {valor} ??? Tu tem {pontos} se liga")
        else:
            break
    return valor


def roulete(escolha):
    clock = 0.01
    c1 = c2 = c3 = "\033[0m"
    if escolha == "A":
        regra = "3 iguais: 30x | 2 iguais: 5x"
    elif escolha == "B":
        regra = "3 diferentes: 4x"
    elif escolha == "C":
        regra = "Todos pares ou todos ímpares: 8x"
    elif escolha == "D":
        regra = "Se não cair 1 ou 7: soma x aposta"
    elif escolha == "E":
        regra = "Número específico - Uma vez: 2x | Duas vezes: 6x | Três vezes: 10x "
    
    while clock < 0.41:
        if clock < 0.2:
            s1 = randint(1, 7)
        else:
            c1 = C.G
        if clock < 0.3:
            s2 = randint(1, 7)
        else:
            c2 = C.G
        if clock < 0.4:
            s3 = randint(1, 7)
        else:
            c3 = C.G
        clock += 0.01
        print("\033[F\033[K", end="")
        print("\033[F\033[K", end="")
        print(f"ROLETA {regra}: \n {c1}{s1} : {c2}{s2} : {c3}{s3} \n", end="\r")
        sleep(clock)
    print("\033[m")
    return int(s1), int(s2), int(s3)


def menu():
    print(f'''{C.P("BEM VINDO", C.O)} ao JOGO DE {C.P("APOSTAS", C.O)} (by {C.P("Ivens", C.Y)})
[ {C.P("0", C.Y)} ]     - SAIR DO JOGO
[ {C.P("1", C.Y)} ]     - VER REGRAS
[ {C.P("ENTER", C.Y)} ] - JOGAR
          ''')
    msg = 'Eu quero... '
    while True:
        op = C.input(msg, C.Y)
        if op not in ['0', '1', '']:
            print('Escolha direito !!!')
            msg = 'Tá bom, então eu quero... '
            continue
        elif op == '0':
            print('Mas já ??? Ok, só não vá jogar no ~você sabe o que~')
            return True
        elif op == '1':
            print('Quem ainda lê regras? Então tá né.')
            regras()
            continue 
        elif op == '':
            limpar_tela()
            return False


def main():
    pontos = 200

    if menu():
        return
    while True:
        escolha = options()
        valor = aposta(pontos)
        limpar_tela()
        if valor <= 30:
            print(f'Tá duro? Tu vai apostar só {valor} pontos? Tá bom né...')
        if valor == pontos:
            print('Tudo ou nada? Que não sobre nada pro beta então.')
        if escolha == "A":
            pontos -= valor
            valores = roulete(escolha)
            
            if valores[0] == valores[1] == valores[2]:
                print(f"\033[0;32m+{valor*30}\033[m")
                print("IMPOSSÍVEL, que sorte viu: ganhou 30x a sua aposta")
                pontos += valor * 30
            elif valores[0] == valores[1] or valores[1] == valores[2] or valores[0] == valores[2]:
                print(f"\033[0;32m+{valor*5}\033[m")
                print("Palmas: ganhou 5x a sua aposta!")
                pontos += valor * 5
            else:
                print(f"\033[0;31m-{valor}\033[m")
                print("Que pena! Você não ganhou nada dessa vez.")
        elif escolha == "B":
            pontos -= valor
            valores = roulete(escolha)

            if valores[0] != valores[1] and valores[1] != valores[2] and valores[0] != valores[2]:
                print(f"\033[0;32m+{valor*4}\033[m")
                print("Queria ter a sua sorte: ganhou 4x sua aposta.")
                pontos += valor * 4
            else:
                print(f"\033[0;31m-{valor}\033[m")
                print("Que peninha, não foi dessa vez, quem sabe numa próxima...")
        elif escolha == "C":
            pontos -= valor
            valores = roulete(escolha)

            if (valores[0] % 2 == 0 and valores[1] % 2 == 0 and valores[2] % 2 == 0) or (valores[0] % 2 != 0 and valores[1] % 2 != 0 and valores[2] % 2 != 0):
                print(f"\033[0;32m+{valor*8}\033[m")
                print("Você me cheira exatas, não sei o porquê: ganhou 8x sua aposta.")
                pontos += valor * 8
            else:
                print(f"\033[0;31m-{valor}\033[m")
                print("Talvez um dia você dê orgulho pra sua família, infelizmente não foi hoje...")
        elif escolha == "D":
            pontos -= valor
            valores = roulete(escolha)

            if (1 in valores) or (7 in valores):
                print(f"\033[0;31m-{valor}\033[m")
                print("Vai na fé que na próxima vem.")
            else:
                soma = sum(valores)
                print(f"\033[0;32m+{valor*soma}\033[m")
                print(f"Fantástico: ganhou {soma}x a sua aposta!")
                pontos += valor * soma
        elif escolha == "E":
            pontos -= valor
            while True:
                try:
                    num = int(input("Escolha um número entre 1 e 7: "))
                    if 1 <= num <= 7:
                        break
                    print('Acho que você não entendeu a parte em que eu disse "entre 1 a 7"')
                except ValueError:
                    print(f"Assim né, eu não conheço o número '{num}', vou acreditar que você tentou escrever por extenso...")

            valores = roulete(escolha)

            if num not in valores:
                print(f"\033[0;31m-{valor}\033[m")
                print(f"Não se preocupe, um desgosto de pessoa é assim mesmo, {num} talvez não seja o SEU número da sorte...")
            elif valores.count(num) == 1:
                print(f"\033[0;32m+{valor*2}\033[m")
                print("Poderia ser melhor: ganhou 2x sua aposta.")
                pontos += valor * 2
            elif valores.count(num) == 2:
                print(f"\033[0;32m+{valor*6}\033[m")
                print("WOW, sorte de principiante: ganhou 6x sua aposta.")
                pontos += valor * 6
            elif valores.count(num) == 3:
                print(f"\033[0;32m+{valor*10}\033[m")
                print("Isso claramnete é um esquema de apostas: ganhou 10x sua aposta.")
                pontos += valor * 10

        if pontos <= 0:
            print(f"\033[0;31mSaldo {pontos}!!!\033[m")
            print("Você ficou oficialmente duro! Fim da linha aqui pra você.")
            break
        else:
            print(f"Você agora tem {pontos} pontos.\n")

 
if __name__ == "__main__":
    main()