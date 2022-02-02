## Inserzione in lista
# Definire una funzione inserisci(L, n1, n2) : data una lista di interi L, ,
# e due interi n1 e n2, la funzione restituisce una nuova lista ottenuta da L
# dove il valore n2 viene inserito subito dopo ogni occorrenza del valore n1.
#
# Esempio: inserisci([3, 12, 4, 3, 10, 3], 3, 0) produce come risultato la 
# lista [3, 0, 12, 4, 3, 0, 10, 3, 0].

def inserisci(L, n1, n2):
# @param L: list of int
# @param n1: int
# @param n2: int
# @return list
    newL = []
    for num in L:
        newL.append(num)
        if num == n1:
            newL.append(n2)
    return newL


## Matrici 1
# Definire la seguente funzione croce(A, i, j) : data una matrice A mxn (m righe, n colonne), 
# contenente valori numerici, e una coppia di indici (i,j), la funzione restituisce vero se 
# l'elemento di A in posizione (i,j) e' maggiore di tutti gli elementi immediatamente 
# adiacenti ad esso nella riga i e nella colonna j, falso altrimenti. Si presti attenzione 
# nella soluzione ai casi particolari di vicinanza ai "bordi" della matrice.
# Esempio: data la seguente matrice A 3x4:
#
# 1  2  3  10
#
# 3  5  7  2 
#
# 4  9  2  5 
#
# la chiamata croce(A,0,0) restituisce falso (sulla riga: 1<2; sulla colonna:  1<3)
# la chiamata croce(A,1,2) restituisce vero (sulla riga: 7>5 e 7>2; sulla colonna: 7>3 e 7>2)
# la chiamata croce(A,2,1) restituisce vero (sulla riga: 9>4 e 9>2; sulla colonna:  9>5)
# la chiamata croce(A,0,2) restituisce falso (sulla riga: 3>2 e 3<10; sulla colonna: 3<7)

def croce(A, i, j):
# @param A: matrix of int
# @param i: int; index of row
# @param j: int; index of column
# @param bool
    row = A[i]
    column = matrix_col_to_vect(A, j)
    return checkAdjacent(row, j) and checkAdjacent(column, i)

def checkAdjacent(vect, i):
# @param vect: list of int
# @param i: int; index of element in list
# @return bool
    a = i-1
    b = i+1
    if a >= 0 and b < len(vect):       
        return vect[i] > vect[a] and vect[i] > vect[b]
    elif a < 0 and b < len(vect):       
        return  vect[i] > vect[b]
    elif a >= 0 and b >= len(vect):       
        return vect[i] > vect[a]
    else: #se il vettore e' composto solo da un elemento
        return True
        

def matrix_col_to_vect(mat, j):
# @param mat: matrix
# @param j: int
# @return list
    v = []
    for i in range(0,len(mat)):
        v = v + [mat[i][j]]
    return v


## Matrici 2
# Ancora due problemi, per non restare inattivi :-)
#
# 1) Scrivere una funzione che, data un'immagine quadrata, e un intero x, modifica 
# l'immagine scambiando tra loro la riga numero x e la colonna numero x (in altre parole, 
# il colore dei pixel della riga x deve essere attribuito, nell'ordine, ai pixel 
# della colonna x, e viceversa). La funzione deve includere un controllo iniziale 
# sulla correttezza dell'input fornito. In caso di input scorretto, l'immagine deve 
# restare invariata;
#
# 2) Come il problema 1, ma immaginando di avere come input una matrice di valori 
# numerici interi, rappresentata come visto a lezione (lista di liste, dove ogni 
# sottolista rappresenta una riga della matrice).

## 1)
def isSquarePic(pict):
# @param pict: Picture
# @return bool
    return getWidth(pict) == getHeight(pict)   

def getRowPixels(pict, width, y):
# @param pict: Picture
# @param width: int
# @param y: int; indice di riga
# @return list of Pixels
        rowColor = []
        for x in range(width):
            px = getPixel(pict, x, y)
            rowColor.append(getColor(px))
        return rowColor

def getColPixels(pict, height, x):
# @param pict: Picture
# @param height: int
# @param x: int; indice di colonna
# @return list of Pixels
        colColor = []
        for y in range(height):
            px = getPixel(pict, x, y)
            colColor.append(getColor(px))
        return colColor

def swapRowColPic(pict, k):
# @param pict: Picture; imagine quadrata
# @param k: int; indice della riga/colonna
    width = getWidth(pict)
    height = getHeight(pict)
    if isSquarePic(pict) and k >= 0 and k < width:    # controllo correttezza dei parametri        
        
        rowColor = getRowPixels(pict, width, k)  # prelevo i colori dei pixel della riga k          
        colColor = getColPixels(pict, height, k)  # prelevo i colori dei pixel della colonna k
        
        # assegno ai pixel della riga k i colori dei pixel della colonna k
        for x in range(width):
            px = getPixel(pict, x, k)
            setColor(px, colColor[x])
        # assegno ai pixel della colonna k i colori dei pixel della riga k
        for y in range(height):
            px = getPixel(pict, k, y)
            setColor(px, rowColor[y])
        
        repaint(pict)
    else:
        print "parametri non adeguati"
        
## 2)
def isSquareMat(mat):
# @param mat: matrix
# @return bool
    return len(mat) == len(mat[0]) 

def getRowMat(mat, width, i):
# @param mat: matrix
# @param width: int
# @param i: int; indice di riga
# @return list of int
        rowList = []
        for j in range(width):
            rowList.append(mat[i][j])
        return rowList

def getColMat(mat, height, j):
# @param mat: matrix
# @param height: int
# @param j: int; indice di colonna
# @return list of int
        colList = []
        for i in range(height):
            colList.append(mat[i][j])
        return colList

def swapRowColMat(mat, k):
# @param mat: matrix
# @param k: int; indice della riga/colonna
    width = len(mat)
    if isSquareMat(mat) and k >= 0 and k < width:    # controllo correttezza dei parametri
        
        rowList = getRowMat(mat, width, k)  # prelevo gli elementi della riga k            
        colList = getColMat(mat, width, k)  # prelevo gli elementi della colonna k
        
        # assegno alla riga k la colonna k
        for j in range(width):
            mat[k][j] = colList[j]
        # assegno alla colonna k la riga k
        for i in range(width):
            mat[i][k] = rowList[i]