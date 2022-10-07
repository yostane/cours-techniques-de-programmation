---
tags:
  - techniques
  - fonctionnel
---

# Programmation fonctionnelle

La programmation fonctionnelle s'articule autour de [ces concepts](https://www.geeksforgeeks.org/functional-programming-paradigm) : fonctions pures, récursivité, transparence référentielle, variables immuables, fonctions en tant que citoyens de première classe et fonctions d'ordre supérieur.

!!! important
    Les langages fonctionnels purs fournissent ces fonctionnalités de manière native et les appliquent si possible au moment de la compilation.


## Immutabilité

- **L'immutabilité** signifient qu'on ne peut pas changer la valeur d'une variable ou ses propriétés une fois qu'elle a été créée. 
- Pour changer de valeur, nous devons créer une copie tout en renseignant les nouvelles valeur.
- Avec les objets, on classifie l'immutabilité en deux catégories:
    - **Immutabilité profonde**: On ne peut pas modifier un objet ou ses membres quelque soit leurs niveaux de hiérarchie ou leurs profondeurs `o.a.b.c...`. Dans le cas d'une collection, on ne peut plus lui ajouter ou supprimer d'éléments.
    - **Immutabilité peu profonde**: On ne peut pas modifier la variable en elle même mais on peut modifier ses membres si c'est un objet ou ajouter et supprimer des éléments si c'est une collection.
- Avec les tableaux, on a deux types d'immutabilité:
    - **Tableau immutable**: On ne peut ni ajouter ou supprimer des éléments, ni changer la valeur des éléments existants.
    - **Tableau en lecture seule**: On ne peut ni ajouter ou supprimer des éléments mais on peut changer la valeur des éléments existants.
- L'immutabilité profonde est la meilleure forme d'immutabilité.
    - En TypeScript, on peut le satisfaire en déclarant systématiquement en `readonly` toutes les propriétés et les tableaux.
    - En Rust, tout est immutable par défaut sauf si on utilise le qualificateur `mut`.
- La modification d'un objet immutable se fait sur une **copie profonde**. Cette dernière peut être réalisée en une seule ligne ou *à la main* (en copiant les champs un par un), selon le langage utilisé.

!!! attention "Limite avec les fonctions de clonage profond"
    Les fonctions de clonage profond qui ne permettent pas de spécifier les propriétés à modifier ne sont pas utiles car elles génèrent une copie conforme à l'original qu'on ne pourra plus modifier.

```ts title="Immutabilité"
--8<--
immutability_demo.ts
--8<--
```


## Fonctions pures et transparence référentielle

- **Les fonctions pures** sont des fonctions qui n'ont pas d'effets secondaires et renverront donc toujours la même sortie étant donné la même entrée.
- [**Transparence référentielle**](https://ericnormand.me/podcast/what-is-referential-transparency) : signifie qu'une expression peut être remplacée par son résultat sans modifier le comportement du programme. 
    - :bulb: La transparence fait référence au fait que implémentation de l'expression n'est pas pertinente.

## Les fonctions comme citoyens de première classe

- Les fonctions sont des citoyens de première classe : elles peuvent être affectées à une variable ou utilisées dans des fonctions d'ordre supérieur (passées en tant que paramètre de fonction à une autre fonction ou renvoyées par une fonction).

## Programmation déclarative

- La programmation usuelle est appeplée programmation impérative et résout le problème sous forme d'une suite d'instructions qui décrivent comment le programme doit se comporter étape par étape.
    - La boucle for est un exemple souvent utilisé pour illustrer la programmation impérative.
- La programmation fonctionnelle décrit le résultat sous d'un enchainements de fonctions.
- Permet d'exprimer ce que l'on veut obtenir mais pas comment l'obtenir.
- Les fonctions les plus connues sont: filter, map et reduce.



## Sources

- [learning-kotlin](https://worldline.github.io/learning-kotlin/en/kotlin-features/#functional-programming)
- [Rust: Constants, Variables, and Mutability - Oh My!](https://oswalt.dev/2020/03/rust-constants-variables-and-mutability-oh-my/)
- [Mutable and Immutable Arrays](https://www.educative.io/courses/learn-typescript-complete-course/q2Q6MZXP4yR)