# Quelques patrons de conception

## Singleton et service locator

-   La technique du singleton permet de manipuler une instance unique
-   Elle peut être mise en place via une propriété ou méthode statique d'une classe qui retourne la même instance de cette classe
-   :warning: **Le constructeur d'une classe singleton est privé**, pour interdire l'instanciation depuis du code externe
-   Il est aussi possible de centraliser les singletons dans une seule classe qu'on appelle **service locator**
-   Le service locator est préféré car il permet de centraliser la gestion des instances et peut apporter des fonctionnalités communes

```ts title="Propriétés"
--8<--
singleton_servicelocator.ts
--8<--
```

## Fabrique (Factory) et Monteur (Builder)

-   Une **fabrique** est une fonction qui génère des instances d'une classe via une fonction.
-   Un **monteur** est similaire à la fabrique avec la différence que les paramètres sont initialisés sous forme d'une série d'appels.
    -   :bulb: La technique du **chaînage d'appels** est souvent utilisée en complément.
-   Ces techniques permettent de substituer l'implémentation sans avoir à changer le code qui demande une instance.
-   Elle permettent aussi de proposer une syntaxe plus concise pour créer des objets complexes.

```ts title="Fabrique et monteur"
--8<--
factory_builder_demo.ts
--8<--
```

## Exercices

### Exo 1

On souhaite modéliser un garage qui répare des véhicules.
Un véhicule est identifié par son matricule et a un état `isBroken` de type booléen.

Il n'y qu'une instance de garage possible.
Le garage est identifié par son nom et permet de réparer un véhicule en basculant l'état `isBroken` à `false`.
Un véhicule réparé reste en garage tant que son propriétaire n'e l'a pas récupéré.
Si un véhicule n'est pas en panne, il est immédiatement remis à son propriétaire.

Un propriétaire est identifié par son nom et la listes des véhicules qu'il possède.
Le propriétaire ne peut pas récupérer un véhicule qu'il ne possède pas.

### Exo 2

Faire l'exercice 5.2 ce [cette série](https://home.mis.u-picardie.fr/~furst/docs/exercicesPOO.pdf) avec les différences suivants:

-   Utiliser TypeScript au lieu de Java
-   Définir des factory (monteurs) pour instancier les différents enseignants (`createResearcherLecturer()`, etc.)
