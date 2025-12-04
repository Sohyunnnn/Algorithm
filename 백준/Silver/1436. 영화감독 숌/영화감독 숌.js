fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim();


const N = Number(input);

let num = 0;

let count = 0;

while (true) {
  num++;
  if (num.toString().includes("666")) {
    count++;
  }
  if (count === N) {
    break;
  }
}

console.log(num);
