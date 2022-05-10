def bubble_sort(lista):
  for i in range (0,len(lista)-2):
    for j in range (0,len(lista)-1):
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1],lista[j]
  return lista