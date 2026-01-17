// https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/typescript

// Dumb approach
export function humanYearsCatYearsDogYears(humanYears: number): [number, number, number] {
  let catYears = 0;
  let dogYears = 0;

  for (let i = 1; i <= humanYears; i++) {
    if (i === 1) {
      catYears += 15;
      dogYears += 15;
      continue;
    }
    if (i === 2) {
      catYears += 9;
      dogYears += 9;
      continue;
    }
    catYears += 4;
    dogYears += 5;
  }
  return [humanYears, catYears, dogYears];
}

// Math Approach
export function humanYearsCatYearsDogYears1(humanYears: number): [number, number, number] {
  if (humanYears === 1) return [1, 15, 15];
  if (humanYears === 2) return [2, 24, 24];

  const extraYears = humanYears - 2;

  return [
    humanYears,
    24 + (extraYears * 4),
    24 + (extraYears * 5)
  ];
}