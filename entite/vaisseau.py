import pygame

from entite.missile import Missile
class Vaisseau(pygame.sprite.Sprite):
    def __init__(self):
        super(Vaisseau,self).__init__()
        #self.taille=pygame.Surface((50,25))#Définir la taille du vaisseau
        self.fond=pygame.image.load("ressources/vaisseau.png").convert()
        self.fond.set_colorkey((255,255,255),pygame.RLEACCEL)#Supprimer la couleur de fond
    
        self.rect=self.fond.get_rect()#Retenir la position

        self.vitesse= 10


    #########################################################################
    ###********************IMPLEMENTER LES ACTIONS************************
    ########################################################################
    def update(self,touche,largEcran, hautEcran, missiles):
        if touche[pygame.K_UP]:
            self.rect.move_ip(0, -self.vitesse)
            return 0

        if touche[pygame.K_DOWN]:
            self.rect.move_ip(0, self.vitesse)
            return 0


        if touche[pygame.K_LEFT]:
            self.rect.move_ip(-self.vitesse, 0)
            return 0

        if touche[pygame.K_RIGHT]:
            self.rect.move_ip(self.vitesse, 0)
            return 0

        if touche[pygame.K_TAB]:
            if len(missiles)<3:
                missiles.add(Missile(self.rect.center))
                pygame.time.delay(150)
                return 1

        #Les conditions pour empêcher le vaisseau de bouger hors de l'écran
        if self.rect.top < 0:
            self.rect.top=0

        if self.rect.left < 0:
            self.rect.left=0

        if self.rect.right > largEcran:
            self.rect.right = largEcran

        if self.rect.bottom > hautEcran:
            self.rect.bottom = hautEcran