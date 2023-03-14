interface Shooter {
  readonly shootPower: number;
  shoot(): void;
}
interface Transporter {
  readonly numberOfPeople: number;
}
abstract class Ship {
  constructor(protected speed: number) {
    console.log("Ship constructor");
  }
  abstract move(): void;
  sayHello() {
    console.log("Hello");
  }
}

class SpaceShip extends Ship implements Shooter, Transporter {
  constructor(
    speed: number,
    readonly staelliteCount: number,
    readonly numberOfPeople: number,
    readonly shootPower: number
  ) {
    console.log("SpaceShip constructor before super");
    super(speed);
    console.log("SpaceShip constructor after super");
  }
  move(): void {
    console.log("VROOOM");
  }
  shoot(): void {
    console.log(`Shooting with power ${this.shootPower}`);
  }
}

const spaceShip = new SpaceShip(1000, 5, 500, 10);
spaceShip.shoot();
console.log("The space ship has ", spaceShip.staelliteCount, " sattelites");

function checkPower(shooter: Shooter) {
  console.log("The shooter has power of", shooter.shootPower);
}

checkPower(spaceShip);

const literalShooter: Shooter = {
  shootPower: 6,
  shoot() {
    console.log("pew pew");
  },
};
literalShooter.shoot();
checkPower(literalShooter);
