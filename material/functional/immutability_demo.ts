const items: readonly number[] = [1, 2];

// compile error
//items[0] = 2;

class Sauce {
  constructor(
    readonly mainIngredient: string,
    readonly secondaryIngredient: string
  ) {}
}

class Kebab {
  constructor(
    readonly name: string,
    readonly sauce: Sauce,
    ingredients: readonly string[]
  ) {}
}

const k1 = new Kebab("miam", new Sauce("tomate", "huile"), ["Salade, Oignons"]);
console.log(k1);
// deep copy, but useless here because we can't touch k2
const k2 = structuredClone(k1);
console.log(k2);

// Manual deep copy
const k3 = new Kebab(k1.name, k1.sauce, ["Olives"]);
console.log(k3);
