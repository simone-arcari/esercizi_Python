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