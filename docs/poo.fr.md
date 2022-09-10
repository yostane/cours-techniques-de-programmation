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

```ts title="classes"
class Ship {
  // En préfixant avec private, public ou protected, l'argument devient une propriété.
  constructor(protected speed: number) {}
  move() {
    console.log("Moving at speed", this.speed);
  }
}

const ship = new Ship(200);
ship.move();

class SpaceShip extends Ship {
  constructor(speed: number, public staelliteCount: number) {
    super(speed);
  }
}

const spaceShip = new SpaceShip(1000, 5);
console.log("The space ship has ", spaceShip.staelliteCount, " sattelites");

```

## Classes abstraites et Interfaces

- Une classe abstraite ou une interface ne peuvent être instanciés sauf via un objet anonyme (exemple en [TS](https://stackoverflow.com/questions/42766986/typescript-anonymous-class)).
- Les classes abstraites et interfaces sont considérés comme des contrats.
- Une interface liste des membres sans implémentation.
- Une classe abstraite liste des membres avec ou sans implémentation.
- Une classe (abstraite ou non) peut hériter d'une seule classe (abstraite ou non) et de plusieurs interfaces.
  - :warning: Certaines langages autorisent l'héritage multiple de classes.

```ts
interface Shooter {
    readonly shootPower: number;
    shoot(): void;
}
interface Transporter {
    readonly numberOfPeople: number;
}
abstract class Ship {
    constructor(protected speed: number) {}
    move(){
        console.log("Moving at speed", this.speed);
    }
}

class SpaceShip extends Ship implements Shooter, Transporter {
    constructor(speed: number, 
        readonly staelliteCount: number, 
        readonly numberOfPeople: number,
        readonly shootPower: number) {
        super(speed);
    }
    shoot(): void {
        console.log("Shooting with power", this.shootPower);
    }
}

const spaceShip = new SpaceShip(1000, 5, 500, 10);
spaceShip.shoot();
console.log("The space ship has ", spaceShip.staelliteCount, " sattelites")

function checkPower(shooter: Shooter) {
    console.log("The shooter has power of", shooter.shootPower);
}

checkPower(spaceShip);
```


## Objets littéraux et anonymes

- Certains langages permettent de créer des obets 

## Modificateurs de visibilité

## Propriétés et accesseurs



## Singleton

## Constructeur (Builder)

## Exercice

