// https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/typescript

export function solution(str: string): string {
  let reversed = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }
  return reversed;
}