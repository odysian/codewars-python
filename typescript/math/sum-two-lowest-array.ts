// https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/typescript

export function sumTwoSmallestNumbers(numbers:Array<number>):number {  
  let min1 = Infinity; // First place
  let min2 = Infinity; // Second place
  
  for (let num of numbers) {
    // If new lowest, first place goes to second
    if (num < min1) {
      min2 = min1;
      min1 = num;
      // If lower than 2nd place, put it there
    } else if (num < min2) {
      min2 = num;
    }
  }
  return min1 + min2
}