// https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/typescript 

export const toJadenCase = (jaden: string) => {
  return jaden.split(" ").map((x) => x[0].toUpperCase() + x.slice(1)).join(" ")
}
