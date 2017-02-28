p =raw_input('Dwse mia protash: ')
lista = list(p)
pl=(len(lista)-1)
x=0
k=pl
while (k>=0):
 if lista[k]!='!':
  x=1
 elif x==1:
  del lista[k]
 k = k -1 
print lista
k=input()