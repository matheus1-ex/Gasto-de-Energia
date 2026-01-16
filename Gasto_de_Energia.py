#Você quer ter uma noção de quanto gasta de energia elétrica em casa,
#para não se assustar quando a conta chegar.
aparelho = str(input("Digite o aparelho que deseja calcular: "))
watts = int(input(f"Digite o watts do aparelho ({aparelho}): "))
horasPordia = int(input(f"Quantas horas o aparelho ({aparelho}) fica ligado: "))
DiasdoMes = int(input("Quantos dias do mês ele é usado (ex: 30): "))
valorKwh = float(input("Valor do kwh: "))
#Calcular...
kw = watts / 1000
consumo = (kw * horasPordia) * DiasdoMes
custo = consumo * valorKwh
media = custo / DiasdoMes
print(f"Aparelho: {aparelho}\nConsumo mensal aproximado: {consumo:.2f}kwh\nValor total da conta desse aparelho: R${custo:.2f}\nA Média de gasto diário: R${media:.2f}")
