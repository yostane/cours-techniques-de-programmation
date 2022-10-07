const words = ["I", "love", "TypeScript", "in", "2022"];

// Count the total number of letters for all words that contain the letter 'i'

let totalImperative = 0;
for (const word of words) {
  if (word.includes("i")) {
    totalImperative += word.length;
  }
}
console.log("Imperative style: ", totalImperative);

const totalDeclarative = words
  .filter((w) => w.includes("i"))
  .map((w) => w.length)
  .reduce((acc, cur) => acc + cur, 0);

console.log("Declarative style:", totalDeclarative);
