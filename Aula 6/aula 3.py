continua="S"
lista=[]
while (continua == "s" or continua == "S"):
    n=eval(input("Digite um número: "))
    lista.append(n)
    continua=input("Deseja continuar? 's' para sim ou 'n' para não: ")
print(lista)
