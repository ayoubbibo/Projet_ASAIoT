
from driverI2C import *
from groveCompass import *

'''import time
import sys'''

#       La fonction affiche sur l'écran lcd le texte qu'on souhaite     
def afficheSurEcran(texte):
    setText(texte)

#       La fonction Change la couleur de l'ecran LCD
def changerCouleur(couleur):
    setColor(couleur)

#       La fonction renvoie l'orientation du livreur    
def orientation():
    return getOrientation()



#       TEST    
orientation()
afficheSurEcran("ayoub")
changerCouleur("blanc")
