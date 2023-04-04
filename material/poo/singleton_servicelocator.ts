class Mage {
  private constructor(public name: string, public hp: number) {}

  static readonly instance = new Mage("", 0);
}

Mage.instance.hp = 200;
console.log(Mage.instance.hp);

class Thief {
  constructor(public name: string, public hp: number) {}
}

class ServiceLocator {
  static get mage(): Mage {
    return Mage.instance;
  }

  static readonly thief = new Thief("Picflouz", 100);
}

console.log(ServiceLocator.mage);
console.log(ServiceLocator.thief);
