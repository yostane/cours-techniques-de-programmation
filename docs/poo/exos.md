# Exercices et compléments

## Exercices

### Exo 1

- On souhaite modéliser un collection de consoles et jeux rétro en utilisant les techniques de programmation orientée objet.
    - Définir les classes `VideoGame` et `VideoGameConsole`.
    - Chaque classe propose les propriétés: `name`, `releaseYear`.
    - `VideoGame` contient en plus une liste des consoles compatibles (pour les jeux cross-platform) via la propriété: `platforms`.
    - `VideoGameConsole` contient en plus la propriété: `companyName` de type string.
    - (⚠ à ne pas faire en Python) Définir toutes les propriétés en `readonly` dans le constructeur.
        - Quel est intérêt du qualificateur `readonly` ?
        - En TypeScript, est-ce que les propriétés sont publiques ou privées par défaut ? Est-ce le cas pour tous les langages ?
- On suppose que le collectionneur a une seule console du même modèle. C'est à dire qu'on peut avoir une instance statique (ou unique, ou globale) pour chaque console.
    - Créer une ServiceLocator qui permet de récupérer une instance unique de ces consoles avec les `name` et `companyName`:
        - `DegaDrive`, `Dega`.
        - `Satourne`, `Dega`.
        - `Super Nontendo`, `Nontendo`.
        - `Nontendo`, `Nontendo`.
        - Le choix du `releaseYear` est libre.
- Créer une factory `createDegaDriveVideoGame` pour créer des jeux dont la `platform` est "DegaDrive". Faire la même chose pour "Super Nontendo"
- Créer une factory `createCrossPlatformVideoGame` pour créer des jeux dont les plateformes sont `DegaDrive`, `Satourne`, `Super Nontendo`, `Nontendo`.
- Créer une liste `retroGames` qui contient 1 jeu pour "DegaDrive", un jeu pour "Super Nontendo" et un jeu cross-platform. Le choix du `name`, `releaseYear` est libre pour chaque jeu.

??? solution

    `ts
    --8<--
    solution_poo_exercise.ts
    --8<--
    `

### Exo 2

- Créez une classe `Point` qui possède deux propriétés x et y de type `number` correspondant aux coordonnées du point.
- Ajoutez une méthode print() qui affiche les coordonnées du point de cette façon (ici, x = 2 et y = 3): `Point | x : 2 | y : 3`
- Ajoutez une méthode `translate(tx,ty)` qui ajoute `tx` à `x` et `ty` à `y`.

### Exo 3

- Créez une classe `BankAccount` modélisant un compte en banque.
- La classe possède deux propriétés initialisées dans le constructeur.
    - `balance` correspond au solde du compte
    - `managementCost` qui correspond au frais de gestion du compte.
- Ajoutez une méthode `print()` qui affiche les information du compte de cette façon: `Compte ( solde: 1000€ | frais de gestion: 13€ )`
- Ajoutez une méthode `debit(amount: number)` qui enlève `amount` au solde du compte uniquement si le solde est suffisant. Elle retourne un booléen qui renvoie `true` si le débit a réussi, sinon `false`.
- Ajouter une méthode `send(bankAccount: BankAccount, amount: number)` qui transfère de l'argent vers un autre compte uniquement si le solde est suffisant. La méthode retourne un booléen calculé de la même façon que la méthode `debit`.

## Sources

- [Exercices sur la programmation orientée objet](https://kxs.fr/cours/poo/exercices)

## Aller plus loin

- [Patrons de conception de refactoring.guru](https://refactoring.guru/fr/design-patterns)
- [What is the difference between Builder Design pattern and Factory Design pattern?](https://stackoverflow.com/a/8959150)
- [howtodoinjava.com](https://howtodoinjava.com/design-patterns/)
- [TypeScript Getters and Setters from typescripttutorial.net](https://www.typescripttutorial.net/typescript-tutorial/typescript-getters-setters)
