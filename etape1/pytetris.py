import vue
import modele
import time


class Controleur:
    def __init__(self,modd):
        '''Controleur, ModeleTetris->Controleur'''
        
        self.__tetris=modd
        self.__vuetetris=vue.VueTetris(self.__tetris)
        self.__delai=320
       
        self.__fen=self.__vuetetris.fenetre()
        self.__vuetetris.dessine_forme(self.__tetris.get_coord_absolue(),self.__tetris.get_couleur_forme())
        self.joue()
        self.__fen.mainloop()
        
        
        
    def joue(self) :
        '''Controleur -> None
        boucle principale du jeu. Fait tomber une forme d'une ligne'''
        if not self.__tetris.est_fini() :
            self.affichage()
            self.__fen.after(self.__delai,self.joue)
            
    def affichage(self):
        '''Controleur,none
        dessine une forme et reinitialise le terrain'''
        self.__tetris.forme_tombe()
        self.__vuetetris.dessine_terrain()
        self.__vuetetris.dessine_forme(self.__tetris.get_coord_absolue(),self.__tetris.get_couleur_forme())
        
        

if __name__ == "__main__" :
      tetris = modele.ModeleTetris()

      ctrl = Controleur(tetris)
      
  


