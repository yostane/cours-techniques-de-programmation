# Projet médiathèque à faire en TypeScript

## Partie 1

Faire en TypeScript un programme de gestion d’une médiathèque. On doit pouvoir stocker différents types de Média : audio, vidéo, texte.

-   Les audio et vidéo peuvent être écoutés, le texte peut être lu et les vidéos peuvent visualisées.
-   Chaque objet d’un de ces médias doit avoir au minimum un nom, un format, une taille.
-   On veut pouvoir faire le trie selon certains critères des objets stockés.
-   Un texte contient en plus une propriété "contenu" ainsi que deux propriétés calculées, la première renvoie le nombre de consonnes du contenu, la deuxième le nombre de mots du contenu.
-   La médiathèque est un singleton.

**A faire:** Faire en TypeScript un programme de gestion d’une médiathèque contenant deux audios, une vidéo et trois textes.

## Partie 2

-   On souhaite aussi stocker stocker des textes audio qui sont des textes qu'on peut écouter.

**A faire:**

-   Donner le diagramme de classes UML de cette médiathèque.
-   Ajouter deux textes audio dans la médiathèque

**## Partie 3:**

On souhaite simuler l'interaction des humains avec la médiathèque. Chaque jour, une seule personne entre dans la médiathèque et ressort le même jour. Chaque personne effectue une seule action puis ressort. On suppose qu'il n'y a qu'une seule personne dans la médiathèque à la fois et peut effectuer une de ces actions:

-   Louer un film. Un film loué sera rendu deux jours après.
-   Ecouter une vidéo, un audio ou texte audio.
-   Louer un texte ou texte audio. Un texte loué sera rendu 4 jours après.

Ecrire un programme qui réalise cette simulation pendant 30 jours. A la fin du mois, afficher des statistiques sur le nombre de films et textes loués ainsi que le nombre d'éléments écoutés.
