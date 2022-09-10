class Mage {
  private constructor(public name: string, public hp: number) {}

  private static _instance = new Mage("", 0);

  static get instance(): Mage {
    return this._instance;
  }
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

  private static _thief = new Thief("Picflouz", 100);

  static get thief(): Thief {
    return this._thief;
  }
}

console.log(ServiceLocator.mage);
console.log(ServiceLocator.thief);
