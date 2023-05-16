
from linkedlist import *
from algo1 import *
from sort import *


def darCambio(Cambio, Monedas):

    MonedasList = LinkedList()
    for n in range(len(Monedas)):
        add(MonedasList,Monedas[n])
    MonedasList = MergeSort(MonedasList)
    MonedasList = inverse(MonedasList)
    currentnode = MonedasList.head
    L = LinkedList()
    Listamenor = darCambioWrapped(Cambio, 0, 0, L, currentnode)
    currentnode = currentnode.nextNode

    while currentnode != None:
        L = LinkedList()
        L = darCambioWrapped(Cambio, 0, 0, L, currentnode)
        if length(L) < length(Listamenor):
            Listamenor = L
        currentnode = currentnode.nextNode
    return Listamenor

def darCambioWrapped(Cambio, Cant, dineroTotal, L, node):
    if dineroTotal == Cambio:
        return L
    if node.value + dineroTotal <= Cambio:
        add(L,node.value)
        dineroTotal = dineroTotal + node.value
        Cant = Cant + 1
        return darCambioWrapped(Cambio, Cant, dineroTotal, L, node)
    else:
        return darCambioWrapped(Cambio, Cant, dineroTotal, L, node.nextNode)








def mochila(PesoMax, latas): 
    
    LatasList = LinkedList()
    for n in range(len(latas)):
        add(LatasList,latas[n])
    currentnode = LatasList.head

    Listamayor = LinkedList()
    add(Listamayor,currentnode.value)
    mochilaWrapped(PesoMax, duplicateList(LatasList,currentnode.value), currentnode.value, Listamayor)
    currentnode = currentnode.nextNode

    while currentnode != None:
        L = LinkedList()
        add(L,currentnode.value)
        mochilaWrapped(PesoMax, duplicateList(LatasList,currentnode.value), currentnode.value, L)
        if sumaPeso(L) > sumaPeso(Listamayor):
            Listamayor = L
        currentnode = currentnode.nextNode
    return Listamayor

def mochilaWrapped(PesoMax, Latas, pesoTotal, L):
    currentLata = Latas.head
    while currentLata != None:
        if currentLata.value + pesoTotal == PesoMax:
            add(L,currentLata.value)
            return
        if currentLata.value + pesoTotal < PesoMax:
            add(L,currentLata.value)
            pesoTotal = currentLata.value + pesoTotal
            return mochilaWrapped(PesoMax,duplicateList(Latas,currentLata.value),pesoTotal,L )
        else:
            currentLata = currentLata.nextNode

def duplicateList(L,banned):
    Ldupli = LinkedList()
    currentnode = L.head
    while currentnode != None:
        if currentnode.value != banned:
            add(Ldupli,currentnode.value)
        else:
            banned = None
        currentnode = currentnode.nextNode
    return Ldupli
def sumaPeso(L):
    currentnode = L.head
    total = 0
    while currentnode != None:
        total = total + currentnode.value
        currentnode = currentnode.nextNode
    return total

def subSecuenciaCreciente(numeros):
    Numbers = LinkedList()
    for n in range(len(numeros)):
        add(Numbers,numeros[n])
    currentnode = Numbers.head
    L = subSecuenciaCrecienteWrapped(Numbers,None)
    return L
def subSecuenciaCrecienteWrapped(Numbers,recursividad):

    definitiveList = LinkedList()
    currentnode = Numbers.head
    while currentnode != None:
        if length(Numbers) == 1:
            L = LinkedList()
            return L

        if recursividad == None: #Si estamos en el primer nivel del arbol de opciones
            L = LinkedList()
            NumbersCutted = cut2NewList(Numbers,currentnode, None)
            L = subSecuenciaCrecienteWrapped(NumbersCutted,currentnode.value) #Comienzo a recorrer el primer subArbol
        else:
            if currentnode.value > recursividad:
                NumbersCutted = cut2NewList(Numbers,currentnode,None)
                L = subSecuenciaCrecienteWrapped(NumbersCutted,currentnode.value) #Mas sub ARBOLES
            else:
                currentnode = currentnode.nextNode
                continue
        if L == None:
            currentnode = currentnode.nextNode
        else:
            add(L, currentnode.value)
            if definitiveList.head == None:
                definitiveList = L 
            else:
                if length(L) > length(definitiveList):
                    definitiveList = L
        currentnode = currentnode.nextNode
    return definitiveList

def cut2NewList(L, node, banned):
    newList = LinkedList()
    currentnode = L.head
    while currentnode != None:
        if currentnode.value == node.value:
            newList.head = currentnode
            return inverse(duplicateList(newList,banned))
        currentnode = currentnode.nextNode

def subconjuntoSuma(numeros, valor): 
    Numbers = LinkedList()
    for n in range(len(numeros)):
        add(Numbers,numeros[n])
    currentnode = Numbers.head
    L = subconjuntoSumaWrapped(Numbers,valor, 0,None,0)
    return L
def subconjuntoSumaWrapped(Numbers,valor,suma,recursividad,carryOver):

    currentnode = Numbers.head
    
    while currentnode != None:
        if length(Numbers) == 1:
            return currentnode.value

        if recursividad == None: #Si estamos en el primer nivel del arbol de opciones
            NumbersCutted = inverse(duplicateList(Numbers, currentnode.value))
            suma = suma + currentnode.value
            suma = subconjuntoSumaWrapped(NumbersCutted,valor,suma,currentnode.value,carryOver) #Comienzo a recorrer el primer subArbol
            if suma == True:
                return True
        else:
            if currentnode.value + suma == valor:
                return True
            if currentnode.value + suma < valor :
                carryOver = suma
                suma = suma + currentnode.value
                NumbersCutted = inverse(duplicateList(Numbers, currentnode.value))
                suma = subconjuntoSumaWrapped(NumbersCutted,valor,suma,currentnode.value,carryOver) #Mas sub ARBOLES
                if suma == True:
                    return True
                currentnode = currentnode.nextNode
            else:
                currentnode = currentnode.nextNode
    return carryOver

