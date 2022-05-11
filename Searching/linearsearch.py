def linearSearchFunction(lista,valor):

  x = False

  for i in range (len(lista)):
    if valor == lista[i]:
      print()
      return i
      x = True
  if x == False:
     print()