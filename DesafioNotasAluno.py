def calc_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media < 5:
        print("Reprovado")
    elif media >= 5 and media <= 6.9:
        print("Recuperação")
    else:
        print("Aprovado")


continuar = True
while continuar:
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))

    pergunta = int(input("Deseja calcular a media de outro aluno? \n[ 1 ] - SIM\n[ 2 ] - NÃO\n"))

    if (pergunta == 2):
        continuar = False
        break
    calc_media(nota1, nota2, nota3)
