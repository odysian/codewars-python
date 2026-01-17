// https://www.codewars.com/kata/515e271a311df0350d00000f/train/typescript

// Map to square, then reduce to sum.
export function squareSum(numbers: number[]): number {
  return numbers.map(x => x**2).reduce((x, y) => x + y, 0)
}