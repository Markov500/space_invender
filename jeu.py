from entite.ennemie import Ennemi
from entite.explosion import Explosion
from config import *

def playGame():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            return 0
        if event.type == creationEnnemi:
            newEnnemi= Ennemi(largeur,hauteur)
            lesEnnemis.add(newEnnemi)

    #Définition de la couleur de la scène
    ecran.fill(sceneColor)
    #Detecter les colisions ennemi/heros
    if pygame.sprite.spritecollideany(heros, lesEnnemis):
        heros.kill()
        lesExplosions.add(Explosion(heros.rect.center))
        sonExplosion.play()
        ecran.blit(txtGameOver.surf,txtGameOver.rect)
        return 0
        

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
    
        
        
    #Les méthodes update perment de modifier l'emplacement des différents objets sur l'écran
    heroTir = heros.update(touche_pressee,largeur,hauteur,lesMissiles)
    if (heroTir == 1):
        sonDeTir.play()
    lesMissiles.update(largeur)
    lesEnnemis.update()
    lesExplosions.update()
    point.update(police,largeur)

      
   
    
    return 1;


def pause():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            return 0
        

    #Définition de la couleur de la scène
    ecran.fill(sceneColor)
    
    ecran.blit(pauseText.surf,pauseText.rect)

    
    
    return 1;



















#Définition de la boucle permettant l'exécution en continue du jeu
arret = 1
isPause = False
while True:
    touche_pressee=pygame.key.get_pressed()#pour savoir quelle touche a été appuyé pendant l'exécution
    if touche_pressee[pygame.K_SPACE] :
        pygame.time.delay(100)
        isPause = not isPause

    if isPause:
        arret = pause()
    else:
        arret = playGame()
    
    if arret == 0:
        break

  
    
    #Affichage des objets sur la scène
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

