numeros = [] 
for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)


soma = 0
for numero in numeros:
    soma += numero

print("A soma dos números é:", soma)