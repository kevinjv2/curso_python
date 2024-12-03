#COMENTARIOS

#VARIABLES TIPO STRING
name = "Kevin"
last_name = "Jacobo"

print(name)

#VARIABLES NUMERO
numero = 19
numero2 = 20

suma = numero + numero2
print(suma)

#CADENAS
nombre = "Kevin Ramon"
apellido = "Jacobo Sanchez"
edad = 19

print("Me llamo, " + nombre + ' ' + apellido) #OPCION 1
print(f"Me llamo {nombre} {apellido} y tengo {edad} de edad") #OPCION 2

#LISTAS
list = ["Python", "DJANGO", "REACT", "VUE"]

print(list[2])
#IMPRIMIR EL ULTIMO ELEMENTO DE UNA LISTA
lista2 = ["Manzana", "Platano", "Durazno"]
print(lista2[-1])

#CAMBIAR UN DATO:  lista2[0] = "Melon" 
#                    print(lista2)

#AÑADIR UN NUEVO DATO
#lista2.append('Nombre del dato')

#AÑADIR ESPECIFICAMENTE DONDE SE UBICARA EL NUEVO DATO
#lista2.insert(1, 'Arroz') DESPUES DE MANZANA


#DICCIONARIO

data = {"name": "Kevin", "last_name":  "Jacobo", "edad": 19}
print(data)
print(data["name"])
#concadenar
print(f"MI NOMBRE ES {data["name"]}")
#añadir un dato
data["ciudad"] = "Colima"
#eliminar un dato de diccionario con "del"
del data["edad"]
print(data)
#como saber cuantos datos hay, con "len"
print(len(data))