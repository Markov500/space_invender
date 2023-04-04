from entite.vaisseau import Vaisseau
from entite.score import Score
from entite.texte import Texte
#Code obligatoire lorsqu'on utilise pygame
import pygame
pygame.init()

#Définition d'un titre
pygame.display.set_caption("Jeu de tir dans l'espace")

#Définition de l'écran avec ses dimensions 
largeur=800
hauteur=600
ecran=pygame.display.set_mode([largeur,hauteur])

#Définir les objets
heros=Vaisseau()

#Définitions des groupes d'objets, permettant l'apparition de plusieurs objets du mème type sur la scène
lesMissiles=pygame.sprite.Group()
lesEnnemis=pygame.sprite.Group()
lesExplosions=pygame.sprite.Group()


sceneColor = (0,25,25)
#Gestion des temps d'exécution
temps=pygame.time.Clock()
creationEnnemi= pygame.USEREVENT + 1 #Creation d'une évènement  

pygame.time.set_timer(creationEnnemi,1000) #Le timer déclenche l'évènement toutes les secondes



#Gestions de l'afichage du score
pygame.font.init()
police=pygame.font.SysFont("algerian", 40)
point=Score(police, largeur)



#Gestion du son
pygame.mixer.init()
sonExplosion=pygame.mixer.Sound("ressources/explosion.ogg")
sonDeTir=pygame.mixer.Sound("ressources/laser.ogg")



bravo=Texte("BRAVO",police,largeur,hauteur)
txtGameOver=Texte("GAME OVER",police,largeur,hauteur)
pauseText = Texte("PAUSE",police,largeur,hauteur)