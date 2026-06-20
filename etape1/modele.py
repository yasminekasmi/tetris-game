import random

class ModeleTetris:
    def __init__(self,lig=12,col=14):
        '''ModeleTetris,int,int->ModeleTetris'''
        self.__haut=lig+4
        self.__larg=col
        self.__base=4
        self.__forme = Forme(self)
        
        
        l=[]
        for i in range (self.__haut):
            liste=[]
            for j in range (self.__larg):
                if i < self.__base :
                    liste.append(-2)
                else :
                    liste.append(-1)
            l.append(liste)
        self.__terrain = l
        
        
    def get_largeur(self):
        '''ModeleTetris->int
        retourne le nb de colonne'''
        return self.__larg
    
    
    def get_hauteur(self):
        '''ModeleTetris->int
        retourne le nb de lignes'''
        return self.__haut
    
    
    def get_valeur(self,lig,col):
        '''ModeleTetris,int,int->int
        retourne la valeur d'une case'''
        return self.__terrain[lig][col]
    
    
    def get_occupe(self,lig,col):
        '''ModeleTetris,int,int->bool
        test si la case est occupée'''
        return self.get_valeur(lig,col)>=0
        
        
        
    def est_fini(self):
        '''ModeleTetris->bool
        test si la partie est finie'''
        for i in range (self.__larg):
            if self.get_occupe(self.__base,i) :
                return True
        
        return False
            
            
 
    
    
    
    def ajoute_forme(self):
        '''ModeleTetris->none
        ajoute une forme sur le terrain'''
        for elt in self.__forme.get_coords():
            self.__terrain[elt[1]][elt[0]]=self.__forme.get_couleur()
            
            
            
    def forme_tombe(self):
        '''ModeleTetris->bool
        faire tomber une forme sur le terrain s'il y' a pas a eu collision,si non ajoute une nouvelle forme'''
        if self.__forme.tombe():
            self.ajoute_forme()
            self.__forme=Forme(self)
            return True
        return False
            
                
                
            
    def get_couleur_forme(self):
        '''ModeleTetris->int
        retourne l'indice de la couleur'''
        return self.__forme.get_couleur()
    
    
    
    def get_coord_absolue(self):
        '''ModeleTetris,(int,int)
        retourne les coordonnées absolues d'une forme sur le terrain'''
        return self.__forme.get_coords()
    
    
    
class Forme:
    
    
    def __init__(self,modele):
        '''Forme,ModeleTetris->Forme'''
        self.__modele = modele
        self.__couleur= 0
        self.__forme = [(-1,1),(-1,0),(0,0),(1,0)]
        self.__x0=random.randint(2,self.__modele.get_largeur()-2)
        self.__y0=0
    
        
    def get_couleur(self):
        '''Forme->int
        retourne l'indice de la couleur'''
        return self.__couleur
    
    
    
    
    def get_coords(self):
        '''Forme->(int,int)
        retourne les coordonnées absolue d'une forme sur le terrain'''
        
        l=[]
        for elt in self.__forme:
            l.append((self.__x0+elt[0],self.__y0+elt[1]))
        return l
        
       
    
    
    
    def collision(self):
        '''Forme->bool
        detecte une collision'''
        for elt in self.get_coords():
            if elt[1]==self.__modele.get_hauteur()-1  or self.__modele.get_occupe(elt[1]+1,elt[0]):
                return True
        return False

    
    
    def tombe(self):
        '''Forme->bool
        faire tomber la forme si il y'a pas eu de collision'''
        if self.collision():
            return True
        else:
            self.__y0+=1
            return False
            
        
        
        
     
           
        
        
        
        
        
        
        
        
        
        
        
            
        