from algo1 import *
from linkedlist import *

def darCambioPD(Cambio, Monedas):
    M = Array(len(Monedas),Array(Cambio + 1,0))
    for n in range(Cambio + 1):
        M[0][n] = n
    for i in range(1,len(Monedas)):
        for j in range(Cambio + 1):
            if j == Monedas[i]:
                M[i][j] = 1
            if j < Monedas[i]:
                M[i][j] = M[i-1][j]
            else:
                if (M[i][j - Monedas[i]] + 1) < M[i-1][j]:
                    M[i][j] = M[i][j - Monedas[i]] + 1
                else:
                    M[i][j] = M[i-1][j]
    return M[len(Monedas)-1][Cambio]


def varianteMochila(numeros,k):
    M = Array(len(numeros),Array(k + 1,String("")))
    for i in range(len(numeros)):
        for j in range(k + 1):
            if j == int(numeros[i]):
                M[i][j] = String(numeros[i])
            if j <= int(numeros[i]):
                if M[i-1][j] != None:
                    M[i][j] = M[i-1][j]
            else:
                if i == 0:
                    continue
                if M[i][j - int(numeros[i])] != None:
                    if existChar(M[i][j - int(numeros[i])],numeros[i]) == False:
                        M[i][j] = concat(M[i][j - int(numeros[i])],String(numeros[i]))
    stringFinal = M[len(numeros)-1][k]
    resultados = Array(len(stringFinal),0)
    for k in range(len(stringFinal)):
        resultados[k] = int(stringFinal[k])
    return resultados


def existChar(stri, c):
    stri = String(stri)
    for n in range(len(stri)):
        if stri[n] == c:
            return True
    return False

def Imprimirmatriz(A):
    sizerows = len(A)
    sizecolumns = len(A[0])
    for i in range(sizerows):
        for j in range(sizecolumns):
            if A[i][j] != None:
                print(A[i][j],end=" ")
            else:
                print(A[i][j],end=" ")
        print("")
    print("\n\n\n")


def pathInTable(Table):
    i = j = 0
    L = LinkedList()
    sumando = Table[0][0]
    add(L,str(i)+"-"+str(j))
            
    while i != len(Table)-1 or j != len(Table)-1:
        if i != len(Table)-1 and j != len(Table)-1:
            if Table[i + 1][j] < Table[i][j + 1]:
                i = i + 1
                add(L,str(i)+"-"+str(j))
                sumando = sumando + Table[i][j]
            else:
                j = j + 1
                add(L,str(i)+"-"+str(j))
                sumando = sumando + Table[i][j]
        else:
            if i == len(Table)-1 and j != len(Table)-1:
                j = j + 1
                add(L,str(i)+"-"+str(j))
                sumando = sumando + Table[i][j]
            else:
                if i != len(Table)-1 and j == len(Table)-1:
                    i = i + 1
                    add(L,str(i)+"-"+str(j))
                    sumando = sumando + Table[i][j]
    L = inverse(L)    
    return sumando


def LCS(string1, string2):
    string1 = String(string1)
    string2 = String(string2)
    M = Array(len(string2) + 1,Array(len(string1) + 1,0))
    contString1 = 0
    contString2 = 0
    for n in range(len(string1)+ 1):
        M[0][n] = 0
    for u in range(len(string2) + 1):
        M[u][0] = 0
    for i in range(1,len(string2) + 1):
        for j in range(1,len(string1) + 1):
            if string1[contString1] == string2[contString2]:
                M[i][j] = M[i-1][j-1] + 1
            else:
                M[i][j] = maximum(M[i][j-1],M[i-1][j])
            contString1 = contString1 + 1
        contString2 = contString2 + 1
        contString1 = 0
    return M[len(string2)][len(string1)]

def maximum(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2
