import math
catetoOp = input('Valor do Cateto Oposto')
catetoAdj = input ('Valor do Cateto Adjacente')
hipotenusa = (catetoOp**2)+(catetoAdj**2)
hipotenusa = math.sqrt(hipotenusa)
print "Valor da Hipotenusa= %.2f " %hipotenusa