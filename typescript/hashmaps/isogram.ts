// https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/typescript

export function isIsogram(str: string): boolean{
  str = str.toLowerCase();
  let seen = new Set<string>();
  
  for (const char of str) {
    if (seen.has(char)) {
      return false;
    }
    seen.add(char);
  }
  return true;
}