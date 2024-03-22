# Classes et héritage

- La poo permet de modéliser les éléments qu'on veut traiter sous forme d'**objets**.
- Un objet contient des **membres** (propriétés et méthodes).
- Un objet peut être **créé** (ou **instancié**) de différentes façons:
    - Les techniques communes: à partir d'une **classe** ou objets **littéraux**.
    - Techniques avancées: Singletons, monteurs (Builders), Injection de dépendances.

=== "Python"

    ```py title="Définition d'une classe"
    --8<--
    python/poo_01.py
    --8<--
    ```

## Exercice

Dans le code donné plus haut, identifier avec des commentaires les parties qui effectuent les opération suivantes: instanciation d'objet, définition d'une classe, définition d'une propriété, définition d'une méthode et appel d'une méthode.

??? "Solution"

    -   Définition d'une classe: `class Monster {}`
    -   Instanciation d'objet: `new Monster("Lapinou", 100);` et `new Monster("Chatounet", 0);`
    -   Définition de propriétés: `readonly name: string, readonly hp: number`
    -   Appel d'une méthode: `monster1.checkAlive();` et `monster2.checkAlive();`

## Classes et héritage simple

- Une classe définit l'ensemble des membres ses instances auront.
- Une classe peut être définie:
    - A partir de zéro,
    - Ou à partie d'une autre classe. :bulb: Cette technique s'appelle **l'héritage simple**,
    - Ou à partie de plusieurs classes. :bulb: Cette technique s'appelle **l'héritage multiple**. :boom: Très peu de langages proposent cette option.
- Une classe peut aussi implémenter des interfaces.
- Le **constructeur** est la première fonction qui est appelée lors de l'instanciation d'un objet.
    - Certains constructeurs permettent d'initialiser les propriétés avec peu de code.
- Certains langages permettent de définir des **modificateurs de visibilité** pour ses membres.
    - Modificateurs de visibilité (non disponible en Python):
        - `private`: membre utilisable uniquement par sa classe.
        - `protected`: membre utilisable uniquement par sa classe ou celles qui en héritent.
        - `public`: membres utilisables depuis n'import où.
    - D'autres modificateur peuvent être proposés selon le langage:
        - `abstract`: rend le membre abstrait
        - `readonly`: propriété publique en lecture seule (comme un `const`)
    - `static`: le membre existera tout le temps en un exemplaire accessible avec le nom de la classe

```ts title="Définition de deux classes dont une qui hérite de l'autre"
--8<--
classes.ts
--8<--
```
