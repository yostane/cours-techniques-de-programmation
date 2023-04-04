class MathUtils {
  static readonly PI = 3.14;
  static add(x: number, y: number): number {
    return x + y;
  }
  static multiply(x: number, y: number): number {
    return x * y;
  }
}

console.log(MathUtils.PI);
console.log(MathUtils.add(2, 5));

// On ne peut pas appeler du statique depuis un objet en TS
// const mu = new MathUtils();
// console.log(mu.PI);
// console.log(mu.add(2, 5));
