// https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/typescript

export const multiTable = (number:number):string => {
  let res: string[] = [];
  for (let i = 1; i <= 10; i++) {
    res.push(`${i} * ${number} = ${i * number}`);
  }
  return res.join("\n");
}