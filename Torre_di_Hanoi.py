# 1) 
# risolvere il problema delle torri di Hanoi (la soluzione deve stampare tutte
# le mosse da fare, p.es. "muovi un disco da A a C")

def hanoi(n,p1,p2,p3):
  # @param n : int
  # @param p1, p2, p3 : string 
  # @return int
  assert n>=1,"Numero dischi inserito non valido."
  if(n==1):
    print p1 ,"in", p3
    return 1
  else:
    c = 1 + hanoi(n-1,p1,p3,p2)
    print p1 ,"in", p3
    c = c + hanoi(n-1,p2,p1,p3)
    return c 

n=int(input("Inserisci numero dischi : "))
m=hanoi(n,"A","B","C")
print "Mosse :", m