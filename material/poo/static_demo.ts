// Méthode globale (pas conseillée si on veut suivre l'orienté objet)
export function subsctract(x: number, y: number): number {
  return x - y;
}

export const gravity = 10;

export class MathUtils {
  // doit être appelé depuis la classe
  static readonly PI = 3.14;
  // doit être appelé depuis la classe
  static add(x: number, y: number): number {
    return x + y;
  }
  // doit être appelé depuis une instance
  multiply(x: number, y: number): number {
    return x * y;
  }
}

console.log(MathUtils.PI);
console.log(MathUtils.add(2, 5));

const mu = new MathUtils();
console.log(mu.multiply(2, 5));

// erreur
//console.log(MathUtils.multiply(2, 5));

// On ne peut pas appeler du statique depuis un objet en TS
// console.log(mu.PI);
// console.log(mu.add(2, 5));
