#  1) Chi ha scritto il codice seguente intendeva applicare  e visualizzare il risultato
#  della formula di conversione da gradi Celsius a gradi Fahrenheit (T_fah = T_cel*9/5+32).
#  Purtroppo, un improvviso colpo di vento ( :-) ) ha alterato l'ordine dei comandi.
#  Provate a riordinare il codice in modo da ottenere il risultato desiderato (i comandi 
#  seguenti includono sia quelli utilizzati per la definizione della funzione celsToFahr() 
#  che quelli utilizzati per la sua chiamata, che vanno quindi opportunamente separati).

#  Una volta riordinato il codice, provate (anche per l'esercizio seguente) a farlo eseguire 
#  dalla macchina JES-Python, per avere la verifica definitiva della correttezza del vostro 
#  operato, e anche per verificare la piena comprensione dei meccanismi di definizione e 
#  chiamata di funzioni:

# ___________________________________________________________________________________________
#    celsToFahr(c)
#    y = x+32
#    def celsToFahr(tempCels) :
#    print 'valore temperatura in gradi Fahrenheit: ', y
#    # @param tempCels: float (temperatura in gradi Celsius)
#    print 'valore temperatura in gradi Celsius: ', tempCels
#    c = 20
#    x = tempCels*9/5.0
# ___________________________________________________________________________________________

def celsToFahr(tempCels):
    # @param tempCels: float (temperatura in gradi Celsius)
    x = tempCels*9/5.0
    y = x+32
        
    print 'valore temperatura in gradi Celsius: ', tempCels
    print 'valore temperatura in gradi Fahrenheit: ', y

c = 20
celsToFahr(c)




