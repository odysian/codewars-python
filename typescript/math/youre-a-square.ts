// https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/typescript

export default function isSquare(n: number): boolean {
  if (n<0) return false;
  
  // return true if sqrt is a whole number
  return Math.sqrt(n) % 1 === 0;
};
