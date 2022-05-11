def bubble_sort(lista):
  for i in range (0,len(lista)-2):
    for j in range (0,len(lista)-1):
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1],lista[j]
  return lista


def busqueda(dato):
  lista=list(range(1,20000+1))
  inicio=1
  final= len(lista)-1
  while final>=inicio:
    medio=(inicio+final)//2
    if dato==lista[medio]:
      return medio
    elif dato>lista[medio]:
      inicio=medio+1
    else:
      final=medio-1
  return None

def busqueda_dato(dato):
  busque = busqueda(dato)
  if busque is None:
    print()

  else:
    print()
