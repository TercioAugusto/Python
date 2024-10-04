print("")
print("*"*40)
print("Programa de Repetição")
print("*"*40)
n=int(input("Quantos números são digitados?\n"))
qpar=0
qimpar=0
for i in range(1,n+1):
    nun=int(input(f"Digite o valor do {i} número: "))
    if(nun%2==0):
        qpar+=1
    else:
        qimpar+=1

        
print("")
print("*"*20)
print("Resultados")
print("*"*20)
print(f"\nForam digitados {n} números")
print(f"Sendo que, no conjunto numérico temos {qpar} números pares e {qimpar} números impares")
