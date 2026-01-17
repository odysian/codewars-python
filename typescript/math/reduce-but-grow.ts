// https://www.codewars.com/kata/57f780909f7e8e3183000078/train/typescript

export function grow(arr: number[]): number {
  // Init total
  let total: number = 1
  // For loop adding product to total
  for (const num of arr) {
    total *= num
  }
  return total
}

export function grow1(arr: number[]): number {
	// Use reduce on array
  // Accumulator is like total, curr is current iteration
  // 1 is the starting value
  return arr.reduce((acc, curr) => acc * curr, 1);
}

export const grow2 = (arr:number[]): number => arr.reduce((acc, curr) => acc * curr, 1);