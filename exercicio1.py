from time import sleep
from random import randint

def roulete():
    clock = 0.01
    while clock < 0.41:
        if clock < 0.2:
            s1 = randint(1, 7)
        else:
            s1 = f"\033[32m{s1}\033[0m"
        if clock < 0.3:
            s2 = randint(1, 7)
        else:
            s2 = f"\033[32m{s2}\033[0m"
        if clock < 0.4:
            s3 = randint(1, 7)
        else:
            s3 = f"\033[32m{s3}\033[0m"
        clock += 0.01
        print("\033[F\033[K", end="")
        print("\033[F\033[K", end="")
        print(f"ROLETA: \n {s1} : {s2} : {s3} \n", end="\r")
        sleep(clock)

roulete()