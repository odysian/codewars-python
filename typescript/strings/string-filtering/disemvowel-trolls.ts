// https://www.codewars.com/kata/52fba66badcd10859f00097e/train/typescript

export class Kata {
  static disemvowel(str: string): string {
    const vowels = "aeiouAEIOU";
    
    return str
      .split("")
      .filter(char => !vowels.includes(char))
      .join("")
  }
}