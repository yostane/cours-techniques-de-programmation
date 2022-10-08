let amount: number = 400;
//amount = "Hello"; // error because TS est statically typed

// TypeScript allows to type implicitly in certain situations
const message = "hello";

function sayHello(s: string) {
  console.log(s);
}
sayHello("Hello");

// Type unions allows to allow multiple types to the same variable
let x: number | string = "Hello";
x = 5;
console.log(x);

// String interpolation possible with back-tick `
console.log(`I am an interpolated string ${x}, ${message}`);
