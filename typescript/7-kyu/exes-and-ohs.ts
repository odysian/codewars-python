// https://www.codewars.com/kata/55908aad6620c066bc00002a/train/typescript

export const xo = (str: string) : boolean  => { 
  let x = 0, o = 0;
  str = str.toLowerCase();
  
  for (let char of str) {
    if (char === "x") {
      x++;
    } else if (char === "o") {
      o++;
    }
  }
  return x === o;
}