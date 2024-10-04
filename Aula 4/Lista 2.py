print("")
print("*"*17)
print("Programa de lista")
print("*"*17)
print("")
n=int(input(f"Digite quantos elementos possui a lista: "))
lista=[0]*n
soma=0
for i in range(n):
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
