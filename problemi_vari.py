## Problema 1: 
# Disegnare un rettangolo "pieno" a partire da una punto (x,y).

def drawFilledRect(pict, x, y, w, h, color):
# @param pict: Picture
# @param x: int
# @param y: int
# @param w: int; width of rectangle
# @param h: int; height of rectangle
# @param color: Color; 
    for i in range(x, min(w+x, getWidth(pict))):
        for j in range(y, min(h+y, getHeight(pict))):
            pix = getPixel(pict, i,j)
            setColor(pix, color)

# SOLUZIONE TUTOR
def squarePic(pic, startX, startY, width, height, color):
    if startX+width >= getWidth(pic) or startY+height >= getHeight(pic):
        return    
    for x in range(startX, startX+width):
        for y in range(startY, startY+height):
            setColor(getPixel(pic, x,y), color)
    repaint(pic)



## Problema 2: 
# Scrivere una o piu' funzioni Python che, data un'immagine A, realizza lo zoom digitale di
# A a partire dalla posizione (x,y) di un generico fattore F di ingrandimento, lasciando inalterate le
# dimensioni dell'immagine ottenuta, rispetto a quella di partenza.

def zoom(pict, x, y, F):
# @param pict: Picture
# @param x: int
# @param y: int
# @param F: int; fattore di scala
# @return Picture
    targetY = 0
    targetX = 0
    width = getWidth(pict)
    height = getHeight(pict)
    canvas = makeEmptyPicture(width, height)   
    for i in range(x, x + (width/F) ):
        for j in range(y, y + (height/F) ):
            pix = getPixel(pict, i, j)
            color = getColor(pix)            
            redrawPix(canvas, targetX, targetY, F, color )
            targetY =  targetY + F
        targetX =  targetX + F
        targetY = 0
    return canvas

def redrawPix(canvas, x, y, F, color ):
# @param canvas: Picture
# @param x: int
# @param y: int
# @param F: int; fattore di scala
# @param color: Color
    w = getWidth(canvas)/F
    h = getHeight(canvas)/F
    drawFilledRect(canvas, x, y, w, h, color)


## Problema 3: 
# Scrivere una o piu' funzioni Python che, data un'immagine A, ruota A di x gradi (a destra
# o a sinistra), per qualunque x.

def rotate(pict, alpha):
# @param pict: Picture
# @param alpha: int; gradi di rotazione
# return Picture
    rad = -alpha * pi / 180
    width = getWidth(pict)
    height = getHeight(pict)
    centerW = width/2
    centerH = height/2
    diagonal = int(sqrt(width**2 + height**2))
    #canvas = makeEmptyPicture(diagonal, diagonal)
    canvas = makeEmptyPicture(500,500)
    for x1 in range(0, width):
        for x2 in range(0, height):
            pix = getPixel(pict, x1, x2)
            color = getColor(pix)
            
            y1 = x1*cos(rad) - x2*sin(rad) + 200
            y2 = x1*sin(rad) + x2*cos(rad) + 200                               
            
            newPix = getPixel(canvas, int(round(y1)), int(round(y2)))
            setColor(newPix, color)
    return canvas      

# SOLUZIONE TUTOR
def rotate_tutor(pic, degAngle):
    # @param pic: Picture
    # @param deg Angle: float; The rotation angle expressed in DEG
    # @return Picture; The rotated picture
    
    angle = (degAngle*pi)/180
    width = getWidth(pic)
    height = getHeight(pic)
    picXCenter = width/2
    picYCenter = height/2
    
    canvDim = int(sqrt(width**2 + height**2))
    canvas = makeEmptyPicture(canvDim, canvDim)
    startXY = canvDim/2
    
    for x in range(width):
        for y in range(height):
            color = getColor(getPixel(pic, x, y))
            
            newX = startXY + int( (x - picXCenter)*cos(angle) - (y - picYCenter)*sin(angle) )
            newY = startXY + int( (x - picXCenter)*sin(angle) + (y - picYCenter)*cos(angle) )
            setColor(getPixel(canvas, newX, newY), color)
    repaint(canvas)
    return canvas

def antiAlias(pic):
    # @param pict: Picture
    # @return Picture; The picture with the anti-aliasing
    for x in range(getWidth(pic)-1):
        for y in range(getHeight(pic)):
            currentColor = getColor(getPixel(pic, x, y))
            rightColor = getColor(getPixel(pic, x+1, y))
            
            if currentColor == white:
                if rightColor != white:
                    setColor(getPixel(pic, x, y), rightColor)
    repaint(pic)



def rotate_GIF(pic):
    
    width = getWidth(pic)
    height = getHeight(pic)
    picXCenter = width/2
    picYCenter = height/2
    
    canvDim = int(sqrt(width**2 + height**2)) + 1
    canvas = makeEmptyPicture(canvDim, canvDim)
    startXY = canvDim/2
    
    for degAngle in range(360 + 1):
        angle = (degAngle*pi)/180
        for x in range(width):
            for y in range(height):
                color = getColor(getPixel(pic, x, y))
            
                newX = startXY + int( (x - picXCenter)*cos(angle) - (y - picYCenter)*sin(angle) )
                newY = startXY + int( (x - picXCenter)*sin(angle) + (y - picYCenter)*cos(angle) )
                setColor(getPixel(canvas, newX, newY), color)
        #antiAlias(canvas)
        repaint(canvas)


## Problema 4 
# (effetto blend): Scrivere una o piu' funzioni Python che, date due immagini A e B, miscela
# GRADUALMENTE l'immagine A in B, fino a sostituire l'intera immagine con l'altra.

def showBlend(pic1, pic2):
# @param pic1,pic2: Picture
    canvasW = min(getWidth(pic1), getWidth(pic2))
    canvasH = min(getHeight(pic1), getHeight(pic2))
    canvas = makeEmptyPicture(canvasW, canvasH)
    
    for k in range(0, 120, 20):
        blend(pic1, pic2, k, canvas)
        repaint(canvas)

def blend(A, B, k, canvas):
# @param A: picture
# @param A: picture
# @param k: int
# @param canvas: picture
    for x in range( min( getWidth(B), getWidth(A) ) ):
        for y in range( min( getHeight(B), getHeight(A) ) ):
            pixB = getPixel(B, x, y)            
            pixA = getPixel(A, x, y)            
            pixCanvas = getPixel(canvas, x, y)
            
            newRed = (k/100.0) * getRed(pixA) + (1 - (k/100.0) ) * getRed(pixB)
            newGreen = (k/100.0) * getGreen(pixA) + (1 - (k/100.0) ) * getGreen(pixB)
            newBlue = (k/100.0) * getBlue(pixA) + (1 - (k/100.0) ) * getBlue(pixB)
            
            color = makeColor(newRed, newGreen, newBlue)
            setColor(pixCanvas, color)


## Problema 5: 
# Scrivere una o piu' funzioni Python per disegnare un quadrato con iscritto un altro
# quadrato ruotato di 45 gradi e i cui vertici sono tangenti ai lati del primo.

def mirrorVertical(source):
# @param source: Picture;
    width = getWidth(source)
    mirrorPoint = width / 2
    for y in range(0, getHeight(source)):
        for x in range(0, mirrorPoint):
            leftPixel = getPixel(source, x, y)
            rightPixel = getPixel(source, width - x - 1, y)
            color = getColor(leftPixel)
            setColor(rightPixel, color)

def mirrorHorizontal(source):
# @param source: Picture;
    height = getHeight(source)
    mirrorPoint = height / 2
    for x in range(0, getWidth(source)):
        for y in range(0, mirrorPoint):
            topPixel = getPixel(source, x, y)
            bottomPixel = getPixel(source, x, height - y - 1)
            color = getColor(topPixel)
            setColor(bottomPixel, color)

def drawSquare(pic, startX, startY, lato):
    for x in range(startX, startX + lato):
        for y in range(startY, startY + lato):
            if x == startX or x == startX + lato -1 or y == startY or y == startY + lato -1:
                setColor(getPixel(pic, x, y), black)

def drawSquare45(pic):
# @param pic: Picture
    width = getWidth(pic)
    centerX = width/2
    for x in range(0, width/2):
        for y in range(0, width/2):    
            if x == y:
                setColor(getPixel(pic, width/2-x-1, y), black)
    mirrorVertical(pic)
    mirrorHorizontal(pic)

def drawTangentSquare(lato):
# @param l: int; lato del quadrato piu' interno
    diagonale = int(sqrt(lato**2 + lato**2))
    latoCanvas = int(sqrt(diagonale**2 + diagonale**2))
    canvas = makeEmptyPicture(latoCanvas, latoCanvas)
    
    x = latoCanvas/2 -lato/2
    y = x    
    
    drawSquare(canvas, x, y, lato)    
    drawSquare45(canvas)
    
    show(canvas)


## Problema 6: 
# Scrivere una o piu' funzioni Python che, data un'immagini A, conta il numero di
# righe per cui non esiste alcun pixel che ha il valore di ciascuna componente R,G,B < k (con k
# parametro assegnato).

def existPix(pic, row, k):
# @param pic: Picture
# @row: int; indice di riga
# @param k: int; parametro per la verifica
    for x in range(getWidth(pic)):
        pix = getPixel(pic, x, row)
        if getRed(pix) < k and getGreen(pix) < k and getBlue(pix) < k:
            return True
    return False

def countRows(pic, k):
# @param pic: Picture
# @param k: int; parametro per la verifica
# @return int
    count = 0
    for y in range(getHeight(pic)):
        if not existPix(pic, y, k):
            count = count + 1
    return count
    

## Problema 7: 
# Scrivere una o piu' funzioni Python che, data un'immagine A, restituisce la percentuale
# di pixel per cui la componente Red e' doppia rispetto a quella Green.

def countRedGreen(pixList):
# @return int
# @param pixList: list; list of pixels
    count = 0
    for px in pixList:
        if getRed(px) == 2*getGreen(px):
            count += 1
    return count

def percetRedGreen(pic):
# @param pic: Picture
# @return int
    pixList = getPixels(pic)
    totPix = len(pixList)
    count = countRedGreen(pixList)
    return ( count/totPix ) * 100


## Problema 8
# Scrivere una o piu' funzioni Python che, date due immagini A e B, restituisce il numero di 
# colonne di A in cui almeno k pixel hanno la stessa luminosita' di quelli nella rispettiva 
# colonna di B.

def contaCol(pic1, pic2, k):
# @param pic1; Picture
# @param pic1; Picture
# @param k: int
# @return int
    count = 0
    for x in range(getWidth(pic1)):
        if contaPix(pic1, pic2, x) >= k:
            count += 1
    return count

def contaPix(pic1, pic2, x):
# @param pic1; Picture
# @param pic1; Picture
# @param x: int; colonna corrente
# @return int
    count = 0
    if x > getWidth(pict2):
        return 0
    else:
        for y1 in range(getHeight(pict1)):
            for y2 in range(getHeight(pict2)):
                if lum(getPixel(pict1, x, y1)) == lum(getPixel(pict2, x, y2)):
                    count += 1
        return count

def lum(px):
# @param: pixel
# @return int
    return (getRed(px) + getGreen(px) + getBlue(px))/3


## Problema 10
# Scrivere una funzione che realizzi l'effetto scurimento/schiarimento progressivo di 
# un'immagine fino ad arrivare al nero/bianco totale.

def changeBrithness(pict, x, option):
# @param pic: Picture
# @param x: float
# @param option: bool; (True) = black, (False) = white
    while not ( ( allBlack(pict) and option ) or ( allWhite(pict) and not option ) ):
        for px in getPixels(pict):
            originalRed = getRed(px)
            originalGreen = getGreen(px)
            originalBlue = getBlue(px)
        
            if option:  # darker
                color = makeColor(originalRed - x, originalGreen - x, originalBlue - x)
            else:
                color = makeColor(originalRed + x, originalGreen + x, originalBlue + x)
        
            setColor(px, color)
        repaint(pict)

def allBlack(pict):
    for px in getPixels(pict):
        if not getColor(px) == black:
            return False
    return True
 
def allWhite(pict):
    for px in getPixels(pict):
        if not getColor(px) == white:
            return False
    return True


## Problema 11
# Scrivere una funzione o piu' funzioni Python che, data una stringa s e due lettere l1 e l2 , 
# crei una nuova stringa in cui: 
#
# 1) sono state eliminate tutte le cifre presenti in s, 
# 2) ad ogni occorrenza di l1 in s, questa venga sostituita con la prima lettera che la 
#    precede (se presente), 
# 3) ad ogni occorrenza della lettera l2, ripetere la lettera tante volte quante volte occorre 
#    in s da quel punto in poi .

def ComposeStr(str, l1, l2):
# @param str: string
# @param l1: char
# @param l2: char
# @return string    
    for i in range(len(str)):
        if not str[i].sdigit():
            if str[i] == l1:
                newStr += getPrev(str[:i])
            elif str[i] == l2:
                newStr += str[i]*getOccurr(str[i:], l2)
            else:
                newStr += str[i]
    return newStr

def getPrev(str):
# @parma str: string
# @return string
    char = ""
    for i in range(len(str)):
        if str[len(str)-1-i].isalpha():
            char = str[len(str)-1-i]
            return char
    return char

def getOccurr(str, char):
# @parma str: string
# @parma char: string
# @return int
    count = 0
    for ch in str:
        if ch == char:
            count += 1
    return count
