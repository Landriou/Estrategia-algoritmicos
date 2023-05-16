
from linkedlist import *
from algo1 import *
from sort import *
from greedy import *
from DivideAndConquer import *
from backtracking import *
from dynamicProgramming import*

A = Array(5,0)
A[0] = 1
A[1] = 2
A[2] = 6
A[3] = 8
A[4] = 10
print("Ejercicio 1")
imprimirlista(darCambio(14,A))
print("\nEjercicio 2")
A2 = Array(6,0)
A2[0] = 4
A2[1] = 4
A2[2] = 4
A2[3] = 4
A2[4] = 4
A2[5] = 13
imprimirlista(mochila(20, A2)) 
print("\nEjercicio 2")
A2 = Array(6,0)
A2[0] = 4
A2[1] = 4
A2[2] = 4
A2[3] = 4
A2[4] = 13
A2[5] = 4

imprimirlista(mochila(20, A2)) 
print("\nEjercicio 2")

A2 = Array(6,0)
A2[0] = 4
A2[1] = 4
A2[2] = 4
A2[3] = 13
A2[4] = 4
A2[5] = 4
imprimirlista(mochila(20, A2)) 
print("\nEjercicio 2")
A2 = Array(6,0)
A2[0] = 4
A2[1] = 4
A2[2] = 13
A2[3] = 4
A2[4] = 4
A2[5] = 4
imprimirlista(mochila(20, A2)) 
print("\nEjercicio 2")
A2 = Array(6,0)
A2[0] = 4
A2[1] = 13
A2[2] = 4
A2[3] = 4
A2[4] = 4
A2[5] = 4
imprimirlista(mochila(20, A2)) 

print("\nEjercicio 3")
A3 = Array(10,0)
A3[0] = 21
A3[1] = 19
A3[2] = 8
A3[3] = 17
A3[4] = 20
A3[5] = 100
A3[6] = 3
A3[7] = 2
A3[8] = 1
A3[9] = 5

imprimirlista(subSecuenciaCreciente(A3))
print("\nEjercicio 4")
A4 = Array(7,0)
A4[0] = 7
A4[1] = 10
A4[2] = 3
A4[3] = 5
A4[4] = 9
A4[5] = 6
A4[6] = 7
print(subconjuntoSuma(A4,15))

################ PARTE 2##################
print("PARTE 2 GREEDY")
tareas = LinkedList()
a1 = makeTarea("a1",1,3,False)
a2 = makeTarea("a2",2,5,False)
a3 = makeTarea("a3",4,7,False)
a4 = makeTarea("a4",1,8,False)
a5 = makeTarea("a5",5,9,False)
a6 = makeTarea("a6",8,10,False)
a7 = makeTarea("a7",9,11,False)
a8 = makeTarea("a8",11,14,False)
a9 = makeTarea("a9",13,16,False)
add(tareas, a1)
add(tareas, a2)
add(tareas, a3)
add(tareas, a4)
add(tareas, a5)
add(tareas, a6)
add(tareas, a7)
add(tareas, a8)
add(tareas, a9)

imprimirlista(adminActividades(tareas, 0, 16))

vector = Array(6,0)
vector[0] = 5
vector[1] = 8
vector[2] = 1
vector[3] = 4
vector[4] = 7
vector[5] = 9
print("")
print(buscaPares(vector))

latas = Array(6,Lata())

a1 = Lata()
a1.Beneficio = 5
a1.Peso = 3

a2 = Lata()
a2.Beneficio = 5
a2.Peso = 2

a3 = Lata()
a3.Peso = 7
a3.Beneficio = 3

a4 = Lata()
a4.Peso = 11
a4.Beneficio = 15


a5 = Lata()
a5.Beneficio = 9
a5.Peso = 10

a6 = Lata()
a6.Beneficio = 4
a6.Peso = 4

latas[0] = a1
latas[1] = a2
latas[2] = a3
latas[3] = a4
latas[4] = a5
latas[5] = a6


#PARTE 3 DIVIDE AND CONQUER
print("PARTE 3 DIVIDE AND CONQUER")

LordenadaBusqueda = LinkedList()
add(LordenadaBusqueda,31)
add(LordenadaBusqueda,26)
add(LordenadaBusqueda,15)
add(LordenadaBusqueda,12)
add(LordenadaBusqueda,9)
add(LordenadaBusqueda,8)
add(LordenadaBusqueda,8)
add(LordenadaBusqueda,3)
add(LordenadaBusqueda,0)
add(LordenadaBusqueda,-2)
add(LordenadaBusqueda,-5)

print(busquedaBinaria(LordenadaBusqueda, 9))

Lmenorposition = LinkedList()
add(Lmenorposition,66)
add(Lmenorposition,77)
add(Lmenorposition,33)
add(Lmenorposition,11)
add(Lmenorposition,44)
add(Lmenorposition,66)
add(Lmenorposition,22)
add(Lmenorposition,88)
add(Lmenorposition,55)

print(busquedaKesimo(Lmenorposition,3))

imprimirlista(subsecuenciaCreciente_DnC(A3))
print("Ejercicio 4 Divide and Conquer")
print(distancia("perro","perrito"))

##################### PROGRAMACION DINAMICA #################
print("PARTE 4 PROGRAMACION DINAMICA")
Arry = Array(3,0)
Arry[0] = 1
Arry[1] = 4
Arry[2] = 6
print("El minimo de monedas es ", darCambioPD(8,Arry))

Arry2 = Array(4,"")
Arry2[0] = "1"
Arry2[1] = "2"
Arry2[2] = "3"
Arry2[3] = "5"
print("El conjunto de latas final es ", varianteMochila(Arry2,10))

Arry3 = Array(5,Array(5,0))

Arry3[0][0] = 1
Arry3[0][1] = 15
Arry3[0][2] = 5
Arry3[0][3] = 2
Arry3[0][4] = 3

Arry3[1][0] = 32
Arry3[1][1] = 9
Arry3[1][2] = 3
Arry3[1][3] = 4
Arry3[1][4] = 7

Arry3[2][0] = 5
Arry3[2][1] = 7
Arry3[2][2] = 19
Arry3[2][3] = 6
Arry3[2][4] = 4

Arry3[3][0] = 1
Arry3[3][1] = 4
Arry3[3][2] = 12
Arry3[3][3] = 11
Arry3[3][4] = 12

Arry3[4][0] = 53
Arry3[4][1] = 10
Arry3[4][2] = 33
Arry3[4][3] = 17
Arry3[4][4] = 32
Imprimirmatriz(Arry3)
print( "El camino hasta [n,n] es ", pathInTable(Arry3))  



print("La LCS mas larga es ",LCS("aggtab","gxtxayb"))