function randomIntFromInterval(min: number, max: number): number {
  // min and max included
  return Math.floor(Math.random() * (max - min + 1) + min);
}

function createRandomNumbers(): number[] {
  return [...Array(10).keys()].map(() => randomIntFromInterval(0, 20));
}

const numbers = createRandomNumbers();
console.log(numbers);

const sum = numbers.reduce((acc, cur) => acc + cur, 0);
const sumOfDouble = numbers
  .map((x) => x * 2)
  .reduce((acc, cur) => acc + cur, 0);
const sumOfDouble2 = numbers.reduce((acc, cur) => acc + cur * 2, 0);
const productOfExponentialEven = numbers
  .filter((x) => x % 2 === 0)
  .map((x) => Math.exp(x))
  .reduce((acc, cur) => acc * cur, 1);
const avg = sum / numbers.length;
const beforeAvg = numbers
  .filter((x) => x < avg)
  .reduce((acc, cur) => Math.max(acc, cur), -Infinity);
const beforeAvg2 = numbers
  .filter((x) => x < avg)
  .reduce((acc, cur) => (acc > cur ? acc : cur), -Infinity);
console.log(
  "sum",
  sum,
  "sumOfDouble",
  sumOfDouble,
  "productOfExponentialEven",
  productOfExponentialEven,
  "avg",
  avg,
  "beforeAvg",
  beforeAvg,
  beforeAvg2
);

class BinaryCalculator {
  constructor(readonly f: (x: number, y: number) => number) {}
  run(a: number, b: number) {
    const r = this.f(a, b);
    if (r > 10) {
      console.log("succes", r);
    } else {
      console.log("failure", r);
    }
  }
  runWithCallbacks(
    a: number,
    b: number,
    success: (x: number) => void,
    failure?: (x: { code: number; message: string }) => void
  ) {
    const r = this.f(a, b);
    if (r > 10) {
      success(r);
    } else if (failure !== undefined) {
      failure({
        code: 1,
        message: "Aie aie aie",
      });
    }
  }
}

const adder = new BinaryCalculator((x, y) => x + y);
adder.run(10, 5);
adder.runWithCallbacks(
  0,
  5,
  (x) => console.log("yahoo ! ", x),
  (e) => console.error("code:", e.code, "message:", e.message)
);

adder.runWithCallbacks(10, 5, (x) => console.log("yahoo ! ", x));

const minimizer = new BinaryCalculator(Math.min);
minimizer.run(10, 5);
minimizer.runWithCallbacks(
  0,
  5,
  (x) => console.log("yahoo ! ", x),
  (e) => console.error("code:", e.code, "message:", e.message)
);

minimizer.runWithCallbacks(12, 15, (x) => console.log("yahoo ! ", x));
