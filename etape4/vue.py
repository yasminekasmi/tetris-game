import tkinter
import modele
import pytetris

COULEURS = ["red","brown","blue","green","yellow","orange","purple","pink",
"dark grey","black"]
DIM=30
SUIVANT=6

class VueTetris:
    def __init__(self,modele):
        '''VueTetris,ModeleTetris->VueTetris'''
        
        self.__modele=modele
        
        fen=tkinter.Tk()
        fen.title("Tetris")
        can=tkinter.Canvas(fen,width=modele.get_largeur()*DIM,height=modele.get_hauteur()*DIM)
        can.pack(side="left")
        
        frame_btn=tkinter.Frame(fen)
        btn_quitter=tkinter.Button(frame_btn,text="Au revoir",command=fen.destroy,fg="white",bg="red")
        
        frame_btn.pack(side="right")
        self.__btn_commencer=tkinter.Button(frame_btn,text="Commencer",command=self.commencer,fg="white",bg="green")
        self.__btn_commencer.pack(side="top")
        
        self.__commencer=False
        self.__recommencer=False
        self.__pause=False
        self.__reprendre=False
        
        forme_suivante=tkinter.Label(frame_btn,text="Forme suivante")
        forme_suivante.pack()
        self.__can_fsuivante=tkinter.Canvas(frame_btn,width=SUIVANT*DIM,height=SUIVANT*DIM)
        self.__can_fsuivante.pack()
        
        liste=[]
        for i in range(SUIVANT):
            l=[]
            for j in range(SUIVANT):
                
                l.append(self.__can_fsuivante.create_rectangle(j*30,i*30,30*(j+1),30*(i+1), outline="grey",fill="black"))
            liste.append(l)
         
        self.__les_suivants=liste
        
        self.__lbl_score=tkinter.Label(frame_btn,text="Score : 0")
        self.__lbl_score.pack()
      
        btn_quitter.pack()
        self.__can_terrain=can
        can.pack()
        
        liste=[]
        for i in range(self.__modele.get_hauteur()):
            l=[]
            for j in range (self.__modele.get_largeur()):
                if i<4 :
                    can.create_rectangle(j*30,i*30,30*(j+1),30*(i+1), outline="grey",fill="dark grey")
                
                    l.append(can.create_rectangle(j*30,i*30,30*(j+1),30*(i+1), outline="grey",fill="dark grey"))
                else:
                    can.create_rectangle(j*30,i*30,30*(j+1),30*(i+1), outline="grey",fill="black")
                    l.append(can.create_rectangle(j*30,i*30,30*(j+1),30*(i+1),outline="grey",fill="black"))
                
            liste.append(l)
        self.__les_cases=liste
        self.__fenetre=fen
        
        
        
        
    def fenetre(self):
        '''VueTetris->Tk
        retourne la fenetre'''
        return self.__fenetre
    
    def dessine_case(self,i,j,coul):
        '''VueTetris,int,int,int->None
        dessine une case sur le terrain'''
        self.__can_terrain.itemconfigure(self.__les_cases[i][j],fill=COULEURS[coul])
     
        
    def dessine_terrain(self):
        '''VueTetris->none
        dessine le terrain de jeu'''
        for i in range(self.__modele.get_hauteur()):
            for j in range(self.__modele.get_largeur()):
              self.dessine_case(i,j,self.__modele.get_valeur(i,j))
                    
                    
    def dessine_forme(self,coord,couleur):
        '''VueTetris,(int,int),int->none
        dessine une forme dont les coordonnées sont coord et sa couleur couleur'''
        for elt in coord:
            self.dessine_case(elt[1],elt[0],couleur)
            
            
    def met_a_jour_score(self,val):
        '''VueTetris->none
        met a jour la valeur du score'''
        self.__lbl_score["text"]="Score:"+str(val)
        

    def dessine_case_suivante(self,x,y,coul):
        '''VueteTris,int,int,int->none '''
        self.__can_fsuivante.itemconfigure(self.__les_suivants[x][y],fill=COULEURS[coul])
    
    def nettoie_forme_suivante(self):
        '''VueTetris->none
        dessine une case noir pour nettoyer la forme suivante'''
        for i in range(SUIVANT):
            for j in range(SUIVANT):
                self.dessine_case_suivante(i,j,-1)
                
    def dessine_forme_suivante(self,coords,coul):
        '''VueTetris->none
        dessine la forme suivante'''
        self.nettoie_forme_suivante()
        for elt in coords:
            self.dessine_case_suivante(elt[1]+2,elt[0]+2,coul)
            
        
    def commencer(self):
        '''VueTetris->none'''
        self.__commencer=True
        self.__btn_commencer["text"]="Pause"
        self.__btn_commencer["command"]=self.pause
        self.__btn_commencer["bg"]="red"
        
        return
    
    def debut(self):
        '''VueTetris->booleen
        retourne la valeur de self.__commencer'''
        return self.__commencer
        
    
    def pause(self):
        '''VueTetris->none
        change le texte de bouton commencer en fonction de la pause'''
        self.__pause=not(self.__pause)
        
        if self.__pause:
            self.__btn_commencer["text"]="Reprendre"
            self.__btn_commencer["bg"]="green"
        else:
            self.__btn_commencer["text"]="Pause"
            self.__btn_commencer["bg"]="red"
            
    
            
            
        return
    
    def pause1(self):
        '''VueTetris->boolen
        retourne la valeur de self.__pause'''
        return self.__pause
    
    def reset(self):
        '''VueTetris->none'''
        self.__btn_commencer["text"]="Recommencer"
        self.__btn_commencer["command"]=self.recommencer
        self.__btn_commencer["bg"]="blue"
        return
    
    def recommencer(self):
        '''VueTetris->none'''
        self.__recommencer=True
        return
    
    def recommencer1(self):
        '''VueTetris->boolen
        retourne la valeur de self.__recommencer'''
        return self.__recommencer
    
        
        
        
        
        
        
        
    
  
        
        
    
    
    
    
    
    
        
  
    

    
  
        
        
       
     
        
        
       
   
        
        
        
   
            
    
        
        
        
        
                
                    
        
        