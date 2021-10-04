import numpy as np

class CASE():
    def __init__(self):
        self.Ligne   = 0           #par défaut
        self.Colonne = 0           #par défaut
        self.Contenu = 0           #par défaut
        self.Est_modifiable = True #par défaut
        self.Region  = 0           #par défaut


        
class REGION():
    def __init__(self):

        #initialisation de la liste des cases #chaque région a la forme d'une matrice 3*3
        self.Liste_cases           = [ [0]*3 for i in range (3)]
        for i in range (len(self.Liste_cases)):
            for j in range (len(self.Liste_cases)):
                (self.Liste_cases)[i][j] = CASE()

        #valeur par défaut du numéro de la région
        self.Numero_region = 0           #par défaut



        
class GRILLE():
    def __init__(self , GrilleInitiale):

        self.Grille_initiale = GrilleInitiale

        #initialisation de la liste des cases
              #la grille a la forme d'une matrice 9*9
        self.Liste_cases             = [ [0]*9 for i in range (9)]
        
              #remplissage de la liste des cases par des cases
        for i in range (len(self.Liste_cases)):
            for j in range (len(self.Liste_cases)):
                (self.Liste_cases)[i][j] = CASE()
                
                
                
        #initialisation de la liste des cases modifiables #on va ajouter les cases modifiables
        self.Liste_cases_modifiables = []

        

        #initialisation de la liste des regions
                  #l'ensemble des régions a la forme d'une matrice 3*3
        self.Liste_regions           = [ [0]*3 for i in range (3)]

                  #remplissage de la liste des régions par des régions
        for i in range (len(self.Liste_regions)):
            for j in range (len(self.Liste_regions)):
                (self.Liste_regions)[i][j] = REGION()


        GRILLE.Initialisation_regions(self) #cet algorithme permet d'affecter à chaque région du sudoku, ses attributs
        GRILLE.Initialisation_cases(self)   #cet algorithme permet d'affecter à chaque case de la liste des cases de la grille, ses attributs

        
            
        




    def Initialisation_regions(self):
            M = [ [7,8,9],
                  [4,5,6],
                  [1,2,3] ]
            for i in range(len(M)):
                for j in range(len(M)):
                    #*************affectation des attributs de la region******************
                    region               = (self.Liste_regions)[i][j]
                    region.Numero_region = M[i][j] #M[i][j] est le numéro de la région
                    region.Liste_cases   = ( np.array(self.Liste_cases) )[ i*3:(i+1)*3 , j*3:(j+1)*3 ]



    def Initialisation_cases(self):
            for ligne in range(9):
                for colonne in range (9):
                    #*************affectation des attributs de la case******************
                    case         = (self.Liste_cases)[ligne][colonne]
                    #attribut ligne
                    case.ligne   = ligne

                    #attribut colonne
                    case.colonne = colonne

                    #attribut contenu
                    contenu_case = (self.Grille_initiale)[ligne][colonne]
                    case.Contenu = contenu_case

                    #attribut Est_modifiable
                    if contenu_case == 0:
                        case.Est_modifiable = True
                    else:
                        case.Est_modifiable = False

                    #attribut Region
                    case.Region = (self.Liste_regions)[ligne//3][colonne//3]
        



#initialisation d'un grille sudoku vide
Grille_Vide= GRILLE([ [0]*9 for i in range (9)])

#affichage de la grille
Liste = Grille_Vide.Liste_cases

for i in range (len(Liste)):
    for j in range (len(Liste)):
        case = Liste[i][j] 
    print("\n")




#---------------------------Resolution du sudoku-------------------------------------------------------------------

M = [ [0]*9 for i in range (9)]
Grille = GRILLE(M)



arret = False
for i in range(9):
    
    if arret == True : break
    for j in range(9):
        ListeCases = Grille.Liste_cases
        if arret == True : break

        if ( (Grille.Liste_cases)[i][j] ).Contenu != 0: continue

        CaseEnCours = (Grille.Liste_cases)[i][j]




        NombresDéjàUtilisés = []
        for k in range (9):
            if k == j : continue
            contenu = ( (Grille.Liste_cases)[i][k] ).Contenu
            if contenu != 0:
                NombresDéjàUtilisés.append(contenu)

        for k in range (9):
            if k == i : continue
            contenu = ( (Grille.Liste_cases)[k][j] ).Contenu
            if contenu != 0:
                NombresDéjàUtilisés.append(contenu)


        I = i - i%3
        J = j - j%3 
        for m in range(I,I+3,1):
            for n in range(J,J+3,1):
                if m!=i and n!=j :
                    contenu = ( (Grille.Liste_cases)[m][n] ).Contenu
                    if contenu != 0:
                        NombresDéjàUtilisés.append(contenu)
        


        for nb in range (1,10,1):
            if nb not in NombresDéjàUtilisés:
                CaseEnCours.Contenu = nb
                break
                
        if CaseEnCours.Contenu == 0 :
            arret = True


        


#affichage
for i in range(9):
    for j in range(9):
        case = (Grille.Liste_cases)[i][j]
        print(case.Contenu, end = ' ')
    print("\n")



#------------------------------------------------------------------------------------------------------------------













def Résulotion_AUTRE_METHODE(Matrice):  #Grille est une matrice Sudoku 9*9 qui contient des valeurs=  0 (case modifiable) ou non(case non modifiable)
        Sudoku = GRILLE(Matrice)
        Resolution_Partielle( Sudoku )            #cet algorithme reçoit une grille sudoku et la résoud en la modifiant 
        afficher_grille(Sudoku)         #ce algorithme reçoit une grille sudoku et l'affiche


def afficher_grille(grille):
        Liste = grille.Liste_cases
        
        for i in range (len(Liste)):
                for j in range (len(Liste)):
                        case = Liste[i][j]
                        print(case.Contenu, end = '  ')
                print("\n")


def Absent_ligne(Grille,val,i,j):
        for k in range(0,9):
                case =(Grille.Liste_cases)[i][k]
                if case.Contenu == val and k!=j:
                        return False
        return True

def Absent_Colonne(Grille,val,i,j):
        for k in range(0,9):
                case = (Grille.Liste_cases)[k][j]
                if case.Contenu == val and k!=i:
                        return False
        return True

def Absent_Region(Grille,val,i,j):
        a = i - i%3
        b = j - j%3
        for m in range(a,a+3):
                for n in range(b,b+3):
                        case = (Grille.Liste_cases)[m][n]
                        if case.Contenu == val and m!=i and n!=j:
                                return False
        return True


        
        

def Resolution_Partielle( Grille , position = 1 , Liste = [] ): #position parcoure la liste de 1 à 81; Liste sert à voir les cases qu'on n'a pas pu remplir
        if position == 82: # on sort de la table
                return Liste
        
        i = (position-1)//9 #on indexe la case
        j = (position-1)%9 
        case = (Grille.Liste_cases)[i][j]
        if case.Contenu != 0: #case remplie donc on passe à la case suivante
                return Resolution_Partielle( Grille, position +1 , Liste )

        #ici, la case est non remplie

        for val in range(1,10):
                if Absent_ligne(Grille,val,i,j) and Absent_Colonne(Grille,val,i,j) and Absent_Region(Grille,val,i,j): #on peur remplir cette case
                        case.Contenu = val
                        return Resolution_Partielle( Grille, position +1 , Liste ) #case remplie donc on passe à la case suivante

        # on ne peut pas remplir la case donc on ajoute cette position à la liste des positions correspondant aux cases qui n'ont pas trouvée de valeur
        Liste.append(position)
        return Resolution_Partielle( Grille, position +1 , Liste )

'''
grille = [[0]*9 for i in range(9)]
S = Resolution_Partielle(grille)
Liste = grille
for i in range (len(Liste)):
    for j in range (len(Liste)):
        case = Liste[i][j]
        print(case, end = '  ')
    print("\n")
'''

Matrice = [[0]*9 for i in range(9)]
Résulotion_AUTRE_METHODE(Matrice)

'''	def Est_non_vide(position):

        if position == 82: # on sort de la table
                return True
        
        i = position//9 #on indexe la case
        j = position%9

        if Grille[i][j] != 0: #case remplie donc on passe à la case suivante
                return Est_vide(position + 1)

        

        for val in range(1,10):
                if Absent_ligne(val,i) and Absent_colonne(val,j) and Absent_bloc(val,i,j):
                        grille[i][j] = val
                        return Est_vide(position + 1)
                        

        return False

def nb_position(i,j):
        a = 0
        for val in range (0,9):
                if Absent_ligne(val,i) and Absent_colonne(val,j) and Absent_bloc(val,i,j):
                        a += 1
        return a'''





        
m = input()
