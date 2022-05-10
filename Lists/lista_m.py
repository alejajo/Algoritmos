
def lista_m(list1, list2): 

  newlista = []

  a = 0
  j = 0 

  while a < len(list1) and j <len(list2):
    
    if list1[a] < list2[j]:
      newlista.append(list1[a])
      a += 1 
    else:
      newlista.append(list2[j])
      j += 1

  if    a == len(list1):
    for k in range(j, len(list2)):
      newlista.append(list2[k])

  else:
    for k in range(a, len(list1)):
      newlista.append(list1[k])

  return newlista