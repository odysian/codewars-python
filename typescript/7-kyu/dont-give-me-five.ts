// https://www.codewars.com/kata/5813d19765d81c592200001a/train/typescript

export function dontGiveMeFive(start:number, end:number) : number {
  // Array of nums
  let count: number[] = []
  // ! is not operator, convert to string, check if '5' in str
  for (let i = start; i < end + 1; i++) {
    if (!String(i).includes('5')) {
      count.push(i);
    }
  }
  // .length doesnt have ()
  return count.length;
}

export const dontGiveMeFive1 = (start:number, end:number): number => {
  const range = Array.from(
    { length: end - start + 1 },
    (_, i) => start + i
  );
  return range.filter(n => !String(n).includes('5')).length
}