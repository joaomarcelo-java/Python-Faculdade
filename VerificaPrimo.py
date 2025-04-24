def verificaprimo(num1):
    primo = True
    if num1 < 2:
        primo = False
    for i in range(2, num1 + 1):
        if num1 % i == 0 and i != num1:
            primo = False
            break
    return primo


num1 = int(input("Digite um número para saber se é primo ou não: "))

if verificaprimo(num1):
    print(f"O número {num1} é primo.")
else:
    print(f"O número {num1} não é primo.")
