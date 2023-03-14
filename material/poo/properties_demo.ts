class Mage {
  // Deux propriétés dont le backing field est généré automatiquement
  constructor(public name: string, public hp: number) {}
}

// La propriété name a des accesseurs peronnalisés
class OtherMage {
  constructor(name: string, public hp: number) {
    this._name = name;
  }

  // backing field
  private _name: string;

  get name() {
    console.log("🧹 getting name", this._name);
    return this._name;
  }

  set name(value) {
    console.log("🧙 setting name with new value", value);
    this._name = value.toLowerCase();
    console.log("🧙🏾 name with new value", this._name);
  }
}

const mage = new Mage("magus", 10);
mage.name = "magicus";
console.log(mage.name);

const otherMage = new OtherMage("sorcellus", 100);
otherMage.name = "sorcellicus";
console.log(otherMage.name);
