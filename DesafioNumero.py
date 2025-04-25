import random

print("[ + ]                      Descubra o número                        [ + ]")
print("[-->] Um número foi gerado, ele pode ser maior que 1 e menor que 20 [<--]")

numero = random.randint(1, 20)

rodando = True
tentativas = 0

while rodando:
    tentativas = tentativas + 1
    try:
        escolha = int(input("[***] Digite o número:\n"))
    except ValueError:
        print("[!!!] Valor inválido, use apenas numeros.")
        tentativas = tentativas - 1
        continue

    if escolha > numero:
        print("[!!!] O número gerado é MENOR que esse!")
    elif escolha < numero:
        print("[!!!] O número gerado é MAIOR que esse!")
    else:
        rodando = False

print(f"[ + ]                  Parabéns                  [ + ]")
print(f"[-->] O número era {numero}")
print(f"[-->] Você acertou depois de {tentativas} tentativas.")

