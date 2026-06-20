import vue
import modele
import time


class Controleur:
    def __init__(self,modd):
        '''Controleur, ModeleTetris->Controleur'''
        
        self.__tetris=modd
        self.__vuetetris=vue.VueTetris(self.__tetris)
        self.__delai=320
        self.__delai1=320
       
        self.__fen=self.__vuetetris.fenetre()
        self.__vuetetris.dessine_forme(self.__tetris.get_coord_absolue(),self.__tetris.get_couleur_forme())
        self.joue()
        self.__fen.bind("<Key-Left>",self.forme_a_gauche)
        self.__fen.bind("<Key-Right>",self.forme_a_droite)
        self.__fen.bind("<Key-Down>",self.forme_tombe)
        self.__fen.bind("<Key-Up>",self.forme_tourne)
        self.__fen.mainloop()
        
        
        
    def joue(self) :
        '''Controleur -> None
        boucle principale du jeu. Fait tomber une forme d'une ligne'''
        if not self.__tetris.est_fini() :
            self.affichage()
            self.__fen.after(self.__delai,self.joue)
            
        else:
            self.__vuetetris.reset()
            self.__fen.after(self.__delai,self.joue)
            if self.__vuetetris.recommencer1():
                
                self.__fen.destroy()
                self.__init__(modele.ModeleTetris())
                
            
            
    def affichage(self):
        '''Controleur,none
        dessine une forme et reinitialise le terrain'''
        
        if self.__vuetetris.debut() and not self.__vuetetris.pause1():
                
                if self.__tetris.forme_tombe():
                    self.__delai=self.__delai1
                   
                if self.__tetris.collision()and self.__delai>160:
                   self.__delai1-=1
                   self.__delai-=1
                   
                self.__vuetetris.dessine_terrain()
                self.__vuetetris.dessine_forme(self.__tetris.get_coord_absolue(),self.__tetris.get_couleur_forme())
                
                self.__vuetetris.met_a_jour_score(self.__tetris.get_score())
                    
                    
                
                
        self.__vuetetris.dessine_forme_suivante(self.__tetris.get_coords_suivante(),self.__tetris.get_couleur_suivante())
                
        
    def forme_a_gauche(self,event):
        '''Controleur->none
        demande au modele de se deplacer a gauche'''
        self.__tetris.forme_a_gauche()
        
        
    def forme_a_droite(self,event):
        '''Controleur->none
        demande au modele de se deplacer a droite'''
        self.__tetris.forme_a_droite()
        
    def forme_tombe(self,event):
        '''Controleur->none
        modifie la valeur de la vitesse '''
        self.__delai=160
        
    def forme_tourne(self,event):
        '''Controleur->none
        demande au odele de faire tourner la forme'''
        self.__tetris.forme_tourne()
        
        
        
    

        

        
   
        
   



 
    
    
    
        
        
        

if __name__ == "__main__" :
      tetris = modele.ModeleTetris()

      ctrl = Controleur(tetris)
      
      
      
      
  


