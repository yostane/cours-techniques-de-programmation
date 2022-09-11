interface Transporter {
  readonly capacity: number;
}

class SpaceShip implements Transporter {
  constructor(
    readonly speed: number,
    readonly staelliteCount: number,
    readonly capacity: number,
    readonly shootPower: number
  ) {}
}

class Bus implements Transporter {
  constructor(readonly capacity: number) {}
}

function createTransporter(capacity: number): Transporter {
  // Can change type without changing caller
  return new Bus(capacity);
  //return new SpaceShip(10, 1, 4, 2200);
}

const transporter = createTransporter(2);
console.log(transporter);

class TransporterBuilder {
  private capacity = 0;
  constructor() {}
  setCapacity(capacity: number) {
    this.capacity = capacity;
    // retourner this permet d'autoriser le chainage
    return this;
  }

  build(): Transporter {
    return new Bus(this.capacity);
  }
}

const transporter2 = new TransporterBuilder().setCapacity(5).build();
console.log(transporter2);
