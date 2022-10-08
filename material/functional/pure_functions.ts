/**
 * A pure function return the same output for the same input and does have side-effects
 */
function add(a: number, b: number) {
  return a + b;
}

/**
 * This function is impure because it does not always return the same output given the same input
 */
function addImpure1(a: number, b: number) {
  return a + b + Math.random();
}

/**
 * This function is impure because it has a side effect (write to the console)
 */
function addImpure2(a: number, b: number) {
  console.log(a, b);
  return a + b;
}
