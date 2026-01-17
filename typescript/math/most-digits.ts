// https://www.codewars.com/kata/58daa7617332e59593000006/train/typescript

// Initial approach
export class Kata {
  static findLongest(array:number[]):number {
    let topLen: number = 0;
    let num: number = 0;
    
    for (const val of array) {
      const valLength = String(val).length;
      if (valLength > topLen) {
        topLen = valLength;
        num = val;
      }
    }
    return num;
  }
}

// Reduce approach
export class Kata1 {
  static findLongest(array: number[]): number {
    // "Reduce the array to a single number: the one with the most digits"
    return array.reduce((currentMax, num) => {
      // Compare string lengths
      return String(num).length > String(currentMax).length ? num : currentMax;
    });
  }
}