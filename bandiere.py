# Risolvere il problema delle "bandiere" presentato a lezione (Slides_13_a), 
# utilizzando oggetti di tipo Turtle.

def main():
## funzione principale del programma
    earth = makeWorld(400, 400)  # creo oggetto World
    turtle = makeTurtle(earth)   # creo oggetto Turtle
    #turtle.turnRight()           # oriento turtle inizialmente verso destra
    #turtle.penUp()               # disabilito l'attributo pen (quello che permette di disegnare)
    #turtle.backward(300)         # sposto indietro turtle (verso sinistra)
    #turtle.penDown()             # riabilito l'attributo pen (quello che permette di disegnare)
    #flag = input("di quale paese vuoi disegnare la bandiera: ")
    flag = 'ITA'
    drawFlag(earth, turtle, 100, 60, flag)

def drawFlag(earth, turtle, width, height, flag):
# @param earth: World 
# @param turtle: Turtle: the turtle to operate on
# @param width: int
# @param height: int
# @param flag: string
# @return None
    listOfFlag = ['ITA', 'FRA']
    assert(flag in listOfFlag), "la bandiera del paese richiesto non e' disponibile"
    startX = getXPos(turtle)
    startY = getYPos(turtle)
    
    band = width/3
    
    greenITA = makeColor(0, 153, 0)
    turtle.setColor(greenITA)
    for x in range(startX, band + startX):
        for y in range(startY, height + startY):
            turtle.moveTo(x,y)
    turtle.moveTo(x+1,y)
    
    turtle.setColor(white)
    for x in range(band + startX, 2*band + startX):
        for y in range(startY, height + startY):
            turtle.moveTo(x,y)
    turtle.moveTo(x+1,y)
    
    redITA = makeColor(204, 0, 0)
    turtle.setColor(redITA)
    for x in range(2*band + startX, 3*band + startX):
        for y in range(startY, height + startY):
            turtle.moveTo(x,y)
    turtle.moveTo(x+1,y)
   
    
    
    
main()   