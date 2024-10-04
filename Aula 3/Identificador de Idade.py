print("*"*25)
print("Identificador de Idade")
print("*"*25)
idade=int(input("Qual é a sua idade:\n"))
if (idade<=12):
    print(f"Você tem {idade} anos, por isso é uma Criança")
elif (idade<=17):
    print(f"Você tem {idade} anos, por isso é um Adolescente")
elif (idade<=59):
    print(f"Você tem {idade} anos, por isso é um Adulto")
else:
    print(f"Você tem {idade} anos, por isso é um Idoso")    
    
