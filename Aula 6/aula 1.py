n=int(input("Digite quantos elementos possui o vetor: "))
lista=[0]*n
for i in range(n):
    lista[i] = int(input(f"Digite um {i+1}º valor: "))
print(lista)    
soma= sum(lista)
print (soma)
