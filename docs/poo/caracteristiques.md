# Quelques caractéristiques de la POO

## Classes abstraites et Interfaces

-   Une classe abstraite ou une interface ne peuvent être instanciés sauf via un objet anonyme (exemple en [TS](https://stackoverflow.com/questions/42766986/typescript-anonymous-class)).
-   Les classes abstraites et interfaces sont considérés comme des contrats.
-   Une interface liste des membres sans implémentation.
-   Une classe abstraite liste des membres avec ou sans implémentation.
-   Une classe (abstraite ou non) peut hériter d'une seule classe (abstraite ou non) et de plusieurs interfaces.
    -   :warning: Certaines langages autorisent l'héritage multiple de classes.
-   :bulb: En typescript, un objet est compatible avec tout object qui a les mêmes champs sans avoir à explicitement implémenter son interface ou classe. On dit que c'est du **duck typing**; si ça marche et se comporte comme un canard, alors c'est un canard.

```ts title="Classes abstraites et Interfaces"
--8<--
interface_abstract.ts
--8<--
```

## Objets littéraux

-   Certains langages permettent de créer des objets sans instancier une classe (non abstraite)
-   Les propriétés et méthodes sont données directement lors de la définition de l'objet.

```ts title="Objets littéraux"
--8<--
literal_object.ts
--8<--
```

## Propriétés et accesseurs

-   Une propriété permet d'accéder et / ou modifier une donnée de l'objet avec la syntaxe `objet.propriété`
-   Quand un propriété est utilisée en lecture, l'objet appelle une méthode qui retourne la valeur de la propriété. Cette méthode est appelée **getter**
-   Quand on affecte une valeur à une propriété, l'objet appelle une méthode qui modifie la valeur propriété. Cette méthode est appelée **setter**
-   Les **getters** et **setters** sont appelées **accesseurs**
-   :bulb: Certains langages gèrent nativement les accesseurs
-   Dans la plupart des cas, une propriété repose sur un variable privée de la classe.
    -   :star: On appelle ce genre de champ, un **backing field**
-   Les langages qui gèrent nativement les propriétés utilisent un **backing field** par défaut et nous permettent de personnaliser les accesseurs par la suite.
-   Les langages qui gèrent moins bien les propriétés laissent au développeur le soin de prévoir des méthodes **getPropriété** et **setPropriété** en avance.

```ts title="Propriétés"
--8<--
properties_demo.ts
--8<--
```
