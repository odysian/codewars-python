// https://www.codewars.com/kata/5715eaedb436cf5606000381/train/typescript

export const positiveSum = (arr:number[]): number =>
  arr.reduce((sum, curr) => curr > 0 ? sum + curr : sum, 0);
