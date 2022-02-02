#  2) Il vento continua a impazzare ... :-) . Chi ha scritto il codice seguente intendeva 
#  questa volta applicare e visualizzare il risultato del teorema di Pitagora per il calcolo 
#  dell'ipotenusa di un triangolo rettangolo. Provate anche qui a riordinare il codice in 
#  modo da ottenere il risultato desiderato (i comandi seguenti includono sia quelli utilizzati 
#  per la definizione della funzione pitagora() che quelli utilizzati per la sua chiamata, che 
#  vanno quindi opportunamente separati):

# ___________________________________________________________________________________________
#    ipo = sqrt(cat1+cat2)
#    a = 4
#    cat1 = cat1**2
#    def pitagora(cat1, cat2) :
#    # @param cat1 : float (primo cateto)
#    b = 3
#    print 'valore ipotenusa: ', ipo
#    print 'valore primo cateto: ', cat1
#    pitagora(a, b)
#    cat2 = cat2**2
#    print 'valore secondo cateto: ', cat2
#    # @param cat2 : float (secondo cateto)
# ___________________________________________________________________________________________

def pitagora(cat1, cat2) :
    # @param cat1 : float (primo cateto)
    # @param cat2 : float (secondo cateto)
    cat1 = cat1**2
    cat2 = cat2**2
    ipo = sqrt(cat1+cat2)
    print 'valore primo cateto: ', cat1
    print 'valore secondo cateto: ', cat2    
    print 'valore ipotenusa: ', ipo

a = 4
b = 3
pitagora(a, b)





