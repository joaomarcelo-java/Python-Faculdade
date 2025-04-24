pares = 0

for i in range(1, 51):
    if i % 2 == 0:
        print(f"O número {i} é par!")
        pares += 1

print(f"Entre 1 e 50 existem {pares} números pares.")
