from time import sleep

def tratarnum(ordem):
    while True:
        if ordem == 1:
            num = input("Digite o primeiro número: \n")
        else:
            num = input("Digite o segundo número: \n")
        try:
            return float(num)
        except ValueError:
            print("\n\nUse apenas números!\n\n")
            sleep(1)


def soma():
    num1 = tratarnum(1)
    num2 = tratarnum(2)
    print(f"A soma entre {num1} e {num2} é {num1 + num2}")


def subtracao():
    num1 = tratarnum(1)
    num2 = tratarnum(2)
    print(f"A subtração de {num1} em {num2} é {num1 - num2}")


def multiplicacao():
    num1 = tratarnum(1)
    num2 = tratarnum(2)
    print(f"A multiplicação entre {num1} e {num2} é {num1 * num2}")


def divisao():
    num1 = tratarnum(1)
    while True:
        num2 = tratarnum(2)
        if num2 == 0:
            print("O divisor não pode ser 0!")
            sleep(2)
        else:
            print(f"A divisão de {num1} por {num2} é {num1 / num2}")
            break


def menucalc():
    continuar = True

    while continuar:
        print("### Qual operação deseja realizar? ###")
        opc = input("[ 1 ] - Soma\n[ 2 ] - Subtração\n[ 3 ] - Multiplicação\n[ 4 ] - Divisão\n[ 5 ] - Sair\n")

        match opc:
            case "1":
                soma()
            case "2":
                subtracao()
            case "3":
                multiplicacao()
            case "4":
                divisao()
            case "5":
                print("Saindo da calculadora!")
                break
            case _:
                print("Opção inválida! Retornando ao menu!")
                sleep(2)
                continue

        escolha = input("Deseja realizar mais operações?\n[ 1 ] - SIM\n[ 2 ] - NÃO\n")
        if escolha == "1":
            continuar = True
        else:
            print("Saindo da calculadora!!")
            continuar = False


print("Bem vindo a calculadora!!")
menucalc()
