def ler_valores():
    tempo = int(input("Digite tempo gasto na viagem (em horas): "))
    velocidade = int(input("Digite a velocidade média durante a viagem (em km/h): "))
    return tempo, velocidade

def calcular_distancia(tempo, velocidade):
    distancia = tempo * velocidade
    return distancia

def calcular_litros(distancia):
    litros = distancia / 12
    return litros

def apresentar_resultado(tempo, velocidade, distancia, litros):
    print(f"Velocidade média: {velocidade} km/h")
    print(f"Tempo gasto na viagem: {tempo} horas")
    print(f"Distância percorrida: {distancia} km")
    print(f"Litros de combustível utilizados: {litros:.2f} litros")

tempo, velocidade = ler_valores()
distancia = calcular_distancia(tempo, velocidade)
litros = calcular_litros(distancia)
apresentar_resultado(tempo, velocidade, distancia, litros)
