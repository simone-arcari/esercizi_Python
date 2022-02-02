## Sostituzione caratteri
# Data una stringa s, scrivere una funzione che restituisce una nuova stringa ottenuta da s sostituendo TUTTE le 
# occorrenze ripetute di uno stesso carattere (escluso il carattere 'spazio') con il carattere '*', senza cambiare 
# pero' la prima occorrenza del carattere stesso. Ad esempio, presa in input la stringa "la mia casa bianca", la 
# funzione deve restituire "la mi* c*s* b**n**" (la sostituzione ha riguardato i caratteri 'a', 'i', 'c').

def replaceRepChar(str):
# @param str: string
# @return string
    firstChar = ''    # stringa che contiene i caratteri apparsi per la prima volta
    for index in range(0, len(str)):
        if str[index] in firstChar and str[index] != ' ':
            str = replaceChar(str, index, '*')
        else:
            firstChar = firstChar + str[index]
    return str

def replaceChar(str, index, c):
# @param str: string
# @param index: int
# @param c: char
# @return string
    return str[:(index)] + c + str[(index+1):]


## Stringhe palindrome
# Scrivere una funzione che verifica se una stringa e' palindroma (una stringa e' palindroma se risulta identica 
# sia leggendola da sinistra verso destra che viceversa. Ad esempio la parola 'ossesso' e' palindroma, cosi' come 
# anche la parola 'osso')

def checkPalin(str):
# @param str: string
# @return bool
    for index in range(0, len(str)/2):
        if not chekSymmetry(str , index):
            return False
    return True

def chekSymmetry(str, index):
# @param str: string
# @param index: int
# @return bool
    opposite = len(str) - index - 1
    return str[index] == str[opposite]


# 1) scrivere una funzione che, data una stringa s, restituisce una nuova stringa ottenuta eliminando da s tutti 
# i caratteri alfabetici (latini).
# Ricordare la presenza, tra gli operatori del tipo di dato string in Python, degli operatori isalpha() e isdigit().

def eliminaAlpha(str):
# @param str: string
# @return string
    newStr = ''
    for char in str:
        if not char.isalpha():
            newStr = newStr + char
    return newStr

def eliminaAlpha_2(str):
# @param str: string
# @return string
    newStr = ''
    while i < len(s):
        if not str[i].isalpha():
            newStr = newStr + str[i]
        i = i+1
    return newStr
    
    
# 2) scrivere una funzione che, data una stringa s, restituisce una nuova stringa ottenuta eliminando da s tutte 
# le cifre numeriche.
# Ricordare la presenza, tra gli operatori del tipo di dato string in Python, degli operatori isalpha() e isdigit().

def eliminaCifre(str):
# @param str: string
# @return string
    newStr = ''
    for char in str:
        if not char.isdigit():
            newStr = newStr + char
    return newStr

def eliminaCifre_2(str):
# @param str: string
# @return string
    newStr = ''
    while i < len(s):
        if not str[i].isdigit():
            newStr = newStr + str[i]
        i = i+1
    return newStr
    

# Il tipo di dato str (string) in Python mette a disposizioni funzioni come find (), rfind () 
# Ipotesi: immaginiamo di non disporre di queste funzioni. Scrivere funzioni Python che realizzano lo stesso 
# comportamento di find(), rfind()

def myFind(str, findStr):
# @param str: string
# @param findStr: string
    L = len(findStr)
    for index in range(0, len(s)-L+1):
        if s[i:i+L] == findstr:
            return i
    return -1

def myFind_2(str, findStr, start, end):
# @param str: string
# @param findStr: string
# @param start: int
# @param end: int
    L = len(findStr)
    for index in range(start, min(end, len(s))-L+1):
        if s[i:i+L] == findstr:
            return i
    return -1


def myRfind(str, findStr):
# @param str: string
# @param findStr: string
    L = len(findStr)
    for index in range(qualcosa come prima ma al contrario):
        if s[i:i+L] == findstr:
            return i
    return -1