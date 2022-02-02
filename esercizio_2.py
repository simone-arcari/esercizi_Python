# 1.a) scrivere una funzione che consenta di tracciare su un'immagine data una linea orizzontale di vario spessore e colore 
# (spessore e colore sono parametri della funzione);

def drawHorizontalLine(pict, position, lineWidth, color):
# @param pict: Picture
# @param position: int
# @param lineWidth: int
# @param color: Color
    for y in range(position, position + lineWidth):
        for x in range(0, getWidth(pict)):
            setColor(getPixel(pict, x, y), color)

                        
# 1.b) scrivere una funzione che consenta di tracciare su un'immagine data una linea verticale di vario spessore e colore 
# (spessore e colore sono parametri della funzione);

def drawVerticalLine(pict, position, lineWidth, color):
# @param pict: Picture
# @param position: int
# @param lineWidth: int
# @param color: Color
    for x in range(position, position + lineWidth):
        for y in range(0, getHeight(pict)):
            setColor(getPixel(pict, x, y), color)         


# 2.a) scrivere una funzione che consenta di effettuare il ribaltamento totale orizzontale (sull'asse orizzontale) di un'immagine;

def horizontalFlip(pict):
# @param pict: Picture
    offSet = 1
    width = getWidth(pict)
    height = getHeight(pict)
    for x in range(0, width):
        for y in range(0, height/2):
            topPix = getPixel(pict, x, y)
            bottomPix = getPixel(pict, x, height - y - offSet)
            
            topPixColor = getColor(topPix)
            bottomPixColor = getColor(bottomPix)
            
            setColor(topPix, bottomPixColor)
            setColor(bottomPix, topPixColor)
            

# 2.b) scrivere una funzione che consenta di effettuare il ribaltamento totale verticale (sull'asse verticale) di un'immagine.

def verticalFlip(pict):
# @param pict: Picture
    offSet = 1
    width = getWidth(pict)
    height = getHeight(pict)
    for x in range(0, width/2):
        for y in range(0, height):
            topPix = getPixel(pict, x, y)
            bottomPix = getPixel(pict, width - x - offSet, y)
            
            topPixColor = getColor(topPix)
            bottomPixColor = getColor(bottomPix)
            
            setColor(topPix, bottomPixColor)
            setColor(bottomPix, topPixColor)