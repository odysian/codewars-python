// https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/typescript

// Use typeof to check if number
export const filter_list = (l:Array<any>):Array<number> => {
  const res: number[] = []
  for (const i of l) {
    if (typeof i === 'number') {
     res.push(i)
    }
  }
  return res;
} 

// Use filter to be more concise
export const filter_list1 = (l:Array<any>):Array<number> => {
  return l.filter(a => typeof a === 'number')
} 