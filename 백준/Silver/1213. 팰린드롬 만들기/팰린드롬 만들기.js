const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin") // 백준용
  .toString()
  .trim()
  .split("");

input.sort();

const counts = {};
for (const ch of input) counts[ch] = (counts[ch] || 0) + 1;

let oddCount = 0;
let center = "";
for (const key in counts) {
  if (counts[key] % 2 === 1) {
    oddCount++;
    center = key; // 홀수인 문자는 가운데에 위치
  }
}

if (oddCount > 1) {
  console.log("I'm Sorry Hansoo");
  process.exit(0);
}

// 절반 만들기
let half = "";
for (const key of Object.keys(counts).sort()) {
  half += key.repeat(Math.floor(counts[key] / 2));
}

// 팰린드롬 완성
const palindrome = half + center + half.split("").reverse().join("");
console.log(palindrome);
