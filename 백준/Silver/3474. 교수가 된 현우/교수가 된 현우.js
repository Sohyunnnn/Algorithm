const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");


const T = Number(input[0]);
const arr = input.slice(1).map(Number);

for (let i = 0; i < T; i++) {
  let n = arr[i];
  let count = 0;

  while (n >= 5) {
    count += Math.floor(n / 5);
    n = Math.floor(n / 5);
  }

  console.log(count);
}

