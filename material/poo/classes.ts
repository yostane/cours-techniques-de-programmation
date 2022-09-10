class Ship {
  // En préfixant avec private, public ou protected, l'argument devient une propriété.
  constructor(protected speed: number) {}
  move() {
    console.log("Moving at speed", this.speed);
  }

  static staticValue = "Hello !";
}

// static members always exist
console.log(Ship.staticValue);

const ship = new Ship(200);
ship.move();

class SpaceShip extends Ship {
  constructor(speed: number, public staelliteCount: number) {
    super(speed);
  }
}

const spaceShip = new SpaceShip(1000, 5);
console.log("The space ship has ", spaceShip.staelliteCount, " sattelites");
