// https://www.codewars.com/kata/5680781b6b7c2be860000036/train/typescript

export const vowelIndices = (word: string): number[] => {
  const vowels = new Set(['a', 'e', 'i', 'o', 'u', 'y']);
  let res: number[] = [];
  for (let i = 0; i < word.length; i++) {
    if (vowels.has(word[i].toLowerCase())) {
      res.push(i + 1)    
    }
  }
  return res;
}