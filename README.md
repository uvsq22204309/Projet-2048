# Projet-2048

Bienvenue sur le projet 2048 !
- auteurs : Dorian Le Guillou, Anaé ratabouil, William Dang
- L1 MI TD2
- 2022/2023

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

__Structure :__
La grille de jeu se présente sous la forme d'un tableau à deux dimensions avec 4 lignes et 4 colonnes. Les éléments sont des puissances de 2 (au moins égales à 2) ou 0 si la tuile est vide.

__Déroulement du jeu :__
Au départ, on a une grille contenant 2 valeurs prises dans {2,4}. 
L’utilisateur doit alors faire bouger les tuiles, jusqu’au « mur », vers la gauche, la droite, le haut ou le bas, ce déplacement implique un nombre fini d'additions de tuiles. Et suite à un de ces déplacement, une des tuiles vides prend la valeur 2 ou 4 de manière aléatoire.
Le jeu se termine si aucun déplacement ne peut faire évoluer la grille.

__Déplacement :__
1) à gauche :
Tout d'abord, on observe ligne par ligne, et on déplace tous les entiers non nuls, jusqu’au « mur », vers la gauche.
Ensuite, on additionne deux tuiles, en partant de la gauche, si et seulement si elles ont la même valeur.
- Par exemple :
[2, 0, 2, 2] -> [2, 2, 2, 0] -> [4, 2, 0, 0]

- 2 ) à droite 
de même en considérant la valeur aléatoire

__Donc ce qui nous donne l'algorithme suivant :__
- Si a = b
  - Si c = d
    - La ligne devient [2 * a ,2 * c ,0 ,0] 
  - Sinon (c différent de d)
    - La ligne devient [2* a,c ,d , 0] 
- Sinon ( cas a != b )
  - Si b = c
    - La ligne devient [a , 2 * b ,d ,0] 
  - Sinon ( b différent de c )
    - Si c = d
      - La ligne devient [a , b, 2 * c, 0] 
    - Sinon ( c différent d )
      - La ligne devient [a, b, c, d]
