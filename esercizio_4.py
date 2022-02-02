# Completare il codice per elaborare una immagine in strisce verticali che
# vengono scambiate tra loro (ogni striscia viene scambiata con quella adiacente
# alla sua destra);
# i ... indicano la mancanza di una o piu' parti di codice


def verticalStrips(pict, stripWidth):
# @param pict: Picture
# @param stripWidth: int; ampiezza di una striscia (da scambiare con quella adiacente)
   for c in range(0, getWidth(pict)-getWidth(pict)%(2*stripWidth), 2*stripWidth):
       stripExchange(pict, c, stripWidth)
   show(pict)

     
def stripExchange(pict, colIndex, stripWidth):
# @param pict: Picture
# @param colIndex: int     
# @param stripWidth: int
   for x in range(colIndex, colIndex + stripWidth):
       for y in range(0, getHeight(pict)):
           pSx = getPixel(pict, x, y)
           pDx = getPixel(pict, x+stripWidth, y)
           colorSx = getColor(pSx)
           colorDx = getColor(pDx)
           setColor(pSx, colorDx)
           setColor(pDx, colorSx)
           

# Avevo promesso di fornirvi le mie versioni delle due "animazioni" mostrate qualche lezione fa, cosi' potrete 
# confrontarle con le vostre. Premetto che queste non sono Le soluzioni, sono solo possibili soluzioni. 
# Per la prima (schiarimento/scurimento progressivo), vi riporto il codice completo (funziona "bene" con immagini 
# piccole, su immagini piu' grandi conviene aggiustare il numero di iterazioni e/o lo step):

def slider2(pict, step):
# @param pict: Picture
# @param step: int
#suggerimento: usare step == +6 oppure -6
    show(pict)
    for i in range(0, 50) :
        changeBrightness2(pict, step)
        repaint(pict)

def changeBrightness2(picture, step):
# @param picture: Picture; immagine da modificare
# @param step: int; passo di variazione di luminosita'(positivo o negativo)
    for pix in getPixels(picture):
        originalRed = getRed(pix)
        originalBlue = getBlue(pix)
        originalGreen = getGreen(pix)
        modifiedRed = originalRed + step
        modifiedBlue = originalBlue + step
        modifiedGreen = originalGreen + step
        newColor = makeColor(int(modifiedRed), int(modifiedGreen), int(modifiedBlue))
        setColor(pix, newColor)
        

# Per la seconda animazione (trascolorazione progressiva di un'immagine in un'altra), vi propongo invece una 
# soluzione parziale, da completare. Ricordo le regole per questa tipologia di problemi: il codice dato non deve 
# essere considerato come un canovaccio da cui partire per proporre proprie soluzioni. NON bisogna modificare 
# assolutamente nulla, e inserire SOLAMENTE le parti mancanti (indicate da ". . .") per renderlo eseguibile e 
#funzionalmente corretto.
#Vale ovviamente la raccomandazione di verificare, eseguendola, se la funzione che avete ri-costruito risolve 
#correttamente il problema:

# Completare il codice seguente per miscelare progressivamente due immagini;
# si assuma per semplicita' che la seconda immagine abbia sempre dimensioni uguali o
# maggiori di quelle della prima immagine;
# i ... indicano la mancanza di una o piu' parti di codice
# la funzione mixer() realizza l' "animazione"
# la funzione blendPictures() miscela una percentuale C della prima immagine
#    con una percentuale 100-C della seconda

def mixer(pict1, pict2) :
# @param pict1: Picture
# @param pict2: Picture;
    W = min(getWidth(pict1), getWidth(pict2))
    H = min(getHeight(pict1), getHeight(pict2))
    canvas = makeEmptyPicture(W, H)
    for b in range(0, 101, 5):
        blendPictures(pict1, pict2, b, canvas)
        repaint(canvas)

                     
def blendPictures(pict1, pict2, blendFactor, canvas) :
# @param pict1: Picture
# @param pict2: Picture
# @param blendFactor: int
# @param canvas: Picture
    for x in range(0, getWidth(pict1)) :
        for y in range(0, getHeight(pict1)) :
            pix1 = getPixel(pict1, x, y)
            pix2 = getPixel(pict2, x, y)
            pixCanvas = getPixel(canvas, x, y)
            newRed = (blendFactor/100.0)*getRed(pix1)+(1-(blendFactor/100.0))*getRed(pix2)
            newGreen = (blendFactor/100.0)*getGreen(pix1)+(1-(blendFactor/100.0))*getGreen(pix2)
            newBlue = (blendFactor/100.0)*getBlue(pix1)+(1-(blendFactor/100.0))*getBlue(pix2)
            color = makeColor(newRed,newGreen,newBlue)
            setColor(pixCanvas, color)
            

# scrivere una funzione che, data un'immagine e un intero K, inverte il valore della componente Red con quello 
# della componente Blue in tutti e soli i pixel dell'immagine che hanno la coordinata "larghezza" (la prima) <K 
# (in altre parole, se prima della modifica un pixel ha Red=10 e Blue=50, dopo la modifica deve avere Red=50 e 
# Blue=10). Per verificare la correttezza della soluzione elaborata, provate a far lavorare la funzione su 
# un'immagine costruita cosi': makeEmptyPicture(500, 500, red) (un quadrato tutto rosso). Se la soluzione e' corretta,
# dovreste ottenere una nuova immagine con una striscia blu di larghezza K nella parte sinistra dell'immagine 
# (il resto rimane rosso).

def exchangeRedBlue(pixel):
# @param pixel: Pixel 
    Red = getRed(pixel)
    Blue = getBlue(pixel)
    setRed(pixel, Blue)
    setBlue(pixel, Red)
    

def drawStripe(pict, k):
# @param pict: Picture
# @param k: int
    for x in range(0, min(k, getWidth(pict))):
        for y in range(0, getHeight(pict)):
            pix = getPixel(pict, x, y)
            exchangeRedBlue(pix)


# Completare il codice seguente, che estrae da un'immagine i contorni delle figure presenti
# i ... indicano la mancanza di una o piu' parti di codice
# Nota 1: il rilevamento dei contorni e' basato sul rilevamento di "bruschi" cambi di
# luminosita' tra un pixel e quelli adiacenti ad esso.
# Nota 2: la luminosita' di un pixel e' calcolata come somma delle componenti R,G,B (diviso 3)
# Nota 3: la funzione duplicatePicture() e' una funzione del tipo di dato Picture presente
# in JES; restituisce una copia dell'immagine passata come parametro

def lineDetect(orig, threshold):
# @param orig: Picture
# @param threshold: int (for most pictures, good results for values <, << 50)
# @return makeBW: Picture
    makeBW = duplicatePicture(orig) # makeBW e' l'immagine che verra' modificata tracciando i bordi
    for x in range(0, getWidth(orig) - 1):
        for y in range(0, getHeight(orig) - 1):
            here=getPixel(makeBW, x, y)
            down=getPixel(orig, x, y+1)
            right=getPixel(orig, x+1, y)
            hereLum=(getRed(here)+getGreen(here)+getBlue(here))/3
            downLum=(getRed(down)+getGreen(down)+getBlue(down))/3
            rightLum=(getRed(right)+getGreen(right)+getBlue(right))/3
            if (abs(hereLum - downLum) > threshold) and (abs(hereLum - rightLum) > threshold):
                setColor(here ,black)
            if (abs(hereLum - downLum) <= threshold) or (abs(hereLum - rightLum) <= threshold):
                setColor(here ,white)
    return makeBW