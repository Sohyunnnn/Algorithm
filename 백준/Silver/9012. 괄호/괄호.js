const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");


const T = Number(input[0]);

const arr = input.slice(1);

for (let i = 0; i < T; i++) {
  const str = arr[i];
  let count = 0;
  let valid = true;

  for (const ch of str) {
    if (ch === "(") count++;
    else count--;

    if (count < 0) {
      valid = false;
      break;
    }
  }

  if (count !== 0) valid = false;

  console.log(valid ? "YES" : "NO");
}
