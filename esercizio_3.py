# 1) scrivere una funzione che consenta di inserire un rettangolo colorato all'interno di un'immagine (posizione, 
# colore e dimensione del rettangolo forniti come parametri);

def drawRectangle(pict, xRect, yRect, wRect, hRect, color):
# @param pict: Picture
# @param xRect: int; coordinata X del rettangolo
# @param yRect: int; coordinata Y del rettangolo
# @param wRect: int; larghezza del rettangolo
# @param hRect: int; altezza del rettangolo
# @param color: Color
    imgWidth = getWidth(pict)
    imgHeight = getHeight(pict)
    for x in range(xRect, min(imgWidth, xRect + wRect)):
        for y in range(yRect, min(imgHeight, yRect + hRect)):
            pix = getPixel(pict, x, y)
            setColor(pix, color)           


# 2) tracciare una "scaletta" all'interno di un'immagine bianca

def drawLadder(stepWidth, stepHeight, color):
# @param height : int; altezza del rect
# @param width : int; larghezza del rect
# @param startingPixX : int; coordinata X dell'inizio del rect
# @param startingPixY : int; coordinata  dell'inizio del rect
# @param color : color; Color   
    canvasWidth = 800
    canvasHeight = 500
    startingPixX = 0
    startingPixY = 0
    wPadding = 0
    hPadding = 0
    canvas = makeEmptyPicture(canvasWidth,canvasHeight)
    
    # cicli per disegnare i trattini orizzontali della scaletta
    for y in range(0, canvasHeight, stepHeight):
        for x in range(wPadding + startingPixX, min(canvasWidth, wPadding + stepWidth)):
            pix = getPixel(canvas, x, y)
            setColor(pix, color)
        wPadding = x + 1
    
    # cicli per disegnare i trattini orizzontali della scaletta
    for x in range(stepWidth, canvasWidth, stepWidth):
        for y in range(hPadding + startingPixY, min(canvasHeight, hPadding + stepHeight)):
            pix = getPixel(canvas, x, y)
            setColor(pix, color)
        hPadding = y + 1
        
    repaint(canvas)
    explore(canvas)
    
    
# 3) Ricordo infine le "sfide" lanciate oggi:
#    provare a scrivere una funzione che visualizza sullo schermo lo schiarimento/scurimento progressivo di un'immagine;
#    provare a scrivere una funzione che visualizza sullo schermo la trascolorazione progressiva di un'immagine in un'altra.

def vanish(pict, iterations):
# @param pict: Picture
# @param iteration: int; numero di esecuzione del ciclo di schiarimento    
    percentageEachStep = round(float(100)/iterations)
    for iter in range(0, iterations):
        repaint(pict)
        for x in range(0, getWidth(pict)):
            for y in range(0, getHeight(pict)):
                pix = getPixel(pict, x, y)
                
                #catturo i singoli colori del pixel 
                Red = getRed(pix)
                Green = getGreen(pix)
                Blue = getBlue(pix)
                
                # red
                RedUnit = round(float(Red)/100)
                RedIncrease = RedUnit * percentageEachStep * iter
                RedEnhanced = Red + RedIncrease
                # green
                GreenUnit = round(float(Green)/100)
                GreenIncrease = GreenUnit * percentageEachStep * iter
                GreenEnhanced = Green + GreenIncrease
                # blue
                BlueUnit = round(float(Blue)/100)
                BlueIncrease = BlueUnit * percentageEachStep * iter
                BlueEnhanced = Blue + BlueIncrease
                
                vanishedColor = makeColor(RedEnhanced, GreenEnhanced, BlueEnhanced)
                setColor(pix, vanishedColor)
                
                #colorPix = getColor(pix)
                #vanishedColor = makeLighter(colorPix)
                #setColor(pix, vanishColor)
        

def darken(pict, iterations):
# @param pict: Picture
# @param iteration: int; numero di esecuzione del ciclo di schiarimento    
    percentageEachStep = round(float(100)/iterations)
    for iter in range(0, iterations):
        repaint(pict)
        for x in range(0, getWidth(pict)):
            for y in range(0, getHeight(pict)):
                pix = getPixel(pict, x, y)
                
                #catturo i singoli colori del pixel 
                Red = getRed(pix)
                Green = getGreen(pix)
                Blue = getBlue(pix)
                
                # red
                RedUnit = round(float(Red)/100)
                RedDecrease = RedUnit * percentageEachStep * iter
                RedEnhanced = Red - RedDecrease
                # green
                GreenUnit = round(float(Green)/100)
                GreenDecrease = GreenUnit * percentageEachStep * iter
                GreenEnhanced = Green - GreenDecrease
                # blue
                BlueUnit = round(float(Blue)/100)
                BlueDecrease = BlueUnit * percentageEachStep * iter
                BlueEnhanced = Blue - BlueDecrease
                
                darkenColor = makeColor(RedEnhanced, GreenEnhanced, BlueEnhanced)
                setColor(pix, darkenColor)
                
                #colorPix = getColor(pix)
                #vanishedColor = makeDarker(colorPix)
                #setColor(pix, darkenColor)


def mixer (pict1, pict2, iterations):
# @param pict1 : Picture
# @param pict2 : Picture | The picture that will overlap the first one
# @param iteration : int | The number of times of "image repaint"
    percentageEachStep = round(float(100)/iterations)
    for iter in range(1, iterations+1): # iterazioni    
        repaint(pict1)
        for x in range(0, min(getWidth(pict1), getWidth(pict2))): # larghezza
            for y in range(0, min(getHeight(pict1), getHeight(pict2))): # altezza
                firstImagePix = getPixel(pict1, x, y)
                secondImagePix = getPixel(pict2, x, y)
        
                # retreiving colors
                firstImageRed = getRed(firstImagePix)
                firstImageGreen = getGreen(firstImagePix)        
                firstImageBlue = getBlue(firstImagePix)  
        
                secondImageRed = getRed(secondImagePix)
                secondImageGreen = getGreen(secondImagePix)        
                secondImageBlue = getBlue(secondImagePix) 
        
                # processing FIRST image and retreive colors to be bounded     
                # red
                firtImageRedUnit = float(firstImageRed)/100   
                firstImageRedDecrease = firtImageRedUnit * percentageEachStep * iter
                firstImageRedScaled = firstImageRed - firstImageRedDecrease
                # green
                firtImageGreenUnit = float(firstImageGreen)/100   
                firstImageGreenDecrease = firtImageGreenUnit * percentageEachStep * iter
                firstImageGreenScaled = firstImageGreen - firstImageGreenDecrease
                # blue
                firtImageBlueUnit = float(firstImageBlue)/100   
                firstImageBlueDecrease = firtImageBlueUnit * percentageEachStep * iter
                firstImageBlueScaled = secondImageBlue - firstImageBlueDecrease

                # processing SECOND image and retreive colors to be bounded     
                # red
                secondImageRedUnit = float(secondImageRed)/100
                secondImageRedIncrease = secondImageRedUnit * percentageEachStep * iter
                secondImageRedEnhanced = secondImageRed + secondImageRedIncrease
                # green
                secondImageGreenUnit = float(secondImageGreen)/100
                secondImageGreenIncrease = secondImageGreenUnit * percentageEachStep * iter
                secondImageGreenEnhanced = secondImageGreen + secondImageGreenIncrease
                # blue
                secondImageBlueUnit = float(secondImageBlue)/100
                secondImageBlueIncrease = secondImageBlueUnit * percentageEachStep * iter
                secondImageBlueEnhanced = secondImageBlue + secondImageBlueIncrease
        
        
                scaledRed = (firstImageRedScaled + secondImageRedEnhanced)/2
                scaledGreen = (firstImageGreenScaled + secondImageGreenEnhanced)/2
                scaledBlue = (firstImageBlueScaled + secondImageBlueEnhanced)/2
        
        
                secondImagePixColorScaled = makeColor(scaledRed, scaledGreen, scaledBlue) 
                setColor(firstImagePix, secondImagePixColorScaled)




# A) Date le due funzioni riportate sotto, siete in grado di descrivere esattamente come verra' modificata 
# l'immagine passata come parametro (senza eseguire le funzioni)? Provate poi ad eseguirle per verificare.

def enigma(pict, col):
# @param pict: picture
# @param col: color
    for x in range(0, min(getWidth(pict), getHeight(pict))):
        px = getPixel(pict, x, x)
        setColor(px, col)      


def enigma2(pict, col, k):
# @param pict: picture
# @param col: color
# @param k: int
    for x in range(0, min(getWidth(pict), getHeight(pict))):
        px = getPixel(pict, x, x+k)
        setColor(px, col)


def miaVarianteEnigma2(pict, col, k):
# Se k negativo disegna una "diagonale" spostata verso destra
# se k positivo disegna una "diagonale" spostata verso sinistra
# @param pict: picture
# @param col: color
# @param k: int
    if(k >= 0):
        for x in range(0, min(getWidth(pict), getHeight(pict) - k)):
            px = getPixel(pict, x, x+k)
            setColor(px, col)
    else:
        for y in range(0, min(getWidth(pict), getHeight(pict) + k)):
            px = getPixel(pict, y-k, y)
            setColor(px, col)
            
def drawDiagonals(pict, col, k):
# @param pict: picture
# @param col: color
# @param k: int
    width = getWidth(pict)
    height = getHeight(pict)
    for i in range(-width, height, k):
        miaVarianteEnigma2(pict, col, i)