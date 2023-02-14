from entite.ennemie import Ennemi
from entite.explosion import Explosion
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
lesMissiles=pygame.sprite.Group()
lesEnnemis=pygame.sprite.Group()
lesExplosions=pygame.sprite.Group()


#Gestion des temps d'exécution
temps=pygame.time.Clock()
creationEnnemi= pygame.USEREVENT + 1 #Creation d'une évènement  

pygame.time.set_timer(creationEnnemi,1000) #Le timer déclenche l'évènement toutes les secondes

pause=False

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
#Définition de la boucle permettant l'exécution en continue du jeu
continuer=True
while continuer:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            continuer = False
        elif event.type == creationEnnemi:
            newEnnemi= Ennemi(largeur,hauteur)
            lesEnnemis.add(newEnnemi)

    ecran.fill((0,25,25))
    #Detecter les colisions ennemi/heros
    if pygame.sprite.spritecollideany(heros, lesEnnemis):
       
        heros.kill()
        lesExplosions.add(Explosion(heros.rect.center))
        sonExplosion.play()
        ecran.blit(txtGameOver.surf,txtGameOver.rect)
        continuer = False
        

    #Detecter les colisions ennemi/missile
    for mis in lesMissiles:
        ennemiTouche= pygame.sprite.spritecollide(mis, lesEnnemis, True)
        for enne in ennemiTouche:
            lesExplosions.add(Explosion(enne.rect.center))
            sonExplosion.play()
        if len(ennemiTouche)>0:
            mis.kill()
            point.valeur+=1



    touche_pressee=pygame.key.get_pressed()#pour savoir quelle touche a été appuyé pendant l'exécution
    if touche_pressee[pygame.K_TAB] :
        sonDeTir.play()
    #Les méthodes update perment de modifier l'emplacement des différents objets sur l'écran
    heros.update(touche_pressee,largeur,hauteur,lesMissiles)
    lesMissiles.update(largeur)
    lesEnnemis.update()
    lesExplosions.update()
    point.update(police,largeur)

    ecran.blit(heros.fond,heros.rect)#Afficher le héros à l'écran

    ecran.blit(point.surf,point.rect)#Afficher le score à l'écran

    if point.valeur % 10 ==0 and point.valeur > 9:
        ecran.blit(bravo.surf,bravo.rect)
    for obus in lesMissiles:
        ecran.blit(obus.fond,obus.rect)#Afficher les missiles à l'écran

    for mechant in lesEnnemis:
        ecran.blit(mechant.fond,mechant.rect)#Afficher les ennemis à l'écran

    for boom in lesExplosions:
        ecran.blit(boom.fond,boom.rect)#Afficher les explosions à l'écran


    
    pygame.display.flip()

    temps.tick(20)
pygame.time.delay(2000)
pygame.quit()

