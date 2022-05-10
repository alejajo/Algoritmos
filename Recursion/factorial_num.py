def  factorial_num():
  num=int(input("Ingrese un numero del que desee saber el factorial:   "))
  i=0
  a =1
  while i<num:
    i+=1
    a *=i
  print(a)