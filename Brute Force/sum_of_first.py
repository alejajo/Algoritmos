def sum_of_firts():
    n= int(input("Ingrese el numero hasta donde desea llegar:"))
    print("n:",n)

    suma=0

    for num in range(n+1):

        suma=suma+num

    print("suma", suma)