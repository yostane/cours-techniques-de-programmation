# Exercices

-   On souhaite modéliser un collection de consoles et jeux rétro en utilisant les techniques de programmation orientée objet.
    -   Définir les classes `VideoGame` et `VideoGameConsole`.
    -   Chaque classe propose les propriétés: `name`, `releaseYear`.
    -   `VideoGame` contient en plus une liste des consoles compatibles (pour les jeux cross-platform) via la propriété: `platforms`.
    -   `VideoGameConsole` contient en plus la propriété: `companyName` de type string.
    -   Définir toutes les propriétés en `readonly` dans le constructeur.
-   Quel est intérêt du qualificateur `readonly` ?
-   En TypeScript, est-ce que les propriétés sont publiques ou privées par défaut ? Est-ce le cas pour tous les langages ?
-   On suppose que le collectionneur a une seule console du même modèle. C'est à dire qu'on peut avoir une instance statique (ou unique, ou globale) pour chaque console. Créer une ServiceLocator qui permet de récupérer une instance unique de ces consoles avec les `name` et `companyName`:
    -   `DegaDrive`, `Dega`.
    -   `Satourne`, `Dega`.
    -   `Super Nontendo`, `Nontendo`.
    -   `Nontendo`, `Nontendo`.
    -   Le choix du `releaseYear` est libre.
-   Créer une factory `createDegaDriveVideoGame` pour créer des jeux dont la `platform` est "DegaDrive". Faire la même chose pour "Super Nontendo"
-   Créer une factory `createCrossPlatformVideoGame` pour créer des jeux dont les plateformes sont `DegaDrive`, `Satourne`, `Super Nontendo`, `Nontendo`.
-   Créer une liste `retroGames` qui contient 1 jeu pour "DegaDrive", un jeu pour "Super Nontendo" et un jeu cross-platform. Le choix du `name`, `releaseYear` est libre pour chaque jeu.

??? solution

    `ts
    --8<--
    solution_poo_exercise.ts
    --8<--
    `
