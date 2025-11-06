const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");


const [A, B, C] = input[0].split(" ").map(Number);

const times = input.slice(1).map((line) => line.split(" ").map(Number));

let result = Array(100).fill(0);

for (let i = 0; i < times.length; i++) {
  for (let j = times[i][0]; j < times[i][1]; j++) {
    result[j] += 1;
  }
}

const counts = { 1: 0, 2: 0, 3: 0 };

for (const x of result) {
  if (counts[x] !== undefined) counts[x]++;
}

let total = 0;

total = counts[1] * A + counts[2] * 2 * B + counts[3] * 3 * C;

console.log(total);
