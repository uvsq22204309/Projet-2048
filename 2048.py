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
import keyboard

# Création d'une fenêtre et de son nom
fenetre = tk.Tk()
fenetre.title(2048)

label_title = tk.Label(fenetre, text = "2048", font = ("Courrier", 20), bg = "#ECCE0F", fg = "#FFFFFF")
label_title.pack()

# Personnalisation de la fenêtre
fenetre.geometry("500x500") #taille de base
fenetre.iconbitmap("2048Icon.ico") #ajout du logo
fenetre.config(background="#FFDD33") # couleur brun, code héxadécimal

#Définiton longeur case
taille_case = 100

#Définiton du score
score = 0

# Création d'un canevas 200x200 pixels
canvas = tk.Canvas(fenetre, width=395, height=395, borderwidth=2, relief="solid")

#Afficher le score
score_label = tk.Label(fenetre, text="Score : " + str(score))
score_label.pack()

#Liste pour stocker les carrées
liste_carre = []

#La fonction qui augmente le score
def augmenter_score():
    global score
    score += 1
    score_label.config(text="Score : " + str(score))

# Dessiner le carré avec des dimensions de taille_casextaille_case pixels pour chaque case
for i in range(4):
    for j in range(4):
        carre = canvas.create_rectangle(i*taille_case, j*taille_case, (i+1)*taille_case, (j+1)*taille_case)
        #Récuperer les coordonnées de chaque carrés
        liste_carre.append(canvas.coords(carre))


'''for carre in liste_carre:
    print("Rectangle {} à pour coord {}".format(carre, canvas.coords(carre)))
'''

liste_carre_disponible = [i for i in liste_carre]
#Apparition aléatoire d'un 2
def nouvelle_case(nb):
    for i in range(nb):

        nb_aleatoire = rd.randint(0, len(liste_carre_disponible)-1)
        x = liste_carre_disponible[nb_aleatoire][0]
        y = liste_carre_disponible[nb_aleatoire][2]

        liste_valeur_aleatoire = [2 for i in range(9)]
        liste_valeur_aleatoire.append(4)
        valeur_aleatoire = rd.choice(liste_valeur_aleatoire)
        print(valeur_aleatoire)
        
        r_nb, g_nb, b_nb = 119,110,101
        color_nb = f'#{r_nb:02x}{g_nb:02x}{b_nb:02x}'

        if valeur_aleatoire == 2:  
            r, g, b = 238,228,218
            color = f'#{r:02x}{g:02x}{b:02x}'
            canvas.create_text(x+(taille_case/2), y-(taille_case/2), text=valeur_aleatoire, fill=color_nb, font=("Arial", 24, "bold"))
            #canvas.create_rectangle(liste_carre_disponible[nb_aleatoire][0],liste_carre_disponible[nb_aleatoire][2],liste_carre_disponible[nb_aleatoire][3],liste_carre_disponible[nb_aleatoire][3], fill=color)
        elif valeur_aleatoire == 4:
            canvas.create_text(x+(taille_case/2), y-(taille_case/2), text=valeur_aleatoire, fill=color_nb, font=("Arial", 24, "bold"))

        print(liste_carre_disponible[nb_aleatoire])
        liste_carre_disponible.remove(liste_carre_disponible[nb_aleatoire])

# La fonction qui détermine la direction
def determine_direction():
    if keyboard.is_pressed('d'):
        return 'droite'
    if keyboard.is_pressed('q'):
        return 'gauche'
    if keyboard.is_pressed('z'):
        return 'haut'
    if keyboard.is_pressed('s'):
        return 'bas'

direction = determine_direction()
print(direction)

# Ajouter le canevas à la fenêtre
canvas.pack()

# Execution des définitions:
nouvelle_case(2)

# Lancer la boucle principale de la fenêtre
fenetre.mainloop()
