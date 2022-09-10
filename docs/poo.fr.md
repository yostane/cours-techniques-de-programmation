---
tags:
  - techniques
---

# La programmation orienté objet

- La poo permet de modéliser sous forme d'objets.
- Un objet contient des membres (propriétés et  méthodes).
- Un objet peut être créé (ou instancié) de différentes façons:
  - Les techniques communes: Objets littéraux, anonymes ou instanciation à partir d'une classe.
  - Autres techniques: Singletons,  bâtisseurs (Builders), Injection de dépendances.

## Classes

- Une classe définit l'ensemble des membres ses instances auront.
- Une classe peut être définie à partir de zéro, ou à partie d'une classe abstraite ou non. Cette technique s'appelle l'héritage.
- Une classe peut aussi implémenter des interfaces.
- Le constructeur est la première fonction qui est appelée lors de l'instanciation d'un objet.
  - Certains constructeurs permettent d'initialiser facilement les propriétés.
- Certains langages permettent de définir des modificateurs de visibilité pour ses membres. Voici les plus communs:
  - `private`: membre utilisable uniquement par sa classe.
  - `protected`: membre utilisable uniquement par sa classe ou celles qui en héritent.
  - `public`: membres utilisables depuis n'import où.
- D'autres modificateur peuvent être proposés selon le langage:
  - `abstract`: rend le membre abstraite
  - `readonly`: propriété en lecture seule (comme un `const`)

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



## Singleton

## Constructeur (Builder)

## Exercice

