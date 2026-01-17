// https://www.codewars.com/kata/546e2562b03326a88e000020/train/typescript

// One liner
export class Kata {
  static squareDigits(num: number): number {
    // num to str, split, map to square each digit, join together again
    // + at start is like Number()
    return +String(num).split("").map(n => (+n) ** 2).join("");
  }
}

// Explicit
export class Kata1 {
  static squareDigits(num: number): number {
    let numList = String(num).split("")
    let squared = numList.map(n => (+n) ** 2)
    let resultString = squared.join("")
    return +resultString
  }
}