# Exercices: série 1

## Classes

### Exercice 1

=== "Python"

    Définir une classe `Book` avec les propriétés suivantes Python: `nb_pages: number, `title`: string, `author`: string, `isbn`: string` ([ISBN (The International Standard Book Number)](https://en.wikipedia.org/wiki/ISBN)) et `marked_page: number`.

    - Dans la classe `Book`, définir une méthode `mark_page(self, page)` qui permet de mettre à jour la valeur de `marked_page` avec la valeur de l'argument `page`. ⚠ bien vérifier que `page` soit < à `nb_pages`.
    - Créer une classe `Library` (Bibliothèque) qui contient un tableau de livres qui est passé au constructeur. ⚠ Il y'a une relation entre `Library` et `Book` mais ce n'est pas une relation d'héritage. Pour ce cas, on dit que c'est une **agrégation**.
    - Dans la classe `Library`, définir une méthode `list_authors()` qui retourne un tableau contenant uniquement les noms des auteurs.
    - Dans la classe `Library`, définir une méthode `sum_of_marked_pages()` qui retourne la somme des `marked_page` de tous les livres.
    - Instancier une `Library` avec trois livres
    - Afficher les résultats des appels des méthodes `list_authors()` et `sum_of_marked_pages()`.
    - Est-ce que la classe `Book` peuvent exister et être utilisée indépendamment de `Library` ?

=== "TypeScript"

    Définir une classe `Book` avec les propriétés suivantes en `readonly`: `nbPages: number, author: string, isbn: string` ([ISBN (The International Standard Book Number)](https://en.wikipedia.org/wiki/ISBN)) et en `protected`: `markedPage: number`.

    - Dans la classe `Book`, définir une méthode `markPage(page: number)` qui permet de mettre à jour la valeur de `markedPage` avec la valeur de l'argument `page`. ⚠ bien vérifier que `page` soit < à `nbPages`.
    - Créer une classe `Library` (Bibliothèque) qui contient un tableau de livres. ⚠ Il une relation entre `Library` et `Book` mais ce n'est pas une relation d'héritage. Pour ce cas, on dit que c'est une **agrégation**.
    - Dans la classe `Library`, définir une méthode `listAuthors()` qui retourne un tableau contenant uniquement les noms des auteurs.
    - Dans la classe `Library`, définir une méthode `sumOfMarkedPages()` qui retourne la somme des `markedPage` de tous les livres.
    - Instancier une `Library` avec trois livres
    - Afficher les résultats des appels des méthodes `listAuthors()` et `sumOfMarkedPages()`.
    - Est-ce que la classe `Book` peuvent exister et être utilisée indépendamment de `Library` ?

??? "Solution en Python"

    ```py
    --8<--
    python/ex_library.py
    --8<--
    ```

### Exercice 2

On souhaite représenter des montres et les personnes qui les portent.

Une montre donne l'heure et les minutes. On peut initialiser une montre soit à partir d'un couple heure/minute donné, soit par clonage (en créant une nouvelle montre à partir d'une montre existante). Il doit être possible de faire **avancer** l'heure d'une montre en ajoutant une minute (attention, les minutes sont limitées à 60 et les heures à 24).

Une personne a un nom et peut éventuellement porter une montre. Une personne peut **porter** une montre donnée, si elle n'en a pas déjà une. Elle peut aussi **enlever** sa montre si elle en a une. Une personne peut **demander l'heure** à une autre, qui lui donne l'heure sous forme d'une chaine de caractères, en consultant sa montre si elle en a une (sinon elle peut retourner une chaine vide).

1. Écrivez une classe qui représente les montres telles que décrites ci-dessus.
1. Créer une montre affichant 13h45 et une autre montre qui est un clone de la première.
1. Écrivez une classe qui représente les personnes telles que décrites ci-dessus.
1. On veut faire en sorte que chaque montre ne soit portée que par une seule personne. Proposer des ajouts/modifications des deux classes précédentes pour garantir cela.
1. Dorénavant, une personne peut porter une montre qui peut être mécanique ou numérique. En utilisant l'héritage, modifier le programme pour prendre ce cas en compte.

??? "Solution en TS"

    ```ts
    --8<--
    poo_ex4.ts
    --8<--
    ```

??? "Solution en Python"

    ```py
    --8<--

    --8<--
    ```

### Exercice 3

On veut réaliser un programme de gestion des recettes de cuisine. La classe `Ingredient` contient ces membres:

- `name`, `state` et `unit` de type `string`
- `quantity` de type `number`
- Le constructeur initialise les propriétés ci-dessus via 4 arguments qui lui seront passés.

L'état d'un ingrédient (son `state`) peut être: `cooked` (cuit), `raw` (cru), `whole` (entier), ou `cut` (découpé) ou une combinaison de ces états (par exemple cuit et entier). L'unité peut être une unité de poids (`g`, `kg`, etc), de volume (`l`, `ml`, `cl`) ou simplement une `cadrinality` (cardinalité ou nombre de pièces).

La classe `Dish` (plat) représente les plats, chaque plat ayant un nom et une liste d'ingrédients. On doit pouvoir créér un plat avec son nom.

1. Définir les classe `Ingredient` et `Dish`
1. Créer un plat appelé choucroute contenant comme ingrédients : 500g de choucroute cuite, 150g de lard cuit et entier et 2 saucisses entières et cuites
1. On veut pouvoir comparer les plats et donc leurs ingrédients. Ajoutez une méthode `equals` dans la classe Ingrédient qui renvoie true si deux ingrédients ont le même nom d'aliment et le même état (pas forcément la même quantité).
1. Ajoutez une méthode `equals` dans la classe `Dish` qui prend en argument un plat, qui renvoie true si deux plats contiennent les mêmes ingrédients, au sens donné juste avant.
    - Si vous faites l'exercice en Python, appeler plutôt cette méthode `__eq__`. Comparer des plats avec le `==`. Que constatez vous ?

## Héritage

### Exercice 3 (suite)

1. On veut faire la distinction entre les ingrédients qu'on peut cuire et ceux qu'on peut découper. Un ingrédient qu'on peut cuire doit avoir une méthode `cook()` qui le fait passer dans l'état `cooked` et une température de cuisson. Un ingrédient qu'on peut découper doit avoir une méthode `cut()` qui le fait passer dans l'état `cut`.
    - En utilisant uniquement l'héritage, proposer une solution à ce problème
    - En utilisant utilisant l'héritage et les interfaces, proposer une solution alternative à ce problème
    - Laquelle des deux solutions vous semble la meilleure ?

### Exercice 4

!!! important

    Cet exercice est purement théorique. Aucun code n'est demandé.

L'héritage est une relation **est**. Par exemple, dans un jeu vidéo, si on suppose qu'un `Human` **est** `Character` (personnage) et qu'un `Monster` (monstre) **est** aussi un `Character`, on écrira `Human extends Character` et `Monster extends Character`.

- Donner deux exemples de relation d'héritage.
- Trouver les relations d'héritage possibles:
  - Être vivant, homme, animal
  - Meuble, fauteuil, Armoire, Table, Jardin
  - Aliment, Pâtisserie, Mille-Feuilles, Croissant, Pain

### Exercice 5

Essayer de modéliser une classe parente commune (qu'on appelle aussi classe mère) pour ces classes:

- Ordinateur portable, ordinateur fixe
- Ordinateur portable, ordinateur fixe, Switch, Xbox, Playstation
- Voiture, Camion, Vélo, Trottinette

## Sources et références

- [Exercices de Programmation Orientée Objet en Java - MIS](https://home.mis.u-picardie.fr/~furst/docs/exercicesPOO.pdf)
