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

Dans le code donné plus haut, identifier les parties du code qui effectuent les opération suivantes: instanciation d'objet, définition d'une classe, définition d'une propriété, définition d'une méthode et appel d'une méthode.

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
-   Certains langages permettent de définir des modificateurs de visibilité pour ses membres. Voici les plus communs:
    -   `private`: membre utilisable uniquement par sa classe.
    -   `protected`: membre utilisable uniquement par sa classe ou celles qui en héritent.
    -   `public`: membres utilisables depuis n'import où.
-   D'autres modificateur peuvent être proposés selon le langage:
    -   `abstract`: rend le membre abstrait
    -   `readonly`: propriété en lecture seule (comme un `const`)
    -   `static`: le membre existera tout le temps en un exemplaire accessible avec le nom de la classe

```ts title="Définition de deux classes dont une qui hérite de l'autre"
--8<--
classes.ts
--8<--
```

## Exercice

- Définir une classe `Book` avec les propriétés suivantes: nbPages, auteur, isbn.
    - Créer une classe `Library` (Bibliothèque) qui contient un tableau de livres.
    - Est-ce que les `Book` peuvent exister indépendamment de `Library` ?
- L'héritage est une relation "est". Par exemple, une `Hydra` (hydre)  est une monstre donc on écrira `Hydra extends Monster`. Donner des exemples de relation d'héritage.
