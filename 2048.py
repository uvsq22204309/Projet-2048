"""
##########################################

Projet 2048
L1 MI TD2
2022/2023
Dorian Le Guillou, Anaé Ratabouil, William Dang

##########################################
"""
# importation des modules
import tkinter as tk
import random as rd


# Création d'une fenêtre et de son nom
fenetre = tk.Tk()
fenetre.title('2048')

label_title = tk.Label(fenetre, text = "2048", font = ("Courrier", 20), bg = "#ECCE0F", fg = "#FFFFFF")
label_title.pack()

# Personnalisation de la fenêtre
fenetre.geometry("500x500") #taille de base
fenetre.minsize(800,600)
fenetre.iconbitmap("2048/2048Icon.ico") #ajout du logo
fenetre.config(background="#FFDD33") # couleur brun, code héxadécimal

#Définiton longeur case
taille_case = 100

#Définiton du score
score = 0

# Création d'un canevas 395x395 pixels
canvas = tk.Canvas(fenetre, width=395, height=395, borderwidth=2, relief="solid")

#Afficher le score
score_label = tk.Label(fenetre, text="Score : " + str(score))
score_label.pack()

#Listes pour stocker les carrées
liste_carre = []
liste_carre_disponible = []

# dictionnaire des couleurs en héxadécimal
colors = {
        2 : "#A7A7A7",
        4 : "#DCD781",
        8 : "#F3A246",
        16 : "#F7721C",
        32 : "#F7441C",
        64 : "#F72D1C",
        128 : "#DEDB0A",
        256 : "#EFEC0B",
        512 : "#FFD903",
        1024 : "#E0C841",
        2048 : "#FFFB00",
        4096: "#707066",
        8192: "#5A5A51",
        16384: "#44443D",
        32768: "#34342E",
        65536: "#272723",
        131072: "#131311",
        }

#La fonction qui augmente le score
def augmenter_score():
    global score
    score += 1
    score_label.config(text="Score : " + str(score))

def haut():
    for i in range(len(liste_carre_indisponible)):
        if liste_carre_indisponible[i][0] != 0: 
            for j in range(liste_carre_indisponible[i][1]):
                localistation = []
                localistation.append(liste_carre_indisponible[i][0])
                localistation.append(j)
                print("loc", localistation)
                if localistation in liste_carre_disponible:
                    #La condition ne marche pas mais je ne comprends pas pourquoi
                    print("enfin")   
                    liste_carre_disponible.append(liste_carre_indisponible[i])
                    liste_carre_indisponible.remove(liste_carre_indisponible[i])
                    liste_carre_indisponible.append(localistation)
                    liste_carre_disponible.remove(localistation)
                    
            '''la fonction est pas encore parfaite mais j'ai un bon proto'''  
    chiffre_dans_une_case()



def bas():
    "fonction qui déplace les tuiles vers le bas"
    pass


def gauche():
    "fonction qui déplace les tuiles vers la gauche"
    pass


def droite():
    "fonction qui déplace les tuiles vers la droite"
    pass

# Boutons
left_button = tk.Button(fenetre, text="Q", command=gauche, fg = "black", font=("Courier","20"))
right_button = tk.Button(fenetre, text="D", command=droite, fg = "black", font=("Courier","20"))
up_button = tk.Button(fenetre, text="Z", command=haut, fg = "black", font=("Courier","20"))
down_button = tk.Button(fenetre, text="S", command=bas, fg = "black", font=("Courier","20"))

left_button.place(relx = 0.8, rely = 0.5)
right_button.place(relx = 0.9, rely = 0.5)
up_button.place(relx = 0.85, rely = 0.45)
down_button.place(relx= 0.85, rely = 0.55)

# Dessiner le carré avec des dimensions de taille_casextaille_case pixels pour chaque case
for i in range(4):
    for j in range(4):
        carre = canvas.create_rectangle(i*taille_case, j*taille_case, (i+1)*taille_case, (j+1)*taille_case)
        #Récuperer les coordonnées de chaque carrés
        liste_carre.append(canvas.coords(carre))



'''for carre in liste_carre:
    print("Rectangle {} à pour coord {}".format(carre, canvas.coords(carre)))
'''

#Initialisation de la liste des carrés disponibles
liste_carre_disponible = [(i,j) for i in range(4) for j in range(4)]
liste_carre_indisponible = []

def chiffre_dans_une_case():
    global liste_carre_disponible
    if liste_carre_disponible:
        # Choisir un carré aléatoire disponible
        choix = rd.choice(liste_carre_disponible)
        liste_carre_indisponible.append(choix)
        liste_carre_disponible.remove(choix)
        print("liste carré dipso", liste_carre_disponible)
        print("liste pas dispo",liste_carre_indisponible)
        if len(liste_carre_disponible) == 0:
            print("-----------------\nDéfaite\nFermeture de la fenêtre\nVotre de score est de {}\n-----------------".format(score))
            fenetre.quit()
        # Générer un "2" ou un "4" aléatoirement et l'afficher dans le carré choisi
        valeur_aleatoire = rd.choice([2]*9+[4])
        x1, y1, x2, y2 = liste_carre[choix[0] * 4 + choix[1]]
        x_centre = (x1 + x2) / 2
        y_centre = (y1 + y2) / 2
        canvas.create_text(x_centre, y_centre, text=valeur_aleatoire, font=("Arial", 24, "bold"))


# Ajouter le canevas à la fenêtre
canvas.pack(expand=True)

#Détéction de touches
fenetre.bind('<z>', haut)
fenetre.bind('<q>', gauche)
fenetre.bind('<s>', bas)
fenetre.bind('<d>', droite)
'''Je comprend pas l'erreur sur la detect des touches'''


# Execution des définitions:
chiffre_dans_une_case()
chiffre_dans_une_case()

# Lancer la boucle principale de la fenêtre
fenetre.mainloop()
