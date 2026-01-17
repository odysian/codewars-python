// https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/typescript

export function descendingOrder(n: number): number {
  let numList = n.toString().split("");
  numList.sort((a, b) => (+b) - (+a));
  return Number(numList.join(""));
}

export const descendingOrder1 = (n: number): number =>
  +n.toString().split("").sort((a,b) => (+b) - (+a)).join("");
