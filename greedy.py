from linkedlist import *
from algo1 import *
from doublelinkedlist import *

#Ejercicio 5
class Tarea:
    Nombre = None
    Tinit = None
    Tfin = None
    Done = None

def adminActividades(tareas, inicio, fin): 
    L = LinkedList()
    busy = False
    while inicio != fin:
        if busy == True:
            if tarea != None:
                if tarea.Tfin == inicio:
                    busy = False
                else:
                    inicio = inicio + 1 
                    continue
        tarea = buscarTarea(tareas,inicio)
        if tarea != None:
            busy = True
            add(L,tarea)
        inicio = inicio + 1 
    return L
def buscarTarea(tareas,inicio):
    currentnode = tareas.head
    tarea = makeTarea("TareaMock",0,2147483647,False)
    tUse = 0
    while currentnode != None:
        if currentnode.value.Tinit == inicio and currentnode.value.Done != True:
            if currentnode.value.Tfin < tarea.Tfin:
                tarea = currentnode.value
        currentnode = currentnode.nextNode
    if tarea.Nombre == "TareaMock":
        return None
    else:
        tarea.Done = True
        return tarea

def makeTarea(Nombre,Tinit, Tfin, Done):
    T = Tarea()
    T.Nombre = Nombre
    T.Tinit = Tinit
    T.Tfin = Tfin
    T.Done = Done
    return T

#Ejercicio 6
def buscaPares(vector): 
    DL = DoubleLinkedList()
    maximum = None
    for i in range(len(vector)):
        D_add(DL,vector[i])
    for n in range(len(vector)//2):
        maximal = resolveMax(DL)
        if n == 0:
            maximum = maximal
        else:
            if maximum < maximal:
                maximum = maximal
    return maximum


def resolveMax(Numbers):
    if Numbers.head == None:
        return None
    currentnode = Numbers.head
    maximum = currentnode.value
    maximumNode = currentnode
    minimum = currentnode.value
    minimumNode = currentnode
    currentnode = currentnode.nextNode
    while currentnode != None:
        if currentnode.value > maximum:
            maximum = currentnode.value
            maximumNode = currentnode
        if currentnode.value < minimum:
            minimum = currentnode.value
            minimumNode = currentnode
        currentnode = currentnode.nextNode
    suma = maximumNode.value + minimumNode.value
    D_deleteNode(Numbers,maximumNode)
    D_deleteNode(Numbers,minimumNode)
    return suma

class Lata:
    Beneficio = None
    Peso = None

def mochila_bene(PesoMax, latas):
    DL = DoubleLinkedList()
    L = LinkedList
    peso = 0
    for n in range(len(latas)):
        D_add(DL,latas[n])
    for i in range(len(latas)):
        lata = buscarLata(DL)
        if lata != None and lata.Peso + peso <= PesoMax :
            peso = peso + lata.Peso
            add(L,lata)
    return L
 
def buscarLata(latas):
    currentnode = latas.head
    lata = makeLata(0,2147483647)
    lataNode = None
    while currentnode != None:
        if currentnode.value.Beneficio > lata.Beneficio:
            lata = currentnode.value
            lataNode = currentnode
        currentnode = currentnode.nextNode
    if latas != None:
        D_deleteNode(latas,lataNode)
    return lata

def makeLata(Beneficio,Peso):
    lata = Lata()
    lata.Beneficio = Beneficio
    lata.Peso = Peso
    return lata