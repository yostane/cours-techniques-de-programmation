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

## Membres statiques

-   Un membre statique d'une classe est utilisable sans créer d'instance particulière
-   On peut appeler ou accéder à un membre statique depuis le nom de la classe. Certains langages permettent d'y accéder aussi depuis une instance.
-   Les membres statiques peuvent être considérées comme des variables et fonctions globales, sauf qu'elles sont classées dans une classe

```ts title="Propriétés"
--8<--
static_demo.ts
--8<--
```

## Polymorphisme

-   Consiste à donner des comportement différents à une méthode selon la classe qui l'implémente et quand on appelle la méthode depuis la classe mère, on aura la méthode de sa classe concrète qui sera appelée

```ts title="Propriétés"
--8<--
polymorphisme_demo.ts
--8<--
```

## Exercices

### Exo 1

Dans cet exercice, on manipule des formes géométriques que l'on définit par la classe abstraite `GeometricShape`. Cette dernière déclare deux méthodes abstraites `computeArea()` qui renvoie un nombre et `computePerimeter()` qui retourne un nombre.

1.  Définir les classes `Rectangle`, `Square` et `Circle` qui héritent de la classe `GeometricShape`.
1.  Définir la classe `Drawing` (dessin en Anglais) qui contient une liste de formes géométriques.
1.  Créer un programme qui instancie deux dessins avec chacun des formes géométriques différentes (4 formes environ par dessin).

### Exo 2

Un fermier veut modéliser ses animaux via leurs caractéristiques. Certain animaux peuvent crier, d’autres sont muets. On représentera le fait de crier au moyen d’une méthode affichant à l’écran le cri de l’animal.

1.  Ecrire une interface `Shouter` (crieur en Anglais) contenant la méthode permettant de crier qu'on appellera `shout()`.
1.  Ecrire les classes des chats `Cat`, des chiens `Dog` et des lapins `Rabbit` (qui sont muets)
1.  Ecrire un programme avec un tableau pour les animaux qui savent crier, le remplir avec 1 chiens et deux chats, puis faire crier tous ces animaux. Décrire ce qui s’affiche à l’écran à l’exécution de ce programme.
1.  L'éleveur donne un nom à chacun de ses animaux. Créer la classe abstraite `Animal` avec la propriété `name` qui est la classe mère de tous les animaux.
1.  Créer une classe `Farmer` (fermier en Français) qui contient un tableau d'animaux passé dans le constructeur.
1.  Créer une instance de la classe `Farmer` en lui passant tableaux d'animaux contenant trois chiens, deux chats et trois lapins.
1.  Le fermier souhaite retrouver facilement ses animaux pas leurs caractéristiques. Créer une méthode `findShoutingAnimals()` qui retourne un tableau des animaux du fermier qui crient (astuce: utiliser `if ("shout" in animal)` pour savoir si un animal peut crier).
    -   Pour info, `if ("shout" in animal)` n'est pas super propre mais c'est la méthode la plus simple pour débuter.
1.  Le fermier souhaite passer par une propriété calculée à la place de la méthode de la question précédente. Créer une propriété calculée `get shoutingAnimals()` qui retourne le même résultat que `findShoutingAnimals()`.
1.  Afficher le résultat de la méthode `findShoutingAnimals()` et la valeur de la propriété `get shoutingAnimals()`. Quelle syntaxe préférez-vous ?
1.  Le fermier élève également un Canari (Canary en Anglais). Il souhaite en profiter pour modéliser les caractéristiques voler et marcher de ses animaux. Définir la classe `Canary` ainsi que les interfaces `Walker` et `Flyer`. Mettre à jour les classes existantes pour implémenter les interfaces qui leurs correspondent.
1.  Créer une propriété calculée `get FlyingAnimals()` qui retourne une liste d'animaux qui volent.

### Exo 3

1. Créer une classe `Station` qui a deux champs en readonly: `id` de type number et `name` de type string.
1. Le constructeur ne prend que `name` en argument et `id` est généré via un compteur qui est incrémenté à chaque nouvelle instance créé (astuce, utiliser une propriété statique)
1. créer trois stations et vérifier que leur id est bien positionné.
1. définir une méthode `isEqualTo(s: Station)` qui retourne `true` si la station passée en argument à le même `id`
1. Faire quelques appels de `isEqualTo` sur différentes stations.

### Exo 4

Créer une classe StringUtils qui définit les méthodes statiques suivantes:

1. `askQuestion(message: string): string`: qui retourne une nouvelle chaîne de caractères qui est une concaténation un "?" à `message`
1. `countVowels(message: string): number` qui retourne le nombre de voyelles dans `message`
1. `removeVowels(message: string): string` qui retourne une nouvelle chaîne de caractères qui est `message` dépourvu de ses voyelles (en gardant l'ordre des lettres initiales)

## Sources

-   [cs108_21_final](https://cs108.epfl.ch/archive/21/x/cs108_21_final.pdf)
-   [TD Programmation Orientée Objet](https://www.irif.fr/~emiquey/enseignement/poo3/TD6.pdf)
-   [classe abstraite et interface](https://www.u-picardie.fr/ferment/java/chap12_c.html)
-   [Corrigés des exercices sur les interfaces](https://deptinfo.cnam.fr/Enseignement/CycleA/APA/nfa032/docs/corriges-interfaces-1.pdf)
