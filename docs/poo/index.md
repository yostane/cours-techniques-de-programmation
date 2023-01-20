# La programmation orientée objet (POO)

-   La poo permet de modéliser les éléments qu'on veut traiter sous forme d'objets.
-   Un objet contient des membres (propriétés et méthodes).
-   Un objet peut être créé (ou instancié) de différentes façons:
    -   Les techniques communes: Objets littéraux, anonymes ou instanciation à partir d'une classe.
    -   Autres techniques: Singletons, monteurs (Builders), Injection de dépendances.

## Motivation

## Classes

-   Une classe définit l'ensemble des membres ses instances auront.
-   Une classe peut être définie:
    -   A partir de zéro
    -   Ou à partie d'une autre classe. :bulb: Cette technique s'appelle **l'héritage**.
-   Une classe peut aussi implémenter des interfaces.
-   Le **constructeur** est la première fonction qui est appelée lors de l'instanciation d'un objet.
    -   Certains constructeurs permettent d'initialiser les propriétés avec peu de code.
-   Certains langages permettent de définir des modificateurs de visibilité pour ses membres. Voici les plus communs:
    -   `private`: membre utilisable uniquement par sa classe.
    -   `protected`: membre utilisable uniquement par sa classe ou celles qui en héritent.
    -   `public`: membres utilisables depuis n'import où.
-   D'autres modificateur peuvent être proposés selon le langage:
    -   `abstract`: rend le membre abstraite
    -   `readonly`: propriété en lecture seule (comme un `const`)
    -   `static`: le membre existera tout le temps en un exemplaire accessible avec le nom de la classe

```ts title="classes"
--8<--
classes.ts
--8<--
```
