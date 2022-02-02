# Si definisca come luminosita' di un pixel px la media aritmetica dei valori delle tre componenti del colore 
# di px ((r+g+b)/3).
# Scrivere una funzione che, data un'immagine, restituisce il minimo tra le luminosita' di 
# tutti i pixel dell'immagine.

def minBrightnessPix(picture):
# @param picture: Picture
# @return minLum: int
    minLum = 255
    for pix in getPixels(picture):
        lumPix = (getRed(pix) + getGreen(pix) + getBlue(pix))/3
        if lumPix < minLum:
            minLum = lumPix            
    return minLum
            
        
    
