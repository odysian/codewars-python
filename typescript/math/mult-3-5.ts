// https://www.codewars.com/kata/514b92a657cdc65150000006/train/typescript

export class Challenge {
  static solution(num: number) {
    let result: number = 0
    
    for (let i = 0; i < num; i++) {
      if (i % 3 === 0 || i % 5 === 0) {
        result += i
      }
    }
    return result;
  }
}