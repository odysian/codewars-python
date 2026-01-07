// https://www.codewars.com/kata/52f3149496de55aded000410/train/typescript

export function sumDigits(n: number): number {
  // Convert n to string
  let strNum: string = String(Math.abs(n));
  // Split and map back to number
  let numList: number[] = strNum.split("").map(Number)
  // Reduce array with arrow function to sum nums
  return numList.reduce((acc, curr) => acc + curr, 0)
}

export const sumDigits1 = (n:number): number => 
  String(Math.abs(n))
    .split("")
    .map(Number)
    .reduce((acc ,curr) => acc + curr, 0)