def verificaparametro():
    num1 = int(input("Digite um número entre 1 e 10 para liberar o console: "))
    if num1 > 10 or num1 < 1:
        return True
    else:
        return False


while verificaparametro():
    print("Valor incorreto!")

print("Valor correto!")
