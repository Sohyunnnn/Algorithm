const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");


const N = Number(input[0]);

const arr = input.slice(1);

let score1 = 0;
let score2 = 0;
let time1 = 0;
let time2 = 0;
let prevTime = 0;

const toSeconds = (time) => {
  const [m, s] = time.split(":").map(Number);
  return m * 60 + s;
};

const toTime = (sec) => {
  const m = String(Math.floor(sec / 60)).padStart(2, "0");
  const s = String(sec % 60).padStart(2, "0");
  return `${m}:${s}`;
};

for (let i = 0; i < N; i++) {
  const [team, t] = arr[i].split(" ");
  const now = toSeconds(t);

  // 이전 시점부터 지금 시점까지 리드한 팀의 시간 더하기
  if (score1 > score2) time1 += now - prevTime;
  else if (score2 > score1) time2 += now - prevTime;

  // 득점 반영
  if (team === "1") score1++;
  else score2++;

  prevTime = now;
}

// 마지막 남은 시간도 반영 (경기 종료까지)
const end = 48 * 60;
if (score1 > score2) time1 += end - prevTime;
else if (score2 > score1) time2 += end - prevTime;

console.log(toTime(time1));
console.log(toTime(time2));
