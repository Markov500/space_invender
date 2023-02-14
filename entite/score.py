import pygame
class Score(pygame.sprite.Sprite):
    def __init__(self, police, largEcran):
        super(Score,self).__init__()
        self.valeur=0
        self._setText(police, largEcran)
        
    
    def _setText(self,police, largEcran):
        self.surf = police.render(
            "Score : "+str(self.valeur)+"PTS", False,(255,255,255)
        )

        self.rect = self.surf.get_rect(
            center=(largEcran/2, 20)
        )

    

    def update(self,police,largEcran):
        self._setText(police,largEcran)