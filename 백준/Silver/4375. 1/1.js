fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");


let answer = [];

for (let line of input) {
  const n = Number(line);

  let remainder = 1 % n;
  let length = 1;

  while (remainder !== 0) {
    remainder = (remainder * 10 + 1) % n;
    length++;
  }

  answer.push(length);
}

console.log(answer.join("\n"));
