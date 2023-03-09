# La programmation orientée objet (POO)

## Motivation

Voyons intérêt de la poo à travers cet exercice: nous souhaitons gérer une liste de monstres dans un jeu. Chaque monstre est défini par ces deux **propriétés**: son nom et ses points de vie (PV ou HP). On veut définir une fonction qui permet d'afficher si on monstre est vivant ou mort (selon ses PV).

Si on veut faire cet exercice de façon naïve et sans utiliser l'orienté objet, on utiliserait une variable pour chaque monstre et pour chacune de ses propriétés. Cela donnerait ce code:

```ts
--8<--
motivation_no_oop.ts
--8<--
```

Quels inconvénients voyez-vous dans ce code ?

??? "Quelque réponses"

    -   Il faut changer la signature de la fonction dès qu'on apporte des modifications aux propriétés (renommage, ajoute, suppression)
    -   Pour chaque monstre, il faut manipuler (nbPropriétés * nbMonstres) variables
    -   Placer des monstres dans une liste est compliqué et encourage le risque d'erreurs
        - Par exemple, le fait d'avoir des types hétérogènes dans une liste est complexe à gérer

Une technique de programmation qui permet de palier à cela est la programmation orientée objet qu'on abrégera poo dans la suite.
L'exercice, donnera cela en poo:

```ts
--8<--
motivation_with_oop.ts
--8<--
```

Quels avantages et inconvénients voyez-vous dans ce code ?

??? "Quelque réponses"

    -   Inconvénients
        -   Nouvelle syntaxe à apprendre avec de nouveaux mots: class, readonly, this
    -   Avantages (qui prennent le dessus sur les inconvénients)
        -   Le code qui concerne les monstres est mis ensemble. On parle **d'encapsulation**
        -   La gestion d'une liste de monstres est plus lisible et simple
        -   La fonction checkAlive est plus simple à maintenir si on change des propriétés

## Vue d'ensemble

-   La poo permet de modéliser les éléments qu'on veut traiter sous forme d'**objets**.
-   Un objet contient des **membres** (propriétés et méthodes).
-   Un objet peut être **créé** (ou **instancié**) de différentes façons:
    -   Les techniques communes: à partir d'une **classe** ou objets **littéraux**.
    -   Techniques avancées: Singletons, monteurs (Builders), Injection de dépendances.

### Exercice

Dans le code donné plus haut, identifier avec des commentaires les parties qui effectuent les opération suivantes: instanciation d'objet, définition d'une classe, définition d'une propriété, définition d'une méthode et appel d'une méthode.

??? "Solution"

    -   Définition d'une classe: `class Monster {}`
    -   Instanciation d'objet: `new Monster("Lapinou", 100);` et `new Monster("Chatounet", 0);`
    -   Définition de propriétés: `readonly name: string, readonly hp: number`
    -   Appel d'une méthode: `monster1.checkAlive();` et `monster2.checkAlive();`

## Classes et héritage simple

-   Une classe définit l'ensemble des membres ses instances auront.
-   Une classe peut être définie:
    -   A partir de zéro,
    -   Ou à partie d'une autre classe. :bulb: Cette technique s'appelle **l'héritage simple**,
    -   Ou à partie de plusieurs classes. :bulb: Cette technique s'appelle **l'héritage multiple**. :boom: Très peu de langages proposent cette option.
-   Une classe peut aussi implémenter des interfaces.
-   Le **constructeur** est la première fonction qui est appelée lors de l'instanciation d'un objet.
    -   Certains constructeurs permettent d'initialiser les propriétés avec peu de code.
-   Certains langages permettent de définir des **modificateurs de visibilité** pour ses membres. Voici les plus communs:
    -   `private`: membre utilisable uniquement par sa classe.
    -   `protected`: membre utilisable uniquement par sa classe ou celles qui en héritent.
    -   `public`: membres utilisables depuis n'import où.
-   D'autres modificateur peuvent être proposés selon le langage:
    -   `abstract`: rend le membre abstrait
    -   `readonly`: propriété publique en lecture seule (comme un `const`)
    -   `static`: le membre existera tout le temps en un exemplaire accessible avec le nom de la classe

```ts title="Définition de deux classes dont une qui hérite de l'autre"
--8<--
classes.ts
--8<--
```

## Exercices

### Exercice 1

Définir une classe `Book` avec les propriétés suivantes en `readonly`: `nbPages: number, author: string, isbn: string` ([ISBN (The International Standard Book Number)](https://en.wikipedia.org/wiki/ISBN)) et en `protected`: `markedPage: number`.

-   Dans la classe `Book`, définir une méthode `markPage(page: number)` qui permet de mettre à jour la valeur de `markedPage` avec la valeur de l'argument `page`. ⚠ bien vérifier que `page` soit < à `nbPages`.
-   Créer une classe `Library` (Bibliothèque) qui contient un tableau de livres. ⚠ Il une relation entre `Library` et `Book` mais ce n'est pas une relation d'héritage. Pour ce cas, on dit que c'est une **agrégation**.
-   Dans la classe `Library`, définir une méthode `listAuthors()` qui retourne un tableau contenant uniquement les noms des auteurs.
-   Dans la classe `Library`, définir une méthode `sumOfMarkedPages()` qui retourne la somme des `markedPage` de tous les livres.
-   Instancier une `Library` avec trois livres
-   Afficher les résultats des appels des méthodes `listAuthors()` et `sumOfMarkedPages()`.
-   Est-ce que la classe `Book` peuvent exister et être utilisée indépendamment de `Library` ?

### Exercice 2

!!! important

    Cet exercice est purement théorique. Aucun code n'est demandé.

L'héritage est une relation **est**. Par exemple, dans un jeu vidéo, si on suppose qu'un `Human` **est** `Character` (personnage) et qu'un `Monster` (monstre) **est** aussi un `Character`, on écrira `Human extends Character` et `Monster extends Character`.

-   Donner deux exemples de relation d'héritage.
-   Trouver les relations d'héritage possibles:
    -   Être vivant, homme, animal
    -   Meuble, fauteuil, Armoire, Table, Jardin
    -   Aliment, Pâtisserie, Mille-Feuilles, Croissant, Pain

### Exercice 3

Essayer de trouver ou d'inventer une classe parent commune (qu'on appelle aussi classe mère) pour ces classes:

-   Ordinateur portable, ordinateur fixe
-   Ordinateur portable, ordinateur fixe, Switch, Xbox, Playstation
-   Voiture, Camion, Vélo, Trottinette

### Exercice 4

On souhaite représenter des montres et les personnes qui les portent.

Une montre donne l'heure et les minutes. On peut initialiser une montre soit à partir d'un couple heure/minute donné, soit par clonage (en créant une nouvelle montre à partir d'une montre existante). Il doit être possible de faire **avancer** l'heure d'une montre en ajoutant une minute (attention, les minutes sont limitées à 60 et les heures à 24).

Une personne a un nom et peut éventuellement porter une montre. Une personne peut **porter** une montre donnée, si elle n'en a pas déjà une. Elle peut aussi **enlever** sa montre si elle en a une. Une personne peut **demander l'heure** à une autre, qui lui donne l'heure sous forme d'une chaine de caractères, en consultant sa montre si elle en a une (sinon elle peut retourner une chaine vide).

1. Écrivez une classe qui représente les montres telles que décrites ci-dessus.
1. Créer une montre affichant 13h45 et une autre montre qui est un clone de la première.
1. Écrivez une classe qui représente les personnes telles que décrites ci-dessus.
1. On veut faire en sorte que chaque montre ne soit portée que par une seule personne. Proposer des ajouts/modifications des deux classes précédentes pour garantir cela.
1. Dorénavant, une personne peut porter une montre qui peut être mécanique ou numérique. En utilisant l'héritage, modifier le programme pour prendre ce cas en compte.

??? "Solution"

    ```ts
    --8<--
    poo_ex4.ts
    --8<--
    ```

### Exercice 5

On veut réaliser un programme de gestion des recettes de cuisine. La classe `Ingredient` contient ces membres:

-   `name`, `state` et `unit` de type `string`
-   `quantity` de type `number`
-   Le constructeur initialise les propriétés ci-dessus via 4 arguments qui lui seront passés.

L'état d'un ingrédient (son `state`) peut être: `cooked` (cuit), `raw` (cru), `whole` (entier), ou `cut` (découpé) ou une combinaison de ces états (par exemple cuit et entier). L'unité peut être une unité de poids (`g`, `kg`, etc), de volume (`l`, `ml`, `cl`) ou simplement une `cadrinality` (cardinalité ou nombre de pièces).

La classe `Dish` (plat) représente les plats, chaque plat ayant un nom et une liste d'ingrédients. On doit pouvoir créér un plat avec son nom.

1. Définir les classe `Ingredient` et `Dish`
1. Créer un plat appelé choucroute contenant comme ingrédients : 500g de choucroute cuite, 150g de lard cuit et entier et 2 saucisses entières et cuites
1. On veut pouvoir comparer les plats et donc leurs ingrédients. Ajoutez une méthode `equals` dans la classe Ingrédient qui renvoie true si deux ingrédients ont le même nom d'aliment et le même état (pas forcément la même quantité).
1. Ajoutez une méthode `equals` dans la classe Plat, qui renvoie true si deux plats contiennent les mêmes ingrédients, au sens donné juste avant.
1. On veut faire la distinction entre les ingrédients qu'on peut cuire et ceux qu'on peut découper. Un ingrédient qu'on peut cuire doit avoir une méthode `cook()` qui le fait passer dans l'état `cooked` et une température de cuisson. Un ingrédient qu'on peut découper doit avoir une méthode `cut()` qui le fait passer dans l'état `cut`.
    - En utilisant uniquement l'héritage, proposer une solution à ce problème
    - En utilisant utilisant l'héritage et les interfaces, proposer une solution alternative à ce problème
    - Laquelle des deux solutions vous semble la meilleure ?

## Sources et références

-   [Exercices de Programmation Orientée Objet en Java - MIS](https://home.mis.u-picardie.fr/~furst/docs/exercicesPOO.pdf)
