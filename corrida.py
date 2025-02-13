import random
import time

def corrida():
    posicao1 = 0
    posicao2 = 0
    
    while posicao1 < 50 and posicao2 < 50:
        posicao1 += random.randint(1, 6)
        posicao2 += random.randint(1, 6)
        
        print(f"Corredor 1: {'=' * posicao1}>")
        print(f"Corredor 2: {'=' * posicao2}>")
        print("-" * 50)
        time.sleep(0.5)
    
    if posicao1 >= 50 and posicao2 >= 50:
        print("Empate!")
    elif posicao1 >= 50:
        print("Corredor 1 venceu!")
    else:
        print("Corredor 2 venceu!")

corrida()
