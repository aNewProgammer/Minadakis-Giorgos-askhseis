lista_keimenou=[]
l=raw_input("Parakalw eisagete keimeno: ")
lista_keimenou=list(l)
plhthos=len(lista_keimenou)
for i in range(0,plhthos):
 if lista_keimenou[i]==0 or lista_keimenou[i]=="0":
  del lista_keimenou[i]
  lista_keimenou.extend([0])
for i in range(-1,plhthos-1):
 if lista_keimenou[i]==0 or lista_keimenou[i]=="0":
  del lista_keimenou[i]
  lista_keimenou.extend([0])
print lista_keimenou
