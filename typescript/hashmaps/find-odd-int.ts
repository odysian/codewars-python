// https://www.codewars.com/kata/54da5a58ea159efa38000836/train/typescript

export const findOdd = (xs: number[]): number => {
  let freq: Record<number, number> = {};
  
  for (let x of xs) {
    freq[x] = (freq[x] || 0) + 1;
    }
  
  for (let key in freq) {
    if (freq[key] % 2 !== 0) {
      return Number(key)
    } 
  }
  return 0
};
