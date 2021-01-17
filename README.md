# TP3-SpaceInvaders

# Binôme : Elisa BEAUCAMP, Mathurin LEMARIE (3-ETI : Groupe-C)

=======================================================
Lien github : https://github.com/elisabeaucamp/TP3-SpaceInvaders
Pour lancer le jeux : lancer le fichier main

=======================================================

- Ce que l'on a fait :
	- Un menu de lancement de jeux, dans lequel on peut accéder à une fenêtre "à propos" ou quitter le jeux. Dans ce menu, on retrouve un bouton "quitter" et un bouton "nouvelle partie".
	- Une fenêtre de jeux dans laquelle se trouve l'interface du jeux (canevas) ainsi qu'une fenêtre d'informations (on retrouve dans cette fenêtre : les points de vie du joueur, le score du joueur, un bouton quitter et un bouton de lancement du jeux).
	- Le joueur contrôle un vaisseau à l'aide des flèches droite et gauche. Il peut tirer à l'aide de la barre espace.
	- Des ilots sont présents pour protéger le joueur. Ce dernier peut cependant les détèriorer en tirant dessus.
	- Une "grille" d'aliens se déplace de gauche à droite. Ils descendent légèrement vers le bas lorsque qu'un allé-retour a été fait.
	- Les aliens tirent à chaque fois qu'ils se déplacent. Ils ont 50% de chance de tirer.
	- Le score s'incrémente de 10 en 10 dès que l'on a touché un alien.
	- Le joueur perd si un alien arrive à atteindre le niveau des ilots ou si le joueur à 0 points de vie.
	- Le joueur gagne si il a touché tous les aliens.

- Ce qu'il reste à faire :
	- Nous n'avons pas pu implémenter un alien "bonus" qui a un comportement différent.
	- Les aliens sont encore sous la forme de carrés, une image pour changer la forme se trouve dans le dossier "Images" mais nous n'avons pas réussi à les appliquer sur les aliens.
