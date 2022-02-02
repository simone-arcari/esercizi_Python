def main():
## funzione principale del programma
    earth = makeWorld(800, 800)  # creo oggetto World
    turtle = makeTurtle(earth)   # creo oggetto Turtle
    turtle.turnRight()           # oriento turtle inizialmente verso destra
    turtle.penUp()               # disabilito l'attributo pen (quello che permette di disegnare)
    turtle.backward(300)         # sposto indietro turtle (verso sinistra)
    turtle.penDown()             # riabilito l'attributo pen (quello che permette di disegnare)
    turtleKochCurve(earth, turtle, 729) # disegna la curva di Koch


def turtleKochCurve(earth, turtle, n):
# @param earth: World 
# @param turtle: Turtle: the turtle to operate on
# @return None
    segment = n/3 # calcolo lunghezza segmento     
    if segment<=3:  # caso piu' semplice                             
        turtle.forward(segment)  # disegno primo segmento orizzontale
        turtle.turn(-60)         # ruoto di 60 gradi (senso antiorario)
        turtle.forward(segment)  # disegno segmento obliquo crescente 
        turtle.turn(120)         # ruoto di 120 gradi (senso orario)
        turtle.forward(segment)  # disegno segmento obliquo decrescente
        turtle.turn(-60)         # ruoto di 60 gradi (senso antiorario)
        turtle.forward(segment)  # disegno ultimo segmento orizzontale
    else:  # caso generale
        turtleKochCurve(earth, turtle, segment)  # disegno la curva di Koch nel primo segmento orizzontale
        turtle.turn(-60)                         # ruoto di 60 gradi (senso antiorario)
        turtleKochCurve(earth, turtle, segment)  # disegno la curva di Koch nel segmento obliquo crescente
        turtle.turn(120)                         # ruoto di 120 gradi (senso orario)
        turtleKochCurve(earth, turtle, segment)  # disegno la curva di Koch nel segmento obliquo decrescente
        turtle.turn(-60)                         # ruoto di 60 gradi (senso antiorario)
        turtleKochCurve(earth, turtle, segment)  # disegno la curva di Koch nell'ultimo segmento orizzontale

# inizio del programma
main()