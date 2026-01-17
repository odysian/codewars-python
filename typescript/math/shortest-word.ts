// https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/typescript

export function findShort(s: string): number {
  let words = s.split(" ");
  let shortest = Infinity
  for (let word of words) {
    if (word.length < shortest) {
      shortest = word.length
    }
  }
  return shortest;
  
  return Math.min(...s.split(" ").map((x) => x.length))
}