from algo1 import *
from linkedlist import *
from diccionary import *

def busquedaBinaria(lista, x): 
    currentnode = lista.head
    A = Array(length(lista),0)
    cont = 0
    while currentnode != None:
        A[cont] = currentnode.value
        currentnode = currentnode.nextNode
        cont = cont + 1
    i = 0
    pivote = len(A) // 2
    j = len(A) - 1
    flag = True
    while flag == True:
        if j == pivote or i == pivote or A[pivote] == x:
            return True
        if A[pivote] >  x:
            j = pivote - 1
            pivote = i + (j - i)//2
        if A[pivote] <  x: 
            i = pivote + 1
            pivote = i + (j - i)//2
    return False

def busquedaKesimo(lista, k):
    large = length(lista)
    busquedaKesimoWrapped(lista,0,large - 1,k-1)
    return access(lista,k-1)

def busquedaKesimoWrapped(L,inicio,fin,position):
    if inicio > fin:
        return
    pivote = accesposition(L,(fin + inicio)//2) #Busco el pivote entre 3 opciones
    initnode = accesposition(L,inicio)
    pivotevalue = pivote.value #Me guardo el value del pivote para el proximo switch
    switchvalues(initnode,pivote) #cambio el valor del pivote
    delimitador = initnode #Inicio un puntero que va avanzando para ordenar la lista con los menores a la izquierda
    currentnode = initnode
    inicioposicion = inicio
    for n in range(inicio, fin + 1):
        if currentnode.value < pivotevalue:
            delimitador = delimitador.nextNode #avanzo el delimitador para cambiarlo
            switchvalues(delimitador,currentnode)
            inicioposicion = inicioposicion +1
        currentnode = currentnode.nextNode
    switchvalues(initnode,delimitador)
    if position <= inicioposicion:   
        busquedaKesimoWrapped(L,inicio, inicioposicion-1,position)
    if position > inicioposicion:
        busquedaKesimoWrapped(L,inicioposicion+1,fin,position)
def switchvalues(nodeA,nodeB):
    value1 = nodeA.value
    value2 = nodeB.value
    nodeA.value = value2
    nodeB.value = value1
    #Obtiene el pivote de la lista comparando el inicio, el fin y la mitad


def subsecuenciaCreciente_DnC(numeros):
    L = LinkedList()
    for n in range(len(numeros)):
        add(L,numeros[n])
    return subsecuenciaCreciente_DnCWrapped(L)
def subsecuenciaCreciente_DnCWrapped(L):
    large = length(L)
    if large == 1 or large == 2:
        if large == 2:
            if isSubCreciente(L) == True:
                return L
            else:
                return getMinor(L)
        else:
            return L
    mid = int(large/2)
    Le = LinkedList() #Creo la lista izquierda
    currentnode = L.head
    for n in range(0,mid): #Paso los elementos hasta la mitad
        add(Le,currentnode.value)
        currentnode = currentnode.nextNode
    Le = inverse(Le)
    R = LinkedList() #Creo la lista derecha
    for u in range(mid+1,large +1 ): #Lo mismo
        add(R,currentnode.value)
        currentnode = currentnode.nextNode
    R = inverse(R)
    Left = subsecuenciaCreciente_DnCWrapped(Le) #Llamo a la recursividad del lado izquierdo y lo guardo
    Right = subsecuenciaCreciente_DnCWrapped(R) #LLamo a la recursividad del lado derecho y lo guardo
    return gitmerge(Left,Right) #Merge a los resultados
#Funcion que mergea 2 listas en 1  y los ordena

def gitmerge(L,R):
    Lfinal = LinkedList()
    largeL = length(L)
    largeR = length(R)
    i = j = 0
    nodeleft = L.head
    noderight = R.head
    lastNodeLeft = accesposition(L,largeL-1)
    if lastNodeLeft.value < R.head.value:
        lastNodeLeft.nextNode = R.head
        return L
    else:
        if largeL == 1:
            return R
        nodeL = accesposition(L,largeL-2)
        cont = 2
        while nodeL != L.head:
            if nodeL.value < R.head.value:
                nodeL.nextNode = R.head
                return L
            else:
                cont = cont + 1
                nodeL = accesposition(L,largeL-cont)
def isSubCreciente(L):
    currentnode = L.head
    if length(L) == 1:
        return True
    while currentnode.nextNode != None:
        if currentnode.value > currentnode.nextNode.value:
            return False
        currentnode = currentnode.nextNode
    return True

def getMinor(L):
    currentnode = L.head
    Lminor = LinkedList()
    if currentnode.value > currentnode.nextNode.value:
        add(Lminor, currentnode.nextNode.value)
    else:
        add(Lminor, currentnode.value)
    return Lminor

#Ejercicio 4
class CharWithPos:
    char = None
    position = None


def distancia(string1, string2): 
    string1 = String(string1)
    string2 = String(string2)
    largo1 = len(string1)
    largo2 = len(string2)
    dist = 0
    String1List= LinkedList()
    for n in range(len(string1)-1,-1,-1):
        char = CharWithPos()
        char.char = string1[n]
        char.position = n
        add(String1List,char)

    String2List= LinkedList()
    for i in range(len(string2)-1,-1,-1):
        char = CharWithPos()
        char.char = string2[i]
        char.position = i
        add(String2List,char)    

    if largo1 > largo2:
        L = charsUsed(String1List,String2List)
        corto = string2
    else:
        L = charsUsed(String2List,String1List)
        corto = string1

    definitive = Array(len(corto),"")
    currentNode = L.head
    while currentNode != None:
        if currentNode.value.position < len(corto) -1:
            if corto[currentNode.value.position] == currentNode.value.char:
                definitive[currentNode.value.position] = currentNode.value.char
        currentNode = currentNode.nextNode
        
    for i in range(len(definitive)):
        if definitive[i] == None:
            dist = dist + 1

    return dist
    

def extractCharsUsed(stringLarge, stringShort):
    L = LinkedList()
    D = Array(127,Diccionary())
    cantidadDeExistencias = 0
    currentNode = stringLarge.head
    while currentNode != None:
        dic_insert(D,ord(currentNode.value.char),currentNode.value,ord(currentNode.value.char))
        currentNode = currentNode.nextNode
    currentNode = stringShort.head
    while currentNode != None:
        if D[ord(currentNode.value.char)] != None:
            cantidadDeExistencias = cantidadDeExistencias + 1
            add(L,D[ord(currentNode.value.char)].head.value)
        dic_insert(D,ord(currentNode.value.char),currentNode.value,ord(currentNode.value.char))
        
        currentNode = currentNode.nextNode
    if cantidadDeExistencias == length(stringLarge):
        return L
    else: 
        return None

def charsUsed(stringLarge, stringShort):
    if stringLarge == None:
        return None
    large = length(stringLarge)
    L = extractCharsUsed(stringLarge,stringShort)
    if L != None: #Recursividad principal
        return L
    if stringLarge.head.nextNode == None: #Si el valor esta solo
        return None
    mid = int(large/2)
    Le = LinkedList() #Creo la lista izquierda
    currentnode = stringLarge.head
    for n in range(0,mid): #Paso los elementos hasta la mitad
        add(Le,currentnode.value)
        currentnode = currentnode.nextNode
    Le = inverse(Le)
    R = LinkedList() #Creo la lista derecha
    for u in range(mid+1,large +1 ): #Lo mismo
        add(R,currentnode.value)
        currentnode = currentnode.nextNode
    R = inverse(R)
    Left = charsUsed(Le, stringShort) #Llamo a la recursividad del lado izquierdo y lo guardo
    Right = charsUsed(R, stringShort) #LLamo a la recursividad del lado derecho y lo guardo
    return gitmergeChars(Left,Right)

def gitmergeChars(L,R):
    Lfinal = LinkedList()
    if L != None and R != None: 
        largeL = length(L)
        nodeleft = L.head
        lastNodeLeft = accesposition(L,largeL-1)
        lastNodeLeft.nextNode = R.head
        return L
    else:
        if R != None:
            return R
        if L != None:
            return L
