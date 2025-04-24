num1 = int(input("Digite o número que deseja ver a tabuada: "))

print(f"### Tabuada do número {num1} ###")

for i in range(1, 11):
    res = i * num1
    print(f"{i} x {num1} = {res}")
