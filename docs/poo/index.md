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
