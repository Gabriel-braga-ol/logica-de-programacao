notas = [5, 8, 9, 7, 7, 10, 6, 8, 5, 7]

notas[-1] = 4
print(notas.count(7))
print(notas)
print(max(notas))

media = sum(notas) / len(notas)
print(media)