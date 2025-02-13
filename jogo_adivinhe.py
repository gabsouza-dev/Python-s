import random

def jogo_adivinhe():
    numero_secreto = random.randint(1, 100)
    tentativa = 0

    print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número entre 1 e 100.")

    while True:
        tentativa += 1
        chute = int(input("Digite seu palpite: "))

        if chute < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif chute > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou em {tentativa} tentativas.")
            break

jogo_adivinhe()