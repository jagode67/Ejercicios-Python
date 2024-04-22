'''E129
Mostrar por pantalla el contenido del archivo b.txt

'''
a=open("b.txt","r",encoding="utf-8")
t=a.read()
a.close()
print(t)





