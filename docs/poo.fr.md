---
tags:
    - techniques
---

# La programmation orienté objet

- La poo permet de modéliser sous forme d'objets.
- Un objet contient des membres (propriétés et  méthodes).
- Un objet peut être créé (ou instancié) de différentes façons:
    - Les techniques communes: Objets littéraux, anonymes ou instanciation à partir d'une classe.
    - Autres techniques: Singletons,  monteurs (Builders), Injection de dépendances.

## Classes

- Une classe définit l'ensemble des membres ses instances auront.
- Une classe peut être définie:
    - A partir de zéro
    - Ou à partie d'une autre classe. :bulb: Cette technique s'appelle **l'héritage**.
- Une classe peut aussi implémenter des interfaces.
- Le **constructeur** est la première fonction qui est appelée lors de l'instanciation d'un objet.
    - Certains constructeurs permettent d'initialiser les propriétés avec peu de code.
- Certains langages permettent de définir des modificateurs de visibilité pour ses membres. Voici les plus communs:
    - `private`: membre utilisable uniquement par sa classe.
    - `protected`: membre utilisable uniquement par sa classe ou celles qui en héritent.
    - `public`: membres utilisables depuis n'import où.
- D'autres modificateur peuvent être proposés selon le langage:
    - `abstract`: rend le membre abstraite
    - `readonly`: propriété en lecture seule (comme un `const`)
    - `static`: le membre existera tout le temps en un exemplaire accessible avec le nom de la classe

```ts title="classes"
--8<--
classes.ts
--8<--
```

## Classes abstraites et Interfaces

- Une classe abstraite ou une interface ne peuvent être instanciés sauf via un objet anonyme (exemple en [TS](https://stackoverflow.com/questions/42766986/typescript-anonymous-class)).
- Les classes abstraites et interfaces sont considérés comme des contrats.
- Une interface liste des membres sans implémentation.
- Une classe abstraite liste des membres avec ou sans implémentation.
- Une classe (abstraite ou non) peut hériter d'une seule classe (abstraite ou non) et de plusieurs interfaces.
    - :warning: Certaines langages autorisent l'héritage multiple de classes.
- :bulb: En typescript, un objet est compatible avec tout object qui a les mêmes champs sans avoir à explicitement implémenter son interface ou classe. On dit que c'est du **duck typing**; si ça marche et se comporte comme un canard, alors c'est un canard.

```ts title="Classes abstraites et Interfaces"
--8<--
interface_abstract.ts
--8<--
```

## Objets littéraux

- Certains langages permettent de créer des objets sans instancier une classe (non abstraite)
- Les propriétés et méthodes sont données directement lors de la définition de l'objet.

```ts title="Objets littéraux"
--8<--
literal_object.ts
--8<--
```

## Propriétés et accesseurs

- Une propriété permet d'accéder et / ou modifier une donnée de l'objet avec la syntaxe `objet.propriété`
- Quand un propriété est utilisée en lecture, l'objet appelle une méthode qui retourne la valeur de la propriété. Cette méthode est appelée **getter**
- Quand on affecte une valeur à une propriété, l'objet appelle une méthode qui modifie la valeur propriété. Cette méthode est appelée **setter**
- Les **getters** et **setters** sont appelées **accesseurs**
- :bulb: Certains langages gèrent nativement les accesseurs
- Dans la plupart des cas, une propriété repose sur un variable privée de la classe.
    - :star: On appelle ce genre de champ, un **backing field**
- Les langages qui gèrent nativement les propriétés utilisent un **backing field** par défaut et nous permettent de personnaliser les accesseurs par la suite.
- Les langages qui gèrent moins bien les propriétés laissent au développeur le soin de prévoir des méthodes **getPropriété** et **setPropriété** en avance.

```ts title="Propriétés"
--8<--
properties_demo.ts
--8<--
```

## Singleton et service locator

- La technique du singleton permet de manipuler une instance unique
- Elle peut être mise en place via une propriété ou méthode statique d'une classe qui retourne la même instance de cette classe
- :warning: **Le constructeur d'une classe singleton est privé**, pour interdire l'instanciation depuis du code externe
- Il est aussi possible de centraliser les singletons dans une seule classe qu'on appelle **service locator**
- Le service locator est préféré car il permet de centraliser la gestion des instances et peut apporter des fonctionnalités communes

```ts title="Propriétés"
--8<--
singleton_servicelocator.ts
--8<--
```

## Fabrique (Factory) et Monteur (Builder)

- Une **fabrique** est une fonction qui génère des instances d'une classe via une fonction.
- Un **monteur** est similaire à la fabrique avec la différence que les paramètres sont initialisés sous forme d'une série d'appels.
    - :bulb: La technique du **chaînage d'appels** est souvent utilisée en complément.
- Ces techniques permettent de substituer l'implémentation sans avoir à changer le code qui demande une instance.
- Elle permettent aussi de proposer une syntaxe plus concise pour créer des objets complexes.

```ts title="Fabrique et monteur"
--8<--
factory_builder_demo.ts
--8<--
```

## Exercices

- On souhaite modéliser un collection de consoles et jeux rétro en utilisant les techniques de programmation orienté objet.
    - Définir les classes `VideoGame` et `VideoGameConsole`.
    - Chaque classe propose les propriétés: `name`, `releaseYear`.
    - `VideoGame` contient en plus une liste des consoles compatibles (pour les jeux cross-platform) via la propriété: `platforms`.
    - `VideoGameConsole` contient en plus la propriété: `companyName` de type string.
    - Définir toutes les propriétés en `readonly` dans le constructeur.
- Quel est intérêt du qualificateur `readonly` ?
- En TypeScript, est-ce que les propriétés sont publiques ou privées par défaut ? Est-ce le cas pour tous les langages ?
- On suppose que le collectionneur a une seule console du même modèle. C'est à dire qu'on peut avoir une instance statique (ou unique, ou globale) pour chaque console. Créer une ServiceLocator qui permet de récupérer une instance unique de ces consoles avec les `name` et `companyName`: 
    - `DegaDrive`, `Dega`.
    - `Satourne`, `Dega`.
    - `Super Nontendo`, `Nontendo`.
    - `Nontendo`, `Nontendo`.
    - Le choix du `releaseYear` est libre.
- Créer une factory `createDegaDriveVideoGame` pour créer des jeux dont la `platform` est "DegaDrive". Faire la même chose pour "Super Nontendo"
- Créer une factory `createCrossPlatformVideoGame` pour créer des jeux dont les plateformes sont `DegaDrive`, `Satourne`, `Super Nontendo`, `Nontendo`.
- Créer une liste `retroGames` qui contient 1 jeu pour "DegaDrive", un jeu pour "Super Nontendo" et un jeu cross-platform. Le choix du `name`, `releaseYear` est libre pour chaque jeu.

```ts title="Fabrique et monteur"
--8<--
solution_poo_exercise.ts
--8<--
```

## Références

- [Patrons de conception de refactoring.guru](https://refactoring.guru/fr/design-patterns)
- [What is the difference between Builder Design pattern and Factory Design pattern?](https://stackoverflow.com/a/8959150)
- [howtodoinjava.com](https://howtodoinjava.com/design-patterns/)
- [TypeScript Getters and Setters from typescripttutorial.net](https://www.typescripttutorial.net/typescript-tutorial/typescript-getters-setters)