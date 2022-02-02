#  1) Pensate ci siano errori sintattici  o semantici nel seguente comando?

# _________________________________________________________________________ 
#    print "Il logaritmo di 1,5 e' ", log(1,5)
# _________________________________________________________________________ 

print "Il logaritmo di 1,5 e' ", log(1.5)

#  2) Fate "copia-e-incolla" (nella Program Area di JES) della seguente 
#  funzione Python, salvatela e provate a caricarla (Load Program) ed 
#  eseguirla; se vi verranno segnalati errori, cercate di correggerli:

# _________________________________________________________________________ 
#    def foo(x,y)
#    a = x + sqrt(y)
#    b = 2.0**a * log(y+3,5*z*x,2)
#    print a + b.
# _________________________________________________________________________  

def foo(x,y):
    a = x + sqrt(y)
    b = 2.0**a * log(y+3) * log(5*y*x) * log(2)
    print a + b
