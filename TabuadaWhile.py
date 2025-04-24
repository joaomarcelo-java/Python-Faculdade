continuar = True

def tabuada(num1):
    print(f"### TABUADA DO {num1} ###")
    for i in range(1, 11):
        valor = i * num1
        print(f"{i} x {num1} = {valor}")


def pergunta():
    pergunta = input("Deseja ver a tabuada de outro número?\n[ 1 ] - SIM\n[ 2 ] - NÃO\n")
    if pergunta == "1":
        return True
    elif pergunta == "2":
        print("Saindo da calculadora.")
        return False
    else:
        print("Resposta inválida! Fechando calculadora.")
        return False


def menu():
    num1 = int(input("Digite o numero que deseja ver a tabuada:"))
    tabuada(num1)


print("Bem-vindo a calculadora de tabuada!!")

while continuar:
    menu()
    continuar = pergunta()
