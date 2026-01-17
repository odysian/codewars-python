export const fizzbuzz = (n: number): (string | number)[] => {
  let res: (string | number)[] = [];
  
  for (let i = 1; i <= n; i++) {
    let word: string = "";
    
    if (i % 3 === 0) word += "Fizz";
    if (i % 5 === 0) word += "Buzz";
    
    res.push(word || i);
  }
  
  return res;
}