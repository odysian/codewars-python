// https://www.codewars.com/kata/554b4ac871d6813a03000035/train/typescript

export class Kata {
  static highAndLow(numbers: string): string {
    // Split on spaces, then map each to number
    const nums: number[] = numbers.split(" ").map(Number);
    // Math.min/max
    // The ... (spread operator) takes the array and "spreads" it out into individual arguments.
    const maxNum = Math.max(...nums);
    const minNum = Math.min(...nums);
    return `${maxNum} ${minNum}`
  }
}