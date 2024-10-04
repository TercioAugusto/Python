print("")
print("*"*25)
print("Programa de Repetição")
print("*"*25)
n=int(input("\nQual a quantidade de número a serem digitados?\n"))
soma=0
for i in range(1,n+1):
    num=int(input(f"Digite o valor do {i}º número:\n"))
    soma+=num
print(f"A soma dos {n} números digitados é: {soma}")    
