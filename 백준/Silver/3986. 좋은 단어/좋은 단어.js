fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");


const N = Number(input[0]);

const arr = input.slice(1);

let count = 0;

for (let i = 0; i < N; i++) {
  const stack = [];

  for (const ch of arr[i]) {
    if (stack[stack.length - 1] === ch) {
      stack.pop(); // 짝 맞으면 없애기
    } else {
      stack.push(ch); // 다르면 쌓기
    }
  }
  if (stack.length === 0) count++;
}

console.log(count);
