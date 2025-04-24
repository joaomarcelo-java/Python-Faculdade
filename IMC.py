peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / pow(altura, 2)

print(f"O seu IMC(Indice de Massa Corporal é: {imc:.2f}")