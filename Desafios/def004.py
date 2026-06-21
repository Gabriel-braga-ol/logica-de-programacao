pais_a = 80000
pais_b = 200000
anos = 0

while True:
    pais_a += (pais_a * 3) / 100
    pais_b += (pais_b * 1.5) / 100
    anos += 1

    if pais_a >= pais_b:
        print(f'{pais_a:.2f}')
        print(f'{pais_b:.2f}')
        print(f'{anos}')
        break

