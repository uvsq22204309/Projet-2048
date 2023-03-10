import tkinter as tk
import random as rd

# Création d'une fenêtre et de son nom
fenetre = tk.Tk()
fenetre.title(2048)

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
print(liste_carre)

#Apparition aléatoire d'un 2

x =liste_carre[rd.randint(0,15)][0]
y = liste_carre[rd.randint(0,15)][2]

canvas.create_text(x+(taille_case/2), y-(taille_case/2), text="2", fill="red", font=("Arial", 24, "bold"))

# Ajouter le canevas à la fenêtre
canvas.pack()

#Défintion des mouvements

# Lancer la boucle principale de la fenêtre
fenetre.mainloop()


