function add(a: number, b: number) {
  return a + b;
}

// a variable can point to a function
const f = add;
// As any usual variable, functions have a type (arg1: type1, ...) => return type
const g: (x: number, y: number) => number = add;
// A function used without () is not called and point to the location of its code
console.log("Function reference", f, add);
// A function reference can be called as any function
console.log("Function call", f(1, 2), add(2, -10));

// Arrow functions allow to assign a function to a vartiable or argument more quickly
// They are also called lambdas in other languages
const h = (x: number, y: number) => {
  return x * y;
};

/**
 * Arrow functions can be written in a single line
 * @param x
 * @param y
 * @returns the result of the expression x / y
 */
const p = (x: number, y: number) => x / y;

/**
 * compte is called a higher order function because
 * @param a left operand
 * @param b right operand
 * @param f a function that will be called with a and b as arguments
 */
function compute(a: number, b: number, f: (x: number, y: number) => number) {
  const result = f(a, b);
  console.log("f(a, b)", result);
}

console.log("compute call 1");
compute(5, 3, add);
console.log("compute call 2");
compute(5, 3, h);

// arrow functions allow to write more concise code in this case
compute(5, 3, (x, y) => x - y);
