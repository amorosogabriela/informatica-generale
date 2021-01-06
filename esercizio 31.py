print("rappresentazione in binario di un numero decimale")
binario = []
num = int(input("indica un numero naturale: "))
while True:
    quoz = int(num/2)
    resto = num % 2
    if resto == 1:
        binario.append (1)
    else:
        binario.append (0)
    num = quoz
    
    if quoz == 0:
        break

binario.reverse ()
print(binario)
