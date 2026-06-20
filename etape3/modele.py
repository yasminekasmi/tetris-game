import random
LES_FORMES = [[(0,-1),(0,0),(0,1),(0,2)],[(0,0),(1,0),(0,1),(1,1)],[(0,0),(1,0),(-1,1),(0,1)],[(-1,-1),(0,-1),(0,0),(1,0)],[(-1,0),(0,0),(1,0),(-1,1)],[(-1,0),(0,0),(1,0),(1,1)],[(0,1),(-1,0),(0,0),(1,0)]] 

class ModeleTetris:
    def __init__(self,lig=16,col=14):
        '''ModeleTetris,int,int->ModeleTetris'''
        self.__haut=lig+4
        self.__larg=col
        self.__base=4
        self.__forme = Forme(self)
        self.__score=0
        self.__suivante=Forme(self)
        
        
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
            
            
            
            self.__forme=self.__suivante
            self.__suivante=Forme(self)
            self.supprime_ligne_complete()
        
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
    
    def forme_a_gauche(self):
        '''ModeleTetris->none
        demande a la forme de se deplacer a gauche'''
        self.__forme.a_gauche()
        
    def forme_a_droite(self):
        '''ModeleTetris->none
        demande a la forme de se deplacer a droite'''
        self.__forme.a_droite()
        
    def forme_tourne(self):
        '''ModeleTetris->none
        demande a la forme de tourner'''
        self.__forme.tourne()
        
        
        
        
        
    def est_ligne_complete(self,lig):
        '''ModeleTetris,int->bool
        teste si une ligne est complete'''
        for i in range (len(self.__terrain[lig])):
            
            if not (self.get_occupe(lig,i)):
                return False
        return True
    
    def supprime_ligne(self,lig):
        '''ModeleTetris,int->none
        supprime la ligne d'indice lig'''
        for i in range(len(self.__terrain[lig])):
            self.__terrain[lig][i]=-1
        
        for j in range(lig-1,self.__base-1,-1):
            self.__terrain[j],self.__terrain[j+1]=self.__terrain[j+1],self.__terrain[j]
            
    def supprime_ligne_complete(self):
        '''ModeleTetris->none
        supprime une ligne complete '''
        for i in range(self.__base,self.__haut):
            if self.est_ligne_complete(i):
                self.supprime_ligne(i)
                self.__score+=1
    def get_score(self):
        '''ModeleTetris->int
        retourne le score du joueur'''
        return self.__score
                
                
     
    def get_coords_suivante(self):
         return self.__suivante.get_coord_relatives()
         
    def get_couleur_suivante(self):
         return self.__suivante.get_couleur()
                
            
            
        
        
        
    
class Forme:
    
    
    def __init__(self,modele):
        '''Forme,ModeleTetris->Forme'''
        indice=random.randint(0,len(LES_FORMES)-1)
        self.__modele = modele
        self.__couleur= indice
        self.__forme = LES_FORMES[indice]
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
        
        
    def position_valide(self):
        '''Forme->bool
        teste si une position est valide ou non'''
        for elt in self.get_coords():
            if elt[0]>(self.__modele.get_largeur()-1) or elt[0]<0 or elt[1]>(self.__modele.get_hauteur()-1)or elt[1]<0 or self.__modele.get_occupe(elt[1],elt[0]):
                return False
        return True
    
    def a_gauche(self):
        '''Forme->none
         deplace la forme a gauche''' 
        self.__x0-=1
        if not self.position_valide():
            self.__x0+=1
            
    def a_droite(self):
        '''Forme->none
         deplace la forme a droite'''
        self.__x0+=1
        if not self.position_valide():
            self.__x0-=1
            
            
    def tourne(self):
        '''Forme->none
        retourner une forme si c'est possible'''
        forme_prec=self.__forme
        self.__forme=[]
        for elt in forme_prec:
            x=elt[0]
            y=elt[1]
            elt=(-y,x)
            self.__forme.append(elt)
        if not self.position_valide():
            self.__forme=forme_prec
            
    def get_coord_relatives(self):
        return self.__forme
            
            
            
            
            
            
            
            
            
        
        
            
            
        
        
        
     
           
        
        
        
        
        
        
        
        
        
        
        
            
        