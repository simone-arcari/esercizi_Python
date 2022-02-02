## FUNZIONI VARIE

def check_a_b(a, b, numRows):
# @param a: int, riga su cui eseguire l'operazione elementare
# @param b: int, riga su cui eseguire l'operazione elementare
# @param numRows: int; numero di righe
# @return bool
    return a < numRows and b < numRows and a != b
    
def check_i_j(i, j, numRows, numCols):
# @param i: int, indice di posizione di riga
# @param j: int, indice posizione colonna
# @param numRows: int; numero di righe
# @param numCols: int; numero di colonne
# @return bool
    return (i >= 0 and i < numRows) and (j >= 0 and j < numCols)


## CLASSE MATRICE

errMsg1 = "Errore: i dati in ingresso sono del tipo sbagliato"
errMsg2 = "Errore: il numero di righe e colonne non puo' essere negativo" 
errMsg3 = "Errore: gli indici forniti non sono accetabili"

class Matrix:
    
    ## COSTRUTTORE
    
    def __init__(self, m, n, valori = []):
    # @param m: int; numero di righe
    # @param n: int; numero di colonne
    # @param valori; lista sequenziale di valori
       
        
        assert type(m) == type(n) == type(1), errMsg1
        assert type(valori) == type([]), errMsg1
        assert m >= 0 and n >= 0, errMsg2
        
        # verifico e corrego la lista di valori
        lenght = len(valori)
        if lenght == 0:      
            valori = [0]*(m*n)
        elif lenght < m*n:
            valori = valori + [0]*(m*n - lenght) 
        
        # inizio costruzione matrice    
        self.mat = []
        k = 0    # indice per scorrere la lista di valori
        for i in range(m):    # scorro le righe
            self.mat.append([])
            for j in range(n):    # scorro le colonne
                self.mat[i].append(valori[k])
                k += 1
        
        self.rows = m
        self.columns = n
    
    
    ## OPERATORI 
    
    def printMat(self):
        for i in range(self.rows):
            print self.mat[i]    # stampo la riga i


    def p_ij(self, a, b):
    # @param a: int, riga da mettere alla posizione b
    # @param b: int, riga da mettere alla posizione a
        assert check_a_b(a, b, self.rows), errMsg3
        newMat = []
        for i in range(0, self.rows):
            if i != a and i != b:
                newMat.append(self.mat[i])
            elif i == a:
                newMat.append(self.mat[b])
            elif i == b:
                newMat.append(self.mat[a])
        self.mat = newMat
    
    
    def e_i(self, a, n):
    # @param a: int, riga su cui eseguire l'operazione elementare
    # @param n: int, coefficiente da moltiplicare alla riga a
        assert a >= 0 and a < self.rows, ErrMsg3
        newMat = []
        for i in range(0, self.rows):
            if i != a:
                newMat.append(self.mat[i])
            else:
                tempList = []
                for j in range(self.columns):
                    tempList.append(self.mat[a][j]*n)
                newMat.append(tempList)
        self.mat =  newMat


    def e_ij(self, a, b, n):
    # @param a: int, riga su cui eseguire l'operazione elementare
    # @param b: int, riga da moltiplicare per n per poi andare a eseguire l'operazione su a
    # @param n: int, coefficiente da moltiplicare alla riga b
        assert check_a_b(a, b, self.rows), errMsg3
        newMat = []
        for i in range(0, self.rows):
            if i != a:
                newMat.append(self.mat[i])
            else:
                tempList = []
                for j in range(0, self.columns):
                    tempList.append(self.mat[a][j]+(self.mat[b][j]*n))
                newMat.append(tempList)
        self.mat = newMat

    
    def checkMatrixLine(self, i, j):
    # @param i: int, riga da analizzare da 0 a x
    # @param j: int, indice della colonna a cui far arrivare il controllo
    # @return: bool, vero se ?? preceduto da tutti 0, falso altrimenti
        assert check_i_j(i, j, self.rows, self.columns), errMsg3
        if self.mat[i][j] != 0:
            for n in range(0, j):
                if self.mat[i][n] != 0:
                    return False
            return True
        else:
            return False
    
    
    def checkPivot(self, i, j):
    # @param i: int, colonna da controllare
    # @param j: int, riga da cui partire per poi andare a controllare la colonna
    # @return: bool, ritorna vero se la l'elemento alla posizione [i][j] e' un pivot, altrimenti falso
        assert check_i_j(i, j, self.rows, self.columns), errMsg3
        if self.mat[i][j] != 0:
            for m in range(i+1, self.rows):
                if self.mat[m][j] != 0:
                    return False
            for n in range(max(0, j-1)):
                if self.mat[i][n] != 0:
                    return False
            return True
        else:
            return False
    
    
    def reduceToZeroByOpEl(self, i, j):
    # @param i: int, coordinata della riga da cui partire a ridurre a 0 le righe sottostanti
    # @param j: int, coordinata della colonna che devo ridurre a scala
        assert check_i_j(i, j, self.rows, self.columns), errMsg3
        for m in range(i+1, self.rows):
            a = float(self.mat[m][j])
            b = float(self.mat[i][j])
            n = a/b*(-1.0)
            self.e_ij(m, i, n)


    def zeroLineCounter(self, i):
    # @param i: int, riga su cui contare quanti zeri ci sono prima di un numero
    # @return: int, numero di zeri contati
        count = 0
        for j in range(0, self.columns):
            if self.mat[i][j] == 0:
                count += 1
            else:
                return count
        return count
    
    # ordina una matrice (sposta le righe fra loro...)
    def orderMatrix(self):
        ordered = False        
        while not ordered:
            for i in range(self.rows):
                ordered = False
                if self.zeroLineCounter(i) > self.zeroLineCounter(min(self.rows-1, i+1)):
                    self.p_ij(i,i+1)
                    break
                ordered = True

    # rende a scala una matrice ordinata (eventuali righe nulle in fondo...)
    def ladderMatrix(self):
    # @return: list, matrice ridotta a scala
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                if self.mat[i][j] != 0 and not self.checkPivot(i, j): # Ho controllato che l'elemento della matrice non sia 0 e non sia un pivot
                    if self.checkMatrixLine(i, j): # Controllo che questo non sia preceduto da numeri, di modo che posso trasformarlo in un pivot
                        self.reduceToZeroByOpEl(i, j)


    #Rende a scala una matrice 
    def gaussAlg(self):
        self.orderMatrix()
        self.ladderMatrix()
        self.orderMatrix()


def esempio1():
    # Creo una matrice A 4x4
    m = 4
    n = 4    
    componenti = [1,1,1,1,1,1,1,2,0,0,0,1,3,3,3,4] # Lista sequenziale delle componenti della matrice
    A = Matrix(m, n, componenti)
    
    # Stampo la matrice A
    A.printMat()
    
    # Riduco a scala la matrice A
    A.gaussAlg()
    
    # Stampo la matrice A ridotta a scala per righe    
    print "\n\nMatrice a scala:"
    A.printMat()
    
    ## LA MATRICE 4x4 USATA IN QUESTO ESEMPIO E' LA STESSA DELL'ESERCIZIO DI PAGINA 18
    ## CAPITOLO 2(Matrici) DELLE DISPENSE DEL PROFESSORE VINCENZO DI GENNARO


def esempio2():
    # Creo una matrice A 3x3
    m = 3
    n = 3   
    componenti = [1,-1,0,0,1,-1,2,2,-4] # Lista sequenziale delle componenti della matrice
    A = Matrix(m, n, componenti)
    
    # Stampo la matrice A
    A.printMat()
    
    # Riduco a scala la matrice A
    A.gaussAlg()
    
    # Stampo la matrice A ridotta a scala per righe    
    print "\n\nMatrice a scala:"
    A.printMat()
    
    ## LA MATRICE 4x4 USATA IN QUESTO ESEMPIO E' LA STESSA DELL'ESERCIZIO DI PAGINA 18
    ## CAPITOLO 2(Matrici) DELLE DISPENSE DEL PROFESSORE VINCENZO DI GENNARO


def esempio3():
    # Creo una matrice A 5x4
    m = 5
    n = 4    
    componenti = [1,1,1,1,2,0,1,3,3,1,2,4,1,0,0,0,0,1,0,-2] # Lista sequenziale delle componenti della matrice
    A = Matrix(m, n, componenti)
    
    # Stampo la matrice A
    A.printMat()
    
    # Riduco a scala la matrice A
    A.gaussAlg()
    
    # Stampo la matrice A ridotta a scala per righe    
    print "\n\nMatrice a scala:"
    A.printMat()
    
    ## LA MATRICE 5x4 USATA IN QUESTO ESEMPIO E' LA STESSA DELL'ESERCIZIO DI PAGINA 18-19
    ## CAPITOLO 2(Matrici) DELLE DISPENSE DEL PROFESSORE VINCENZO DI GENNARO
    