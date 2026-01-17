// https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/typescript

export class Kata {
  static getCount(str: string): number {
    // Set for quick lookups
    const vowels = new Set<string>(["a", "e", "i", "o", "u"]);
    let count = 0

    // +1 if s in vowels
    for (let s of str) {
      if (vowels.has(s)) {
          count++
      }
    }
    return count
  }
}