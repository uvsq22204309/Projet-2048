# Projet-2048

Bienvenue sur le projet 2048
auteurs : Dorian Le Guillou, Anaé ratabouil, William Dang
L1 MI TD2
2022/2023

Pour mener à bien la réalisation de ce projet nous allons suivre le plan suivant : 

- importation de la librairie tkinter : 
  - définition des dimensions du plateau, de la tuile
  - définition de ces paramètres et des boutons de jeu à l'aide de Tkinter
- et random (pour faire apparaître une tuile 2 ou 4)

- noter les coordonnéees de toutes les tuiles et les mettres dans un dictionnaire
- définir un plateau vide 
- définir score de départ à 0
- définir les fonctions de jeu :
  - défaite
  - remplace
  - recommencer
  - quitter, destroy
  - afficher score
  - déplacer vers le haut, bas, gauche, droit avec les touches :
    - Z pour haut, Q pour gauche, S pour bas, D pour droite (clavier azerty)



optionel :
- couleur
- coder une AI

Pour gérer le déplacement :
Tout d'abord, on observe ligne par ligne, et on déplace tous les entiers non nuls, jusqu’au « mur », vers la gauche.
Ensuite, on additionne deux tuiles, en partant de la gauche, si et seulement si elles ont la même valeur.
- Par exemple :
[2, 0, 2, 2] -> [2, 2, 2, 0] -> [4, 2, 0, 0]
