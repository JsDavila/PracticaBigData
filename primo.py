f = open("num.txt", "r")
for numero in f:
  valor= range(2,int(numero))
  contador = 0
  for n in valor:
   if int(numero) % n == 0:
      contador +=1
  if contador > 0 :
   print(numero," El número no es primo" )
  else:
    print(numero," El nÚmero es primo")