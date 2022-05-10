def nth_fibonaacci():
  def f(number):
    if (number==0):
      return 0
    elif(number==1):
      return 1
    else:
      return (f(number-2)+f(number-1))
  n=int(input("Ingrese hasta que valor desea ingresar:  "))
  for n in range(0,n+2):
    print(f(n))