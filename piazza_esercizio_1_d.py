#  Primo esercizio: sintassi e semantica
#  Un semplicissimo esercizio per iniziare a prendere familiarità con il linguaggio 
#  e la macchina Python, e con alcune delle relative problematiche.
#  Quando si scrive codice eseguibile usando un linguaggio di programmazione, si 
#  possono commettere due tipi di errori:

#  1) sintattici : violazione delle regole grammaticali del linguaggio;

#  2) semantici : mancanza di aderenza tra ciò che il codice avrebbe dovuto 
#  esprimere e ciò che effettivamente esprime (con conseguente comportamento 
#  della macchina diverso da quanto atteso).

#  Errori di tipo 1 vengono solitamente identificati e segnalati dalla macchina 
#  Python. Errori di tipo 2 a volte possono essere rilevati dalla macchina Python, 
#  ma molto più spesso non vengono rilevati, portando alla produzione di risultati 
#  sbagliati. Nel seguito vengono mostrate alcune righe di codice che contengono, 
#  rispettivamente, errori sintattici e semantici. Provate a individuarli PRIMA di 
#  eseguire il codice. Poi passate ad eseguirlo (usando l'ambiente JES), per 
#  verificare la correttezza delle vostre osservazioni.

 

#  1) Identificate gli errori sintattici nel seguente codice:
# ___________________________________________________________
#    num = 3
#    a = "bianco"
#    b = "nero"
#    print "Se unisco" a "e" b "ottengo il colore grigio"
#    print num per a "produce un bianco abbagliante :-) "
# ___________________________________________________________
 
num = 3
a = "bianco"
b = "nero"
print "Se unisco " + a + " e " + b + " ottengo il colore grigio"
print str(num) + "per" + a + "produce un bianco abbagliante :-) "

#  2) Identificate gli errori semantici nel seguente codice:
# ___________________________________________________________
#    x = 2
#    y = 4
#    print "Il prodotto di ", x, "e ", y, "e' ", x+y
#    print "La radice quadrata della loro differenza e' ", sqrt(x-y)
# ___________________________________________________________

x = 7
y = 4
print "Il prodotto di " + str(x)  + " e " + str(y) + " e' " +  str(x*y)
print "La radice quadrata della loro differenza e' " + str(sqrt(x-y))