import pygame
class Texte(pygame.sprite.Sprite):
    def __init__(self,texte,police,largEcran,hautEcran):
        super(Texte,self).__init__()
        self.surf=police.render(texte,False,(255,255,0))
        self.rect=self.surf.get_rect(
            center=(largEcran/2, hautEcran/2)
        )
        