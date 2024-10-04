print("")
print("*"*17)
print("Programa de lista")
print("*"*17)
print("")
lista=[0]*10
soma=0
for i in range(10):
   lista[i]=int(input(f"Digite o {i+1}º elemento: "))
   soma+=lista[i]
print("")
print("*"*5)
print("Lista")
print("*"*5)
print("")
print("Números digitados são:")
print(lista)
print("")
print("*"*10)
print("Resultado")
print("*"*10)
print("")
print(f"O somatório é {soma}")
