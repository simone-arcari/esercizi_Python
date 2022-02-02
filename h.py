# A) Date le due funzioni riportate sotto, siete in grado di descrivere esattamente come verrà modificata 
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