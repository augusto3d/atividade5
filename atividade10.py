def calcular_media(lista_numeros):
    total = sum(lista_numeros)
    media = total / len(lista_numeros)
    return media

numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)

print(f"A média dos valores é {numeros} é {media}")
