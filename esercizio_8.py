##
# Per rompere il ghiccio, un paio di problemi da risolvere in modo ricorsivo,
# altri problemi possono essere trovati nei capitoli del testo di riferimento
# indicati a lezione:
#
# 1) scrivere una funzione ricorsiva booleana che, data una stringa s, una 
#    stringa c di lunghezza 1, e un intero n, restituisce il valore vero se 
#    c e' presente ALMENO n volte nella stringa s, falso altrimenti.
#
# 2) un numero naturale e' divisibile per 3 se la somma delle sue cifre (in 
#    base 10!) e' divisibile per 3. Usando questa proprieta', scrivere una 
#    funzione ricorsiva che stabilisce se un numero naturale dato e' 
#    divisibile per 3 (nota: non e' ovviamente consentito usare gli operatori 
#    di divisione o resto :-) )

####################################################

def checkStringRic(s, c, n):
# @param s: string
# @param c: string; formata da un solo carattere
# @param n: int
# @return bool
    assert len(c)==1, c + "non e' una stringa di un carattere" 
    if len(s)>0:
        if c == s[0]: 
            n=n-1
            if n==0:
                return True
        return checkStringRic(s[1:], c,n)     
    return False


####################################################

def divisibleByThree(n):
# verifica che n sia divisibile per 3
# @param n: int
# @return bool
    if n==0 or n==3 or n==6 or n==9:
        return True
    elif n >= 10:
        return divisibleByThree(digitSum(n))
    else:
        return False 

def digitSum(n):
# restituisce la somma delle cifre di n
# @param n: int
# @return int
    if n==0:
        return 0
    return digitSum(n // 10) + n%10


def digitSum2(n):
# non e' ricorsiva
# @param n: int
# @return int
    nStr = str(n)
    nSumDigit = 0
    for i in range(len(nStr)):
        nSumDigit = nSumDigit + int(nStr[i])
    return nSumDigit
    

##
# Ancora due problemi da risolvere in modo ricorsivo:
#
# Data una stringa s di qualunque lunghezza, scrivere una funzione ricorsiva 
# che:
#       1) restituisce il numero di cifre numeriche (eventualmente ripetute) 
#          presenti in s
#
#       oppure
#
#       2) restituisce una lista formata dalle singole cifre numeriche  
#          (eventualmente ripetute) presenti in s
#
# Esempi : s = 'h9u8j91'
# 1) restituisce : 4
# 2) restituisce : ['9', '8', '9', '1']

def countDigitInString(string):
# @param string: string
# @return int
    if len(string) > 0:
        if string[0].isdigit():
            return countDigitInString(string[1:]) + 1
        else:
            return countDigitInString(string[1:])
    return 0


def getDigitInString(string):
# @param string: string
# @return list of digit in string format
    list = []
    if len(string) > 0:
        if string[0].isdigit():
            list.append(string[0])
            return list + getDigitInString(string[1:])
        else:
            return getDigitInString(string[1:])
    return list


# 4) La seguente funzione intende verificare se la cifra 8 e' presente almeno 
# una volta in un numero n (rappresentato in base 10). Cosa c'e' di sbagliato 
# in questa funzione?

def ottoPresente(n):
# @param n : int
# @return bool
    ultimaCifra = n%10  # l'ultima cifra di n
    if n == 0:        ## ho aggiunto questo ora funziona   
        return False  ## ho aggiunto questo ora funziona 
    elif ultimaCifra == 8 :
        return True
    else:
        return ottoPresente(n//10)  # il parametro attuale rappresenta n senza l'ultima cifra