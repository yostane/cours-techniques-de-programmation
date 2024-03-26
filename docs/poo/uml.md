# Les diagrammes de classe

La phase de conception permet de se préparer au mieux au développement.
Parmi les tâches de cette phase est la définition des différents algorithmes, l'identification des données nécessaires au bon fonctionnement du projet, etc.
Dans ce chapitre, nous allons étudier un aspect important de la conception en POO: les diagrammes de classe.

Un diagramme de classe est tout dessin qui permet de représenter: les classes, les interfaces ainsi que leurs relations (héritage, implémentation, composition, agrégation). Il existe plusieurs façons de dessiner un diagramme, un des standard les plus connus sont les **diagrammes de classe UML**.

## Rappel des relations

- Héritage: relation "est un"
- Implémentation: nom de l'héritage pour les interfaces
- Composition: A a une ou plusieurs instances de B et B est détruit si A est détruit (en d'autres termes B dépend A). Exemple: les chambres d'une maison.
- Agrégation: A a une ou plusieurs instances de B et B n'est pas forcément détruit si A est détruit (en d'autres termes B ne dépend pas de A). Exemple: le moteur d'une voiture.
- Association:
    - Association unidirectionnelle: A peut appeler les méthodes et propriétés de B mais pas l'inverse
    - Association bidirectionnelle: A peut appeler les méthodes et propriétés de B et inversement
    - Association avec soi-même: A peut appeler les méthodes et propriétés de d'une autre instance de A

## Les diagrammes de classe UML

UML est une norme qui définit comment représenter différents types de diagrammes.
Parmi ces différents types de diagrammes, on trouve les diagrammes de classe.
[Cet aide-mémoire](https://khalilstemmler.com/articles/uml-cheatsheet/) permet de voir les grandes lignes.

## Exemple 1

![Exemple UML](./img/uml01.drawio.svg)

??? "Ce code illustre la relation d'association `soigner` et `eat` uniquement"

    ```py
    --8<--
    python/association_demo01.py
    --8<--
    ```

## Exemple 2

![Exemple UML](./img/uml02.drawio.svg)

Ce diagramme permet d'obtenir le code suivant:

```py title="Code correspondant du diagramme UML"
    --8<--
    python/uml02.py
    --8<--
```

## Exercices

Pour dessiner les diagrammes UML, vous pouvez-utiliser [diagrams.net](https://www.diagrams.net/) ou [cette extension VSCode](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio).

### Exercice 1

Dessiner le diagramme de classes UML pour chacun groupe de classes (1 diagramme par cas):

- Meuble, Armoire, Table, Jardin, Chambre, Maison
- Pâtisserie, Mille-Feuilles, Pain, Farine, Sel, Sucre
- Voiture, Camion, Vélo, Roue, Moteur, Volant
- Voiture, Berline, SUV, Roue, Moteur, Personne, Commercial, Mécanicien, GarageAutomobile

Coder en python un des cas.

#### Solution du dernier cas

![Exemple UML](./img/ex1-garage.drawio.svg)

??? "Solution en Python"

    ```py
    --8<--
    python/exo_uml_garage.py
    --8<--
    ```

### Exercice 2

Soit le diagramme UML suivant:

![Exemple UML](./img/uml02.drawio.svg)

Apporter les modifications suivantes au diagramme:

- L'être humain a un corps. Ce dernier a un cerveau, des mains et un coeur.
- Un animal est un être vivant qui a aussi un corps
- Une plante est un être vivant (qui n'a pas de corps)

### Exercice 3

Modéliser en UML les diagrammes de classe des cas suivants:

- Une école
- Un garage de mécanicien
- Un jeu de combat en 1v1
- Les exercices précédents

Une fois les diagrammes réalisés, coder en TS et créer quelques objets.
