palavra = input("Insira uma palavra")
k = input("Insira um numero")
if k<(len(palavra)):
    kesima = palavra[k-1]
    print kesima
else:
    print "Numero informado eh maior que numero de letras na palavra"