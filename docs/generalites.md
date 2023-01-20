---
tags:
    - introduction
    - techniques
---

# Généralités

## Concepts de base en programmation

-   Variables et constantes.
    -   💡 Losque le langage permet d'en créer facilement (exemples: JS, TS et Kotlin), il est recommandé de créer des constantes par défaut et de changer en variables au besoin.
-   Fonctions et arguments.
    -   💡 Beaucoup de langages permettent de donner des valeurs par défaut aux arguments.
-   Structures de contrôle: if, for, for-each, while
-   Interpolation de chaînes de caractères.
-   Différence entre typage statique et dynamique.
    -   Typage statique: le type d'une variable ou d'un argument ne change pas.
    -   Typage dynamique: le type d'une variable ou d'un argument peut changer.
-   Si le compilateur déduit le type d'une donnée dans certaines situation sans qu'on ait à l'expliciter, on dit que c'est un **typage implicite**. C'est aussi appelé **l'inférence de types**.

```ts title="Quick tour of TypeScript"
--8<--
ts_tour.ts
--8<--
```

## Règles de nommage

-   Une variable porte un nom passif qui commence par une majuscule
-   Une variable de type collection (tableau, liste, etc.) porte un nom au pluriel
-   Le nom d'une fonction commence par un verbe.
    -   Dans la plupart des langages, le nom d'une fonction commence par une minuscule.
-   Respecter le type de séparation entre les mots d'un identifiant
    -   Kamel case
    -   Snake case
    -   Kebab case
