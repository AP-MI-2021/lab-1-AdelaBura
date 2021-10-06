
'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  if (n==0 or n==1):
    return False
  for d in range (2, n//2+1):
    if (n%d==0):
        return False
  return True
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  prod = 1
  for el in range (0, len(lst)):
    prod = prod * lst[el]
  return prod
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
   if x==0:
     return y
   if y==0:
     return x
   while (x!=y):
      if (x>y):
         x-=y
      else:
          y-=x
   return x
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  if x < y:
    c = x
    x = y
    y = c
  while (y != 0):
    c = x % y
    x = y
    y = c
  return x

def main():
  # interfata de tip consola aici
  print ('''
  1. IS prime
  2.Product
  3.Cmmdc v1
  4.Cmmdc v2
''')
  x= int (input("Comanda:"))
  if (x==1):
    # is prime
    n = int(input("Introduceti n="))
    print (is_prime(n))
  if (x==2):
    # product
    n = int(input("Introduceti n="))
    list = []
    for i in range (0,n):
      el = int(input ())
      list.append(el)
    print(list)
    print(len(list)) #lungimea listei
    print (get_product(list))
    
    # print (is_prime(n))
  if (x==3):
   x = int(input("Introduceti n="))
   y = int(input("Introduceti n="))
   print (get_cmmdc_v1(x,y))

  if (x==4):
   x = int(input("Introduceti n="))
   y = int(input("Introduceti n="))
   print (get_cmmdc_v2(x, y))
  
if __name__ == '__main__':
  main()
